#!/usr/bin/env perl

##################################################################################################################
##														##
##	Juan J. Tena, 2013											##
##	CABD													##
##	jjtenagu@upo.es												##
##														##
##	This script takes 4C-seq data in fastq format and returns different outputs: demultiplexed fastq	##
##	files (if the input file is multiplexed), clean bed files, wig files, smoothened bedGraph		##
##	files and statistically significant targets of each viewpoint. Together with the fastq input		##
##	file, it needs the primers, the enzymes used in the 4C experiment and the reference genome		##
##	in fasta format. The combination between the reference genome and the enzymes used must be		##
##	named the first time it is used, and next times can be invoked with this name (and then it's		##
##	not necessary to provide the reference genome and the enzymes file). This data will be stored		##
##	with the experiment name and a suffix: name_exp.4c1 is the Ògood fragmentsÓ file and name_exp.4c2	##
##	is the file with the intervals between the first enzyme restriction sites. The experiment name		##
##	can be provided with a full path, so it will be easier to find in the future.				##
##														##
##################################################################################################################

##########################################################################################
##				  							##
##  New in Version 3:		  							##
##  - No extension in bed2wig	  							##
##  - New targets calculation	  							##
##  - Targets files with header								##
## 											##
##  Version 4:										##
##  - cleanbed debugged									##
##  - enz_interv modified (now it doesn't add the restriction site to any fragment)	##
##											##
##  Version 5:										##
##  - demultiplexing removed (better with python script), now fqpath (f) is required	##
##  - bowtie output files are stored in 'mapfiles' folder				##
##  - checking of primers file improved							##
##											##
##########################################################################################

use strict;
use warnings;
use Getopt::Long;
use File::Temp qw(tempdir tempfile);
use File::Basename qw/ basename /;
use IO::File;
use Parallel::ForkManager;
use List::Util qw(shuffle max sum);
use Math::Trig;

$|=1;

my ($primfile,$fqpath,$bwtindex,$name_exp,$enzfile,$genome,$mappath);
my $threads=1;

GetOptions
(
    "f=s" => \$fqpath,
    "c=s" => \$primfile,
    "i=s" => \$bwtindex,
    "p=s" => \$threads,
    "n=s" => \$name_exp,
    "e=s" => \$enzfile,
    "g=s" => \$genome,
    "mappath=s" => \$mappath,
);

if ($fqpath && $mappath) {
    print "-fqpath option is not compatible with -mappath.\n";
    help();
}

my ($goodfrags,$enz_interv);
if ($name_exp) {
    $goodfrags=$name_exp.".4c1";
    $enz_interv=$name_exp.".4c2";
}

my $dir=File::Temp->newdir();
my $dirname=$dir->dirname;
my $rest_file1="$dirname/enz1";
my $rest_file2="$dirname/enz2";

if ((!$fqpath && !$mappath) || !$primfile || (!$bwtindex && !$mappath)) {help();}
unless ($name_exp && ((-s $goodfrags && -s $enz_interv) || ($enzfile && $genome))) {help();}

## read primers file

my %prim_seq;
my %prim_pos;
readprimers($primfile);


## read enzymes file and map the restriction sites
my %rest;
my %enz_len;
unless (-s $goodfrags && -s $enz_interv) {
    print "Finding restriction sites in $genome...\n";
    restriction_map($enzfile,$genome);    			# generates $dirname/enz1 and $dirname/enz2
    print "  done\nWriting '$goodfrags' and '$enz_interv'...";
    good_frags();						# generates $name_exp.".4c1"
    ## intervals between first restriction enzyme sites
    first_enz_intervals($rest_file1); 				# generates $name_exp.".4c2"
    print "  done\n";
}


## read the "good fragments" file and store the data in a hash
my %goodfrags=();
my %goodfrags2=();
print "Reading '$goodfrags' and '$enz_interv'...";
open FRAGS, $goodfrags or die $!;
while (<FRAGS>) {
    chomp;
    my @line=split /\t/;
    my $key1=$line[0].":".$line[1];
    my $key2=$line[0].":".$line[2];
    $goodfrags{$key1}=$line[2];    #   hash with interval values
    $goodfrags2{$key1}=1;
    $goodfrags2{$key2}=1;		# hash to compare first enzyme fragments and "good fragments"
}
close FRAGS;
print "  done\n";

