#!/usr/bin/env perl


##  Juan J. Tena, 2013
##  jjtenagu@upo.es
##  CABD, Sevilla
##
##  smoothing of 4 columns files using a window of fragments
##  input format:   chr   start   end   value

use strict;
use warnings;
use Getopt::Long;
use File::Temp;

my ($infile,$win,$zero,$help,$round);

GetOptions
(
    "i=s" => \$infile,
    "w=i" => \$win,
    "z" => \$zero,
    "r" => \$round,
    "h" => \$help,
);

if ($help || !$infile || !$win) {die "Usage: smooth.pl -i INPUT_FILE -w WIN_SIZE [-z] (print zeros) [-r] (round result)\n\n";}

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

my @path=split /\//,$infile;
my @fname=split /\./,$path[-1];
my $name=$fname[0];
my $outfile=$name."_".$win."frags_smooth.bed";

open IN,$infile or die "Could not open $infile: $!\n";
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
        if ($sum!=0||(($sum==0)&&$zero)) {
            my $average=$sum/$win;
            if ($round) {
                $average = round_num($average);
            } 
            print OUT "$chr\t$start[$i]\t$end[$i]\t$average\n";
        }
    }
}
close OUT;
system (qq(echo "track type=bedGraph name='$name smooth $win frags' description='$name smoothed (window: $win fragments)' visibility=full windowingFunction=maximum" > $outfile));
system ("sort -k1,1 -k2n,2 $tmp >> $outfile");
exit;

sub round_num {
    my ($num) = @_;
    if ($num < 0) {
        return int($num - 0.5);
    }
    else {
        return int($num + 0.5);    
    }
}