my @fqfiles=();
my @mapfiles=();
if ($mappath) {
    @mapfiles=<$mappath/*.map>;
    my $err=0;
    foreach (@mapfiles) {
        my $name = file_name($_);
        if (!$prim_pos{$name}) {print "\nIt seems that files and primers names don't fit ($name)"; $err=1;}
    }
    if ($err==1) {die "\n\nAborted\n\n";}
}
else {
    ## map with bowtie
    @fqfiles=<$fqpath/*>;
    my $err=0;
    foreach (@fqfiles) {
	my $name = file_name($_);
	if ($name ne "lost" && !$prim_pos{$name}) {print "\nIt seems that files and primers names don't fit ($name)"; $err=1;}
    }
    if ($err==1) {die "\n\nAborted\n\n";}
    mkdir "mapfiles";
    print "Mapping with Bowtie...";
    open LOG, ">bowtie.log";
    foreach (@fqfiles) {
        unless (file_name($_) eq "lost") {
	    bowtiemap ($_, "mapfiles");
	}
    }
    print "  done\n";
    @mapfiles=<mapfiles/*.map>;
    close LOG;
}


## convert to bed and filter reads
mkdir "bedfiles";
print "Filtering reads...";
my $fork1 = new Parallel::ForkManager($threads);
foreach (@mapfiles) {
    $fork1->start and next;
    clean_bed($_);
    $fork1->finish;
}
$fork1->wait_all_children;
print "  done\n";

## convert bed to wig
my @bedfiles=<bedfiles/*.bed>;
mkdir "wigfiles";
my $fork2 = new Parallel::ForkManager($threads);
print "Converting bed files to wig...";
foreach (@bedfiles) {
    $fork2->start and next;
    bed2wig($_);
    $fork2->finish;
}
$fork2->wait_all_children;
print "  done\n";

## intervals between first restriction enzyme sites
## first_enz_intervals($rest_file1);	# generates $name_exp.".4c2"


## count reads in first enzyme fragments
mkdir "frags_counts";
my $fork3 = new Parallel::ForkManager($threads);
print "Counting reads in first enzyme fragments...";
foreach (@bedfiles) {
    $fork3->start and next;
    reads_in_frags($_);		## here the value is divided by 2 if both ends of the first enzyme fragment are good
    $fork3->finish;
}
$fork3->wait_all_children;
print "  done\n";

## smoothing

mkdir "smooth_data";

my $fork4 = new Parallel::ForkManager($threads);
print "Smoothing bed files...";
my @fragsfiles=<frags_counts/*.fragscounts>;
foreach (@fragsfiles) {
    $fork4->start and next;
    my $name=file_name($_);
    my $outfile="smooth_data/$name\_30frags_smooth.bedGraph";
    smooth($_,$outfile,$name);
    $fork4->finish;
}
$fork4->wait_all_children;
print "  done\n";

mkdir "targets";
my $fork5 = new Parallel::ForkManager($threads);
print "Calculating targets...";

foreach (@fragsfiles) {
    $fork5->start and next;
    my $name=file_name($_);
    my $smoothfile="smooth_data/$name\_30frags_smooth.bedGraph";
    my $outfile="targets/$name\_targets.txt";
    targets2($_,$smoothfile,$prim_pos{$name},$outfile);
    $fork5->finish;
}
$fork5->wait_all_children;
print "  done\n";

print "\nFinished!\n\n";
exit;

############################################################

sub help {
    print "\n4Cseq_pipe.pl script version 4 (May 2014)\n";
    print "\nUsage: 4Cseq_pipe.pl [options]\n";
    print "NOTE: this script uses Bowtie to map reads to the target genome and Bedtools to assign reads to restriction fragments.\n";
    print "      Bedtools, Bowtie and its index must be installed and available from \$PATH environment variable.\n";
    print "Options:\n";
    print "-f         path to folder with already demultiplexed input FASTQ files for each primer.\n";
    print "-c         primers file (must be tabular, three columns with primer name, seq and position chr0:000000)\n";
    print "-i         bowtie index of the target genome\n";
    print "-n         name of the experiment (genome and enzymes used). Next time you can reuse it and -e and -g options are not required\n";
    print "-e         enzymes file (must be tabular, two columns with name and restriction site). Enzymes should be in experimental order.\n";
    print "           Only required the first time that a combination genome/enzymes is used \n";
    print "-g         target genome in fasta format. Only required the first time that a combination genome/enzymes is used\n";
    print "-p         number of threads to use\n";
    print "-d         only demultiplex the fastq file. This option only requires -f and -c options\n";
    print "-mappath   path to folder with already mapped files for each primer (with .map extension). -i option is not required\n\n";
    exit;
}

sub readprimers {		# no exportable (write in external hash)
    my ($primfile)=@_;
    open PRIMERS, $primfile or die "cannot open primers file\n";
    while (<PRIMERS>) {
	chomp;
	my @line=split /\s+/;
	if ($#line!=2) {
	    die "\nBad primers file format (must be tabular, three columns with primer name, seq and position chr0:000000)\n";
	}
	my $name=$line[0];
	my $seq=uc($line[1]);
	my $pos=$line[2];
	
	$seq=~s/[^ACGTN]//g;
	$prim_seq{$name}=$seq;
	$prim_pos{$name}=$pos;
    }
    close PRIMERS;
}

sub read_fq {			# no exportable (read external hash)
    my ($fqfile)=@_;

    my $fqlen=`wc -l $fqfile`;
    chomp $fqlen;
    $fqlen=~s/$fqfile//;
    $fqlen=~s/ //g;
    my $totalfq=$fqlen/4;
    
    my %tmpfiles;
    
    if ($threads==1) {
        $tmpfiles{1}=$fqfile;
    }
    else {
        my $tmplen=int($fqlen/$threads);
        my $tmpstart=1;
        while (($tmplen/4)!=int($tmplen/4)) {$tmplen++;}
        foreach (1..$threads) {
	    my $tmp=File::Temp->new();
	    $tmpfiles{$_}=$tmp;
	    system("tail -n+$tmpstart $fqfile | head -n $tmplen > $tmp");
	    $tmpstart+=$tmplen;
	}	
    }
    return %tmpfiles;
}

sub bowtiemap {			# no exportable (write in external hash)
    my ($file, $dir) = @_;
    my $name=file_name($file);
    my $out = $dir."/".$name.".map";
    my $tmplog = File::Temp->new();
    system ("bowtie -p $threads -m 1 $bwtindex $file $out >> $tmplog 2>&1");
    my @log=<$tmplog>;
    my @write_log;
    push @write_log, "$name\n";
    foreach (@log) {
	if ($ ~= /^\#/) {
	    push @write_log, $_;
	}
    }
    print LOG "@write_log\n";    
}

sub clean_bed {			# no exportable (read external hash)
    my ($infile) = @_;
    my $name = file_name($infile);
    my $outfile = "bedfiles/".$name.".bed";
    my @viewpoint=split /:/, $prim_pos{$name};

    open IN, $infile;
    my $tmpout=File::Temp->new();
    open (OUT, ">$tmpout");
    
    while (<IN>) {
        my @line=split "\t",$_;
	my $strand=$line[1];
	my $chr=$line[2];
	my $seq=$line[4];
	my $start = $line[3] + 1;
	my $end = $start + length($seq) - 1;
	if (($chr eq $viewpoint[0]) && ($start>($viewpoint[1]-5000)) && ($end<($viewpoint[1]+5000))) {next;}
	my $pos=$end;
	my $newkey=$chr.":".$pos;
	while (!defined $goodfrags{$newkey} && $pos>0) {
            $newkey=$chr.":".$pos;
            $pos--;
        }
        if (defined $goodfrags{$newkey} && ($goodfrags{$newkey}>=$start)) {
            print OUT "$chr\t$start\t$end\t0\t0\t$strand\n";
        }
    }
    close IN;
    close OUT;
    system ("sort -k1,1 -k2,2n $tmpout > $outfile");
}

sub restriction_map {
    my ($restfile,$fasta)=@_;
    my %rest;
    my %outfiles;
    my %enz_len;
    my $cont_enz=1;
    
    open REST,$restfile or die "Could not open $restfile: $!\n";
    while (<REST>) {
        chomp;
        my @line=split /\s+/;
        if ($#line!=1) {
    	die "enzymes file is not in the correct format (must be tabular, two columns with name and site)\n";
        }
        my $name=$line[0];
        my $seq=uc($line[1]);
        $seq=~s/[^ACGTN]//g;
        my $rev=reverse $seq;
        $rev=~tr/ACTG/TGAC/;
        unless ($seq eq $rev) {
            die "$name restriction site is not a palindrome, it can't be processed\n";
        }
        $rest{$name}="$seq:$cont_enz";
	$cont_enz++;
        $enz_len{$name}=length $seq;  # hash with the size of each restriction site
    }
    close REST;
    my $max_len=max(values %enz_len);
    
    my $cont=0;
    foreach (keys %rest) {
	my @num_enz=split /:/,$rest{$_};
	my $num=$num_enz[1];
        open my $fh, q{>}, "$dirname/enz$num";
        $outfiles{$_} = $fh;
	$cont++;
	if ($cont>2) {die "The expected number of enzymes is 2\n";}
    }
    my $chr='';
    my $chr_pos=0;
    my $end_line='';
    
    open (IN, $fasta) or die "Could not open $fasta: $!\n";
    while (<IN>) {
        my $line=$_;
        chomp $line;
        if ($line =~ m/^>/) {
            $chr_pos=0;
            $end_line='';
            $chr=$line;
            $chr=~s/>//;
            print "Reading $chr\n";
        }
        else {
            foreach (keys %rest) {
                my $addtoline=substr $end_line,-($enz_len{$_}-1);
                my $newline=uc($addtoline.$line);
                my $offset=0;
		my @seq_enz=split /:/,$rest{$_};
		my $seq=$seq_enz[0];
                my $pos = index ($newline,$seq,$offset);
                while ($pos != -1) {                
                    my $start=$pos+$chr_pos+1-length $addtoline;
                    my $end = $start+$enz_len{$_}-1;
                    print {$outfiles{$_}} "$chr\t$start\t$end\t$_\n";
                    $offset = $pos + 1;
                    $pos = index $newline,$seq,$offset;
                }
            }
            $end_line=substr ($line,-($max_len));
            $chr_pos+=length $line;
        }
    }
    close IN;
    
    map  {close $outfiles{$_}} keys %outfiles;
}

sub first_enz_intervals {
    my ($file)=@_;
    open IN, $file or die "Could not open $file: $!";
    open OUT, ">$enz_interv";
    my ($chr1,$chr2,$pos1,$pos2)=('','','','');
    my $count=0;
    while (<IN>) {    
        my @line=split /\t/;
        if ($count==0) {
            $chr1=$line[0];
#            $pos1=int(($line[2]+$line[1])/2)+1;
	    $pos1 = $line[2] + 1;
            $count=1;
        }
        elsif ($count==1) {
            $chr2=$line[0];
#            $pos2=int(($line[2]+$line[1])/2);
	    $pos2 = $line[1] - 1;
            if (($chr1 eq $chr2) && ($pos2 > $pos1)) {
                print OUT "$chr1\t$pos1\t$pos2\n";
            }
            $chr1=$chr2;
#            $pos1=$pos2+1;
	    $pos1 = $line[2] + 1;
        }
    }
    close IN;
    close OUT;
}

sub good_frags {
    my $tmp=File::Temp->new();
    system ("cat $rest_file1 $rest_file2 | sort -k1,1 -k2n,2 > $tmp");
    open IN, "$tmp" or die $!;
    open GOOD, ">$goodfrags";
    my ($chr1,$chr2,$start1,$end1,$start2,$end2,$enz1,$enz2)=('','','','','','','','');
    my $count=0;
    while (<IN>) {
        chomp;
        if ($_ =~ /track/) {next;}
        else {
            my @line=split /\t/;
            if ($count==0) {
                $chr1=$line[0];
                $start1=$line[1];
		$end1=$line[2];
                $enz1=$line[3];
                $count=1;
            }
            elsif ($count==1) {
                $chr2=$line[0];
                $start2=$line[1];
		$end2=$line[2];
                $enz2=$line[3];
                if ($chr1 eq $chr2) {
		    if (($enz1 ne $enz2) && ($start2-$end1>40)) {
			my $startfrag=int(($end1+$start1)/2)+1;
			my $endfrag=int(($end2+$start2)/2);
			print GOOD "$chr1\t$startfrag\t$endfrag\n";
		    }
                }
                else {
                    $count=0;
                }
                ($chr1,$start1,$end1,$enz1)=($chr2,$start2,$end2,$enz2);
            }        
        }
    }   
    close IN;
    close GOOD;
}

sub bed2wig {
    my ($infile) = @_;
    my $extend=0;

    my $tempfile = File::Temp->new();
    `cat $infile |grep -v track | awk '{if (\$6 == \"+\") print \$1 \"\t\" \$2 \"\t\" \$2 + $extend \"\t\" \$4 \"\t\" \$5 \"\t\" \$6; else  print \$1 \"\t\" \$3 - $extend \"\t\" \$3 "\t" \$4 "\t" \$5 "\t" \$6}' | sort -k1,1 -k2g,2 > $tempfile`;

    open IN, $tempfile or die $!;
    my $name = file_name($infile);
    my $outfile="wigfiles/".$name.".wig";
    my $fh = new IO::File;
    if (not($fh->open($outfile, "w"))) { die "Can't open $outfile: $!";}

    my $step=10;
    my $color="0,0,0";
    my ($chr_new,$start_new,$end_new,$chr_old)=('','','','');
    my $end_old=0;
    my %data;
    
    print $fh "track type=wiggle_0 name=$name maxHeightPixels=64:64:11 color=$color visibility=full\n";
    
    sub print_data {
    	my ($fh, $current_seq, %data) = @_;
	my $pos_start = 0;
	my $pos_end = 0;
	my $pos_value = 0;
	
	my @positions = sort {$a <=> $b } keys %data;
	my @values = sort {$b <=> $a } values %data;
	return if $#positions < 0 or $values[0] <= 1;
	
	while ($positions[0] < 0) { shift @positions }
	printf $fh "fixedStep chrom=%s start=%s step=10 span=10\n", $current_seq, $positions[0] + 1;
	for my $pos (@positions) {
	    $pos_value = $data{$pos};		
	    printf $fh "%s\n", $pos_value;
	}
    }

    while (<IN>) {
        chomp;
        ($chr_new,$start_new,$end_new)=split /\t/;
            
        if (($chr_new ne $chr_old)||($start_new > ($end_old + $step))) {
	    print_data($fh, $chr_old, %data);
	    %data = ();
	    $chr_old = $chr_new;
        }
    
        for (my $i = int($start_new / $step) * $step; $i <= int($end_new / $step) * $step; $i += $step) {
	    $data{$i}++;
        }
	$end_old=$end_new;
    }

    print_data($fh, $chr_old, %data);

    close IN;
    close $fh;
}

sub reads_in_frags {
    my ($bedfile)=@_;
    my $fname=file_name($bedfile);
    my $outfile="frags_counts/$fname.fragscounts";
    my $tmpfile = File::Temp->new();
    system("intersectBed -c -a $enz_interv -b $bedfile > $tmpfile");
    open PEAKS, $tmpfile or die "Could not open $tmpfile: $!\n";
    open OUT, ">$outfile" or die "Could not open $outfile: $!\n";
    while (<PEAKS>) {
	chomp;
	my @peak=split /\t/;
	my $val=$peak[3];
	my $key1=$peak[0].":".$peak[1];
	my $key2=$peak[0].":".$peak[2];
	if (($goodfrags2{$key1})&&($goodfrags2{$key2})&&($val!=0)) {
	    $val/=2;
	}
	print OUT "$peak[0]\t$peak[1]\t$peak[2]\t$val\n";
    }
}

sub smooth {
    my ($infile,$outfile,$name)=@_;
    my $win=30;
    my %chrs;
    
    my ($upstr,$downstr);
    if (int($win/2)==$win/2) {
        $upstr=$win/2-1;
        $downstr=$win/2;
    }
    else {
        $upstr=int($win/2);
        $downstr=int($win/2);    
    }
    
    open IN, $infile or die "Could not open $infile: $!\n";
    while (<IN>) {
        my $line=$_;
        chomp $line;
        my @line=split /\s+/, $line;
        my ($chr,$start,$end,$val)=@line;
        push @{ $chrs{$chr} }, join ' ',@line[1..3];
    }
    close IN;
    
    my $tmp=File::Temp->new();
    open OUT, ">$tmp";
    foreach (keys %chrs) {
        my (@start,@end,@val);
        my $chr=$_;
        foreach (@{ $chrs{$chr} }) {
            my @elem=split /\s/;
            push @start,$elem[0];
            push @end,$elem[1];
            push @val,$elem[2];
        }
        for (my $i=0;$i<=$#val;$i++) {
            my $sum=0;
            for (my $j=$i-$upstr;$j<=$i+$downstr;$j++) {
                my $k=$j;
                if ($k<0) {$k=0;}
                if ($k>$#val) {$k=$#val;}
                $sum+=$val[$k];
            }
            if ($sum!=0) {
                my $average=$sum/$win;
                print OUT "$chr\t$start[$i]\t$end[$i]\t$average\n";
            }
        }
    }
    close OUT;
    system (qq(echo "track type=bedGraph name='$name smooth $win frags' description='$name smoothed (window: $win fragments)' visibility=full windowingFunction=maximum" > $outfile));
    system ("sort -k1,1 -k2n,2 $tmp >> $outfile");
}

sub targets2 {
    my ($raw,$infile,$fix,$outfile)=@_;
    my $num_rand=10;
    my $pval=1e-05;
    my $dist=2;
    my $indist=0.1;
    my $win=30;
    my $name=file_name($infile);

    $dist*=1000000;
    $indist*=1000000;

    my @fix=split/:/,$fix;

    my ($chr_fix,$pos_fix)=($fix[0],$fix[1]);
    my (@region,@values)=();
    my @percent95s=();

    ## selection of the area to calculate lambda
    open RAW, $raw or die "Could not open $raw: $!\n";
    while (<RAW>) {
        chomp;
        my @line=split /\s/;
        my ($chr,$start,$end,$val)=@line;
        if (($chr eq $chr_fix) && (($start > $pos_fix-$dist) && ($start < $pos_fix-$indist) || (($start > $pos_fix+$indist) && ($start < $pos_fix+$dist)))) {
            push @region, "$chr\t$start\t$end";
            push @values, "$val";
        }
    }


    ## randomizing and smoothing to calculate lambda
    for (my $i=1;$i<=$num_rand;$i++) {
        print "\rRandomizing progress: $i/$num_rand";
        my @rand_values=shuffle @values;
        my @new_region;
        for (my $j=0;$j<=$#region;$j++) {
            push @new_region, "$region[$j]\t$rand_values[$j]";
        }
        my @smoothed=smooth2(\@new_region,$win);
        push @percent95s, percent95(@smoothed);
    }
    my $lambda=max @percent95s;
    my (@results,@sum_val,@sum_pos)=();
    my $val='';
    my $count=0;

    open SMOOTH, $infile or die "Could not open $infile: $!\n";
    open OUT, ">$outfile";
    print OUT "track name=\"$name\_targets\" description=\"Statistically significant targets for $name\" visibility=1\n";

    while (<SMOOTH>) {
        if ($_ !~ /track/) {
            chomp;
            my @line=split /\s/;
            $val=$line[3];
            if ($val>$lambda) {
                my $pois=poisson($lambda,$val);
                if ($pois<$pval) {
                    push @sum_pos, $_;
                    push @sum_val, $val;
                    $count=1;
                }
                elsif (($pois>$pval)&&($count==0)) {
                    next;
                }
                elsif (($pois>$pval)&&($count==1)&&(@sum_pos)) {
                    my @first_line=split /\s/,$sum_pos[0];
                    my @last_line=split /\s/,$sum_pos[$#sum_pos];
                    my $val_mean=(sum @sum_val)/($#sum_val+1);
                    my $pois_mean=poisson($lambda,$val_mean);
                    if ($first_line[0] eq $last_line[0]) {
                        print OUT "$first_line[0]\t$first_line[1]\t$last_line[2]\t$pois_mean\n";
                    }
                    $count=0;
                    (@sum_pos,@sum_val)=();
                }            
            }
            else {
                if (($count==1)&&(@sum_pos)) {
                    my @first_line=split /\s/,$sum_pos[0];
                    my @last_line=split /\s/,$sum_pos[$#sum_pos];
                    my $val_mean=(sum @sum_val)/($#sum_val+1);
                    my $pois_mean=poisson($lambda,$val_mean);
                    if ($first_line[0] eq $last_line[0]) {
                        print OUT "$first_line[0]\t$first_line[1]\t$last_line[2]\t$pois_mean\n";
                    }                
                }
                $count=0;
                (@sum_pos,@sum_val)=();
            }
        }
    }
    close SMOOTH;
    close OUT;
}

sub get_max {			# exportable
    my @vals=();
    open IN, $_[0];
    while (<IN>) {
        if ($_ !~ /track/) {
            chomp;
            my @line=split /\s/;
            push @vals,$line[3];
        }
    }
    return max @vals;
}

sub poisson {			# exportable
    my ($lambda,$k)=@_;
    my $pois_val='';
    if ($lambda>30) {
        $pois_val=norm_pois($lambda,$k);
    }
    else {
        $pois_val=($lambda**$k)*exp(-$lambda)/factorial($k);    ## Poisson distribution
    }
    if ($pois_val eq "nan") {
        $pois_val=norm_pois($lambda,$k);
    }
    return $pois_val;
}

sub norm_pois {			# exportable
    my ($lambda,$k)=@_;
    my $norm_pois_val=exp(-(($k-$lambda)**2)/(2*$lambda))/sqrt(2*pi*$lambda);   ## Normal approximation of Poisson (for lambda > 30)
    return $norm_pois_val;
}

sub factorial {			# exportable
    my $n = shift;
    my $f = 1;
    $f *= $n-- while $n > 0;
    return $f;
}

sub media {			# exportable
    my @vals=();
    open IN, $_[0];
    while (<IN>) {
        if ($_ !~ /track/) {
            chomp;
            my @line=split /\s/;
            push @vals,$line[3];
        }
    }
    my $media=0;
    if (@vals!=0) {
	$media=(sum @vals)/($#vals+1);
    }
    return $media;
}


sub percent95 {
        my @vals=();
    foreach (@_) {
        my @line=split /\s/;
        push @vals,$line[3];
    }
    my $num95=@vals*0.95;
    my @sorted_vals=sort { $a <=> $b } @vals;
    return $sorted_vals[$num95-1];
}

sub smooth2 {
    my ($in,$win)=@_;
    my (@in)=@$in;
    my @out;
    
    my ($upstr,$downstr);
    if (int($win/2)==$win/2) {
        $upstr=$win/2-1;
        $downstr=$win/2;
    }
    else {
        $upstr=int($win/2);
        $downstr=int($win/2);    
    }
    
    my (@starts,@ends,@vals);
    my $chr;
    foreach (@in) {
        my @line=split /\s+/, $_;
        $chr=$line[0];
        push @starts,$line[1];
        push @ends,$line[2];
        push @vals,$line[3];
    }
    for (my $i=0;$i<=$#vals;$i++) {
        my $sum=0;
        for (my $j=$i-$upstr;$j<=$i+$downstr;$j++) {
            my $k=$j;
            if ($k<0) {$k=0;}
            if ($k>$#vals) {$k=$#vals;}
            $sum+=$vals[$k];
        }
        if ($sum!=0) {
            my $average=$sum/$win;
            push @out, "$chr\t$starts[$i]\t$ends[$i]\t$average\n";
        }
    }
    return @out;
}

sub file_name {
    my ($file) = @_;
    my @fname = split /\./, basename($file);
    pop @fname;
    return join ".", @fname;
}