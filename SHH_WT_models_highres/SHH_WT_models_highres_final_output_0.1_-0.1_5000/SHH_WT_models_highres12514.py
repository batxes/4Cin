import _surface
import chimera
try:
  import chimera.runCommand
except:
  pass
from VolumePath import markerset as ms
try:
  from VolumePath import Marker_Set, Link
  new_marker_set=Marker_Set
except:
  from VolumePath import volume_path_dialog
  d= volume_path_dialog(True)
  new_marker_set= d.new_marker_set
marker_sets={}
surf_sets={}
if "particle_0 geometry" not in marker_sets:
  s=new_marker_set('particle_0 geometry')
  marker_sets["particle_0 geometry"]=s
s= marker_sets["particle_0 geometry"]
mark=s.place_marker((3438.54, 4941.62, 4411.31), (0.7, 0.7, 0.7), 182.271)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((3895.89, 4980.9, 4357.98), (0.7, 0.7, 0.7), 258.199)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((4085.76, 4655.52, 4111.93), (0.7, 0.7, 0.7), 123.897)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((4526.51, 4736.49, 4090.27), (0.7, 0.7, 0.7), 146.739)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((5033.36, 4711.14, 4040.98), (0.7, 0.7, 0.7), 179.098)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((4816.59, 4226.95, 3821.86), (0.7, 0.7, 0.7), 148.854)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((4688.16, 3754.15, 3637.12), (0.7, 0.7, 0.7), 196.357)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((5178.32, 3915.85, 3747.52), (0.7, 0.7, 0.7), 166.873)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((5670.63, 4044.49, 3833.04), (0.7, 0.7, 0.7), 95.4711)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((5435.03, 3686.86, 3761.5), (0.7, 0.7, 0.7), 185.401)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((5072.26, 3374.53, 3760.46), (0.7, 0.7, 0.7), 151.984)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((4535.05, 3079.02, 3834.72), (0.7, 0.7, 0.7), 185.612)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((4389.76, 2660.36, 4097.84), (0.7, 0.7, 0.7), 210.273)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((4280.03, 2268.59, 4255.5), (0.7, 0.7, 0.7), 106.892)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((4243.4, 1880.29, 4531.51), (0.7, 0.7, 0.7), 202.025)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((3999.34, 1651.74, 4990.62), (0.7, 0.7, 0.7), 192.169)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((3737.42, 1568.27, 5471.62), (0.7, 0.7, 0.7), 241.11)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((3693.58, 1880.08, 5734.28), (0.7, 0.7, 0.7), 128.465)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((3672.44, 2182.96, 6116.85), (0.7, 0.7, 0.7), 217.38)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((3747.28, 2442.37, 6782.25), (0.7, 0.7, 0.7), 184.555)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((3544.06, 2342.28, 6162.33), (0.7, 0.7, 0.7), 140.055)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((3495.23, 1984.69, 5821.98), (0.7, 0.7, 0.7), 169.708)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((3402.3, 1551.16, 5699.1), (0.7, 0.7, 0.7), 184.639)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((3127.2, 1515.58, 5508.2), (0.7, 0.7, 0.7), 119.286)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((2981.97, 1724.1, 5681.92), (0.7, 0.7, 0.7), 147.754)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((3130.01, 2040.02, 5742.11), (0.7, 0.7, 0.7), 171.4)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((3408.11, 2151, 5431.77), (0.7, 0.7, 0.7), 156.341)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((3363.19, 2468.38, 4934.06), (0.7, 0.7, 0.7), 186.501)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((3263.25, 2684.1, 4436.71), (0.7, 0.7, 0.7), 308.325)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((3494.27, 2787.05, 4073.26), (0.7, 0.7, 0.7), 138.617)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((3615.78, 2678.35, 3818.68), (0.7, 0.7, 0.7), 130.03)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((3568.15, 2563.34, 4107.73), (0.7, 0.7, 0.7), 156.552)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((3463.28, 2842.46, 4197.27), (0.7, 0.7, 0.7), 183.244)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((3346.81, 3068.64, 4300.24), (0.7, 0.7, 0.7), 181.382)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((3159.01, 3096.33, 4374.26), (0.7, 0.7, 0.7), 101.943)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((3034.64, 3219.09, 4697.75), (1, 0.7, 0), 138.913)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((2017.03, 2976.76, 4421.71), (0.7, 0.7, 0.7), 221.737)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((1426.07, 2813.62, 3818.24), (0.7, 0.7, 0.7), 256.38)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((1155.64, 3046.8, 3203.32), (0.7, 0.7, 0.7), 221.694)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((1512.73, 3321.27, 2656.77), (0.7, 0.7, 0.7), 259.341)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((2187.21, 2999.89, 2741.44), (0.7, 0.7, 0.7), 117.89)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((2791.61, 2712.01, 3194.43), (0.7, 0.7, 0.7), 116.071)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((3034.19, 2851.25, 3592.84), (0.7, 0.7, 0.7), 268.224)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((2906.32, 3102.17, 3451.85), (0.7, 0.7, 0.7), 386.918)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((2578.4, 3308.14, 2945.63), (0.7, 0.7, 0.7), 121.316)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((2571.05, 3697.87, 2711.88), (0.7, 0.7, 0.7), 138.363)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((2810.05, 3680.94, 3369.14), (1, 0.7, 0), 175.207)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((2580.98, 4195.31, 2937.66), (0.7, 0.7, 0.7), 131.468)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((2156.09, 4748.26, 2685.88), (0.7, 0.7, 0.7), 287.894)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((1986.32, 4245.8, 2736.05), (0.7, 0.7, 0.7), 88.1109)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((2238.45, 3687.45, 2890.76), (0.7, 0.7, 0.7), 145.385)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((2277.35, 3475.74, 2853.69), (0.7, 0.7, 0.7), 155.452)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((1887.93, 3839.91, 2495.48), (0.7, 0.7, 0.7), 145.512)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((1621.43, 4088.13, 2149.38), (0.7, 0.7, 0.7), 99.9972)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((1387.1, 4201.52, 1786.81), (0.7, 0.7, 0.7), 327.529)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((1808.87, 3729.92, 1673.55), (0.7, 0.7, 0.7), 137.983)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((1989.12, 3355, 1968.51), (0.7, 0.7, 0.7), 83.3733)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((2189.6, 3019.18, 2383.92), (0.7, 0.7, 0.7), 101.562)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((2417.65, 2835.61, 2818.6), (0.7, 0.7, 0.7), 165.689)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((2263.78, 3018.51, 2987.09), (0.7, 0.7, 0.7), 136.925)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((2158.1, 3103.84, 3048.45), (0.7, 0.7, 0.7), 123.389)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((1912.5, 3101.9, 2676.96), (0.7, 0.7, 0.7), 184.47)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((1371.67, 3074.33, 2081.95), (0.7, 0.7, 0.7), 148.473)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((658.465, 3074.62, 1406.63), (0.7, 0.7, 0.7), 241.406)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((1319.45, 3144.34, 1433.3), (0.7, 0.7, 0.7), 182.736)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((1727.45, 3274.19, 1615.85), (0.7, 0.7, 0.7), 166.62)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((1725.44, 3187.39, 1881.86), (0.7, 0.7, 0.7), 113.872)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((1882.61, 3266.86, 2157.84), (0.7, 0.7, 0.7), 110.065)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((1952.68, 3513.1, 2466.43), (0.7, 0.7, 0.7), 150.08)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((1954.94, 3875.89, 2804.31), (0.7, 0.7, 0.7), 118.525)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((1739.65, 4229.41, 3166.15), (0.7, 0.7, 0.7), 163.955)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((1358.26, 4341.06, 3164.42), (0.7, 0.7, 0.7), 170.131)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((1109.38, 4076.31, 2519.07), (0.7, 0.7, 0.7), 78.2127)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((964.613, 3785.59, 1765.33), (0.7, 0.7, 0.7), 251.896)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((1060.54, 3555.15, 1130.27), (0.7, 0.7, 0.7), 167.55)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((1300.59, 3372.47, 836.2), (0.7, 0.7, 0.7), 167.846)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((890.307, 3106.51, 933.247), (0.7, 0.7, 0.7), 259.68)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((589.825, 3292.55, 1226.54), (0.7, 0.7, 0.7), 80.2854)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((488.359, 3434.95, 1119.74), (0.7, 0.7, 0.7), 82.4427)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((205.29, 3281.96, 943.927), (0.7, 0.7, 0.7), 212.811)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((373.778, 2585.85, 1135.64), (0.7, 0.7, 0.7), 176.391)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((899.542, 2316.15, 1544.42), (0.7, 0.7, 0.7), 99.3204)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((1206.46, 2368.01, 2056.55), (0.7, 0.7, 0.7), 166.62)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((1190.3, 2298.52, 2360.42), (0.7, 0.7, 0.7), 102.831)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((560.294, 2172.09, 1762.92), (0.7, 0.7, 0.7), 65.0997)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((852.064, 2589.89, 1509.25), (0.7, 0.7, 0.7), 92.1294)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((1347.58, 2944.57, 1530.91), (0.7, 0.7, 0.7), 194.791)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((1747.74, 3158.8, 1438.95), (0.7, 0.7, 0.7), 120.766)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((1607.44, 3158.42, 884.216), (0.7, 0.7, 0.7), 217.803)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((1361.87, 3368.13, 1084.14), (0.7, 0.7, 0.7), 115.775)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((1327.3, 3607.85, 1422.5), (0.7, 0.7, 0.7), 115.648)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((1574.71, 3488.4, 1614.65), (0.7, 0.7, 0.7), 83.8386)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((1876.07, 3444.07, 1418.93), (0.7, 0.7, 0.7), 124.32)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((2261.13, 3528.72, 1283.49), (0.7, 0.7, 0.7), 185.993)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((2414.65, 4042.91, 1036.93), (0.7, 0.7, 0.7), 238.826)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((2180.5, 4525.29, 951.897), (0.7, 0.7, 0.7), 128.465)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((1745.24, 4367.63, 1377.68), (0.7, 0.7, 0.7), 203.209)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((1662.27, 3899.24, 1562.97), (0.7, 0.7, 0.7), 160.486)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((1756.11, 3689.44, 1308.17), (0.7, 0.7, 0.7), 149.277)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((1438.91, 3918.32, 938.546), (0.7, 0.7, 0.7), 35.7435)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((1460.78, 3513.67, 1843.29), (0.7, 0.7, 0.7), 98.3898)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((1696.76, 2971.77, 2705.18), (0.7, 0.7, 0.7), 188.404)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((2016.87, 2592.58, 2820.67), (0.7, 0.7, 0.7), 110.318)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((1841.4, 2606.14, 2477.37), (0.7, 0.7, 0.7), 127.534)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((1668.89, 2771.95, 2185.92), (0.7, 0.7, 0.7), 91.368)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((1552.92, 3016.54, 1916.29), (0.7, 0.7, 0.7), 131.045)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((1582.83, 3388.2, 1769.52), (0.7, 0.7, 0.7), 143.608)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((1816.99, 3467.37, 1498.06), (0.7, 0.7, 0.7), 135.783)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((2031.13, 3487.25, 1258.55), (0.7, 0.7, 0.7), 92.5947)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((2084.95, 3205.28, 1301.9), (0.7, 0.7, 0.7), 150.123)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((2029.18, 2937.95, 1378.52), (0.7, 0.7, 0.7), 121.57)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((2063.2, 2784.95, 1085.16), (0.7, 0.7, 0.7), 104.777)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((2239.7, 2550.17, 1392.25), (0.7, 0.7, 0.7), 114.844)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((2453.15, 2313.78, 1717.56), (0.7, 0.7, 0.7), 150.588)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((2270.1, 2347.52, 2088.86), (0.7, 0.7, 0.7), 103.55)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((1778.82, 2240.62, 2335.76), (0.7, 0.7, 0.7), 215.392)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((1370.28, 2015.1, 2676.22), (0.7, 0.7, 0.7), 99.9126)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((801.028, 1685.5, 2597.83), (0.7, 0.7, 0.7), 99.7857)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((303.281, 1625.84, 2402.7), (0.7, 0.7, 0.7), 109.98)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((778.125, 1683.18, 2223.83), (0.7, 0.7, 0.7), 102.831)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((1104.09, 1918.23, 2163.92), (0.7, 0.7, 0.7), 103.593)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((1395.54, 2255.73, 1982.95), (0.7, 0.7, 0.7), 173.472)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((1325.74, 2664.56, 1614.38), (0.7, 0.7, 0.7), 113.575)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((1618.38, 3014.15, 1447.66), (0.7, 0.7, 0.7), 128.296)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((1859.12, 3273.5, 1213.21), (0.7, 0.7, 0.7), 145.004)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((2279.12, 3493.89, 1081.59), (0.7, 0.7, 0.7), 148.261)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((2498.78, 3914.15, 691.335), (0.7, 0.7, 0.7), 127.704)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((2535.42, 4395.93, 389.636), (0.7, 0.7, 0.7), 129.607)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((2065.16, 4272.05, 600.462), (0.7, 0.7, 0.7), 139.759)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((1633.16, 3975.18, 1090.54), (0.7, 0.7, 0.7), 118.567)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((1402.72, 3587.54, 1173.82), (0.7, 0.7, 0.7), 136.164)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((1388.84, 3173.01, 1318.49), (0.7, 0.7, 0.7), 121.655)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((1535.67, 2795.17, 1293.88), (0.7, 0.7, 0.7), 127.492)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((1527.53, 2494.89, 1007.09), (0.7, 0.7, 0.7), 138.617)
if "particle_134 geometry" not in marker_sets:
  s=new_marker_set('particle_134 geometry')
  marker_sets["particle_134 geometry"]=s
s= marker_sets["particle_134 geometry"]
mark=s.place_marker((1687.34, 2178, 1102.2), (0.7, 0.7, 0.7), 120.766)
if "particle_135 geometry" not in marker_sets:
  s=new_marker_set('particle_135 geometry')
  marker_sets["particle_135 geometry"]=s
s= marker_sets["particle_135 geometry"]
mark=s.place_marker((1597.13, 2059.11, 1401.22), (0.7, 0.7, 0.7), 145.893)
if "particle_136 geometry" not in marker_sets:
  s=new_marker_set('particle_136 geometry')
  marker_sets["particle_136 geometry"]=s
s= marker_sets["particle_136 geometry"]
mark=s.place_marker((1667.85, 2329.48, 1799.99), (0.7, 0.7, 0.7), 185.02)
if "particle_137 geometry" not in marker_sets:
  s=new_marker_set('particle_137 geometry')
  marker_sets["particle_137 geometry"]=s
s= marker_sets["particle_137 geometry"]
mark=s.place_marker((1904.67, 2473.8, 2249.32), (0.7, 0.7, 0.7), 221.314)
if "particle_138 geometry" not in marker_sets:
  s=new_marker_set('particle_138 geometry')
  marker_sets["particle_138 geometry"]=s
s= marker_sets["particle_138 geometry"]
mark=s.place_marker((2308.55, 2521.02, 2512.22), (0.7, 0.7, 0.7), 165.139)
if "particle_139 geometry" not in marker_sets:
  s=new_marker_set('particle_139 geometry')
  marker_sets["particle_139 geometry"]=s
s= marker_sets["particle_139 geometry"]
mark=s.place_marker((2121.66, 2676.65, 2621.64), (0.7, 0.7, 0.7), 179.437)
if "particle_140 geometry" not in marker_sets:
  s=new_marker_set('particle_140 geometry')
  marker_sets["particle_140 geometry"]=s
s= marker_sets["particle_140 geometry"]
mark=s.place_marker((1729.71, 2607.12, 2584.37), (0.7, 0.7, 0.7), 137.898)
if "particle_141 geometry" not in marker_sets:
  s=new_marker_set('particle_141 geometry')
  marker_sets["particle_141 geometry"]=s
s= marker_sets["particle_141 geometry"]
mark=s.place_marker((1528.74, 2564.18, 2335.56), (0.7, 0.7, 0.7), 124.658)
if "particle_142 geometry" not in marker_sets:
  s=new_marker_set('particle_142 geometry')
  marker_sets["particle_142 geometry"]=s
s= marker_sets["particle_142 geometry"]
mark=s.place_marker((1523.64, 2438.91, 1991.93), (0.7, 0.7, 0.7), 97.7553)
if "particle_143 geometry" not in marker_sets:
  s=new_marker_set('particle_143 geometry')
  marker_sets["particle_143 geometry"]=s
s= marker_sets["particle_143 geometry"]
mark=s.place_marker((1472.76, 2347.82, 1688.22), (0.7, 0.7, 0.7), 92.9331)
if "particle_144 geometry" not in marker_sets:
  s=new_marker_set('particle_144 geometry')
  marker_sets["particle_144 geometry"]=s
s= marker_sets["particle_144 geometry"]
mark=s.place_marker((1320.84, 2376.77, 1380.19), (0.7, 0.7, 0.7), 123.135)
if "particle_145 geometry" not in marker_sets:
  s=new_marker_set('particle_145 geometry')
  marker_sets["particle_145 geometry"]=s
s= marker_sets["particle_145 geometry"]
mark=s.place_marker((1472.92, 2452.52, 1731.75), (0.7, 0.7, 0.7), 125.716)
if "particle_146 geometry" not in marker_sets:
  s=new_marker_set('particle_146 geometry')
  marker_sets["particle_146 geometry"]=s
s= marker_sets["particle_146 geometry"]
mark=s.place_marker((1730.08, 2515.38, 1887.84), (0.7, 0.7, 0.7), 127.534)
if "particle_147 geometry" not in marker_sets:
  s=new_marker_set('particle_147 geometry')
  marker_sets["particle_147 geometry"]=s
s= marker_sets["particle_147 geometry"]
mark=s.place_marker((1845.03, 2753.31, 1747.09), (0.7, 0.7, 0.7), 94.9212)
if "particle_148 geometry" not in marker_sets:
  s=new_marker_set('particle_148 geometry')
  marker_sets["particle_148 geometry"]=s
s= marker_sets["particle_148 geometry"]
mark=s.place_marker((2104.51, 2891, 2072), (0.7, 0.7, 0.7), 137.644)
if "particle_149 geometry" not in marker_sets:
  s=new_marker_set('particle_149 geometry')
  marker_sets["particle_149 geometry"]=s
s= marker_sets["particle_149 geometry"]
mark=s.place_marker((2417.52, 2970.13, 2220.89), (0.7, 0.7, 0.7), 149.277)
if "particle_150 geometry" not in marker_sets:
  s=new_marker_set('particle_150 geometry')
  marker_sets["particle_150 geometry"]=s
s= marker_sets["particle_150 geometry"]
mark=s.place_marker((2541.28, 2709.71, 2012.31), (0.7, 0.7, 0.7), 103.677)
if "particle_151 geometry" not in marker_sets:
  s=new_marker_set('particle_151 geometry')
  marker_sets["particle_151 geometry"]=s
s= marker_sets["particle_151 geometry"]
mark=s.place_marker((2564.45, 2516.81, 1582.98), (0.7, 0.7, 0.7), 99.6588)
if "particle_152 geometry" not in marker_sets:
  s=new_marker_set('particle_152 geometry')
  marker_sets["particle_152 geometry"]=s
s= marker_sets["particle_152 geometry"]
mark=s.place_marker((2569.47, 2379.52, 1245.57), (0.7, 0.7, 0.7), 134.133)
if "particle_153 geometry" not in marker_sets:
  s=new_marker_set('particle_153 geometry')
  marker_sets["particle_153 geometry"]=s
s= marker_sets["particle_153 geometry"]
mark=s.place_marker((2335.85, 2287.75, 1499.22), (0.7, 0.7, 0.7), 173.007)
if "particle_154 geometry" not in marker_sets:
  s=new_marker_set('particle_154 geometry')
  marker_sets["particle_154 geometry"]=s
s= marker_sets["particle_154 geometry"]
mark=s.place_marker((2370.12, 2422.51, 2055.53), (0.7, 0.7, 0.7), 141.028)
if "particle_155 geometry" not in marker_sets:
  s=new_marker_set('particle_155 geometry')
  marker_sets["particle_155 geometry"]=s
s= marker_sets["particle_155 geometry"]
mark=s.place_marker((2351.37, 2590.86, 2488.93), (0.7, 0.7, 0.7), 161.121)
if "particle_156 geometry" not in marker_sets:
  s=new_marker_set('particle_156 geometry')
  marker_sets["particle_156 geometry"]=s
s= marker_sets["particle_156 geometry"]
mark=s.place_marker((2365.93, 2918.83, 2425.6), (0.7, 0.7, 0.7), 119.582)
if "particle_157 geometry" not in marker_sets:
  s=new_marker_set('particle_157 geometry')
  marker_sets["particle_157 geometry"]=s
s= marker_sets["particle_157 geometry"]
mark=s.place_marker((2221.07, 3003.47, 2041.14), (0.7, 0.7, 0.7), 137.094)
if "particle_158 geometry" not in marker_sets:
  s=new_marker_set('particle_158 geometry')
  marker_sets["particle_158 geometry"]=s
s= marker_sets["particle_158 geometry"]
mark=s.place_marker((1877.87, 3012.13, 1677.71), (0.7, 0.7, 0.7), 149.234)
if "particle_159 geometry" not in marker_sets:
  s=new_marker_set('particle_159 geometry')
  marker_sets["particle_159 geometry"]=s
s= marker_sets["particle_159 geometry"]
mark=s.place_marker((1560.48, 2823.54, 1974.67), (0.7, 0.7, 0.7), 151.011)
if "particle_160 geometry" not in marker_sets:
  s=new_marker_set('particle_160 geometry')
  marker_sets["particle_160 geometry"]=s
s= marker_sets["particle_160 geometry"]
mark=s.place_marker((1584.59, 2557.87, 2476.13), (0.7, 0.7, 0.7), 184.216)
if "particle_161 geometry" not in marker_sets:
  s=new_marker_set('particle_161 geometry')
  marker_sets["particle_161 geometry"]=s
s= marker_sets["particle_161 geometry"]
mark=s.place_marker((1780.06, 2205.16, 2410.29), (0.7, 0.7, 0.7), 170.596)
if "particle_162 geometry" not in marker_sets:
  s=new_marker_set('particle_162 geometry')
  marker_sets["particle_162 geometry"]=s
s= marker_sets["particle_162 geometry"]
mark=s.place_marker((1486.08, 2135.09, 1835.97), (0.7, 0.7, 0.7), 215.603)
if "particle_163 geometry" not in marker_sets:
  s=new_marker_set('particle_163 geometry')
  marker_sets["particle_163 geometry"]=s
s= marker_sets["particle_163 geometry"]
mark=s.place_marker((1024.22, 2067.86, 1058.31), (0.7, 0.7, 0.7), 79.0164)
if "particle_164 geometry" not in marker_sets:
  s=new_marker_set('particle_164 geometry')
  marker_sets["particle_164 geometry"]=s
s= marker_sets["particle_164 geometry"]
mark=s.place_marker((1251.36, 1959.26, 828.259), (0.7, 0.7, 0.7), 77.2821)
if "particle_165 geometry" not in marker_sets:
  s=new_marker_set('particle_165 geometry')
  marker_sets["particle_165 geometry"]=s
s= marker_sets["particle_165 geometry"]
mark=s.place_marker((1587.75, 2024.58, 899.213), (0.7, 0.7, 0.7), 188.658)
if "particle_166 geometry" not in marker_sets:
  s=new_marker_set('particle_166 geometry')
  marker_sets["particle_166 geometry"]=s
s= marker_sets["particle_166 geometry"]
mark=s.place_marker((1687.27, 1734.22, 973.238), (0.7, 0.7, 0.7), 115.437)
if "particle_167 geometry" not in marker_sets:
  s=new_marker_set('particle_167 geometry')
  marker_sets["particle_167 geometry"]=s
s= marker_sets["particle_167 geometry"]
mark=s.place_marker((1806.37, 2064.18, 1495.56), (0.7, 0.7, 0.7), 88.4916)
if "particle_168 geometry" not in marker_sets:
  s=new_marker_set('particle_168 geometry')
  marker_sets["particle_168 geometry"]=s
s= marker_sets["particle_168 geometry"]
mark=s.place_marker((1990.8, 2324.01, 2023.13), (0.7, 0.7, 0.7), 108.88)
if "particle_169 geometry" not in marker_sets:
  s=new_marker_set('particle_169 geometry')
  marker_sets["particle_169 geometry"]=s
s= marker_sets["particle_169 geometry"]
mark=s.place_marker((1876.33, 2478.03, 2322.52), (0.7, 0.7, 0.7), 172.119)
if "particle_170 geometry" not in marker_sets:
  s=new_marker_set('particle_170 geometry')
  marker_sets["particle_170 geometry"]=s
s= marker_sets["particle_170 geometry"]
mark=s.place_marker((1568.35, 2286.88, 1991.72), (0.7, 0.7, 0.7), 139.505)
if "particle_171 geometry" not in marker_sets:
  s=new_marker_set('particle_171 geometry')
  marker_sets["particle_171 geometry"]=s
s= marker_sets["particle_171 geometry"]
mark=s.place_marker((1253.23, 2093.42, 1647.02), (0.7, 0.7, 0.7), 92.7639)
if "particle_172 geometry" not in marker_sets:
  s=new_marker_set('particle_172 geometry')
  marker_sets["particle_172 geometry"]=s
s= marker_sets["particle_172 geometry"]
mark=s.place_marker((1088.85, 2128.5, 1850.48), (0.7, 0.7, 0.7), 89.8452)
if "particle_173 geometry" not in marker_sets:
  s=new_marker_set('particle_173 geometry')
  marker_sets["particle_173 geometry"]=s
s= marker_sets["particle_173 geometry"]
mark=s.place_marker((1224.45, 1936.99, 2039.73), (0.7, 0.7, 0.7), 149.446)
if "particle_174 geometry" not in marker_sets:
  s=new_marker_set('particle_174 geometry')
  marker_sets["particle_174 geometry"]=s
s= marker_sets["particle_174 geometry"]
mark=s.place_marker((1263.22, 1623.45, 1939.68), (0.7, 0.7, 0.7), 126.858)
if "particle_175 geometry" not in marker_sets:
  s=new_marker_set('particle_175 geometry')
  marker_sets["particle_175 geometry"]=s
s= marker_sets["particle_175 geometry"]
mark=s.place_marker((1067.08, 1735.63, 1694.62), (0.7, 0.7, 0.7), 106.046)
if "particle_176 geometry" not in marker_sets:
  s=new_marker_set('particle_176 geometry')
  marker_sets["particle_176 geometry"]=s
s= marker_sets["particle_176 geometry"]
mark=s.place_marker((825.055, 2185.47, 1630.66), (0.7, 0.7, 0.7), 156.298)
if "particle_177 geometry" not in marker_sets:
  s=new_marker_set('particle_177 geometry')
  marker_sets["particle_177 geometry"]=s
s= marker_sets["particle_177 geometry"]
mark=s.place_marker((619.019, 2752.19, 1514.08), (0.7, 0.7, 0.7), 231.212)
if "particle_178 geometry" not in marker_sets:
  s=new_marker_set('particle_178 geometry')
  marker_sets["particle_178 geometry"]=s
s= marker_sets["particle_178 geometry"]
mark=s.place_marker((635.3, 3128.69, 1917.57), (0.7, 0.7, 0.7), 88.4916)
if "particle_179 geometry" not in marker_sets:
  s=new_marker_set('particle_179 geometry')
  marker_sets["particle_179 geometry"]=s
s= marker_sets["particle_179 geometry"]
mark=s.place_marker((898.616, 3120.24, 2323.68), (0.7, 0.7, 0.7), 111.334)
if "particle_180 geometry" not in marker_sets:
  s=new_marker_set('particle_180 geometry')
  marker_sets["particle_180 geometry"]=s
s= marker_sets["particle_180 geometry"]
mark=s.place_marker((1390.63, 2858.81, 2568.06), (0.7, 0.7, 0.7), 127.619)
if "particle_181 geometry" not in marker_sets:
  s=new_marker_set('particle_181 geometry')
  marker_sets["particle_181 geometry"]=s
s= marker_sets["particle_181 geometry"]
mark=s.place_marker((1817.14, 2696.12, 2653.86), (0.7, 0.7, 0.7), 230.746)
if "particle_182 geometry" not in marker_sets:
  s=new_marker_set('particle_182 geometry')
  marker_sets["particle_182 geometry"]=s
s= marker_sets["particle_182 geometry"]
mark=s.place_marker((1660.39, 2799.44, 2282.8), (0.7, 0.7, 0.7), 124.573)
if "particle_183 geometry" not in marker_sets:
  s=new_marker_set('particle_183 geometry')
  marker_sets["particle_183 geometry"]=s
s= marker_sets["particle_183 geometry"]
mark=s.place_marker((1248.38, 2672.87, 1782.81), (0.7, 0.7, 0.7), 124.489)
if "particle_184 geometry" not in marker_sets:
  s=new_marker_set('particle_184 geometry')
  marker_sets["particle_184 geometry"]=s
s= marker_sets["particle_184 geometry"]
mark=s.place_marker((1304.56, 2432.17, 1462.58), (0.7, 0.7, 0.7), 196.61)
if "particle_185 geometry" not in marker_sets:
  s=new_marker_set('particle_185 geometry')
  marker_sets["particle_185 geometry"]=s
s= marker_sets["particle_185 geometry"]
mark=s.place_marker((1308.89, 2257.03, 1749.48), (0.7, 0.7, 0.7), 134.049)
if "particle_186 geometry" not in marker_sets:
  s=new_marker_set('particle_186 geometry')
  marker_sets["particle_186 geometry"]=s
s= marker_sets["particle_186 geometry"]
mark=s.place_marker((986.353, 2292.64, 1971.56), (0.7, 0.7, 0.7), 141.493)
if "particle_187 geometry" not in marker_sets:
  s=new_marker_set('particle_187 geometry')
  marker_sets["particle_187 geometry"]=s
s= marker_sets["particle_187 geometry"]
mark=s.place_marker((565.547, 2254.19, 1995.63), (0.7, 0.7, 0.7), 172.203)
if "particle_188 geometry" not in marker_sets:
  s=new_marker_set('particle_188 geometry')
  marker_sets["particle_188 geometry"]=s
s= marker_sets["particle_188 geometry"]
mark=s.place_marker((1136.39, 2042.48, 1816.4), (0.7, 0.7, 0.7), 271.354)
if "particle_189 geometry" not in marker_sets:
  s=new_marker_set('particle_189 geometry')
  marker_sets["particle_189 geometry"]=s
s= marker_sets["particle_189 geometry"]
mark=s.place_marker((1560.32, 2170.8, 1563.69), (0.7, 0.7, 0.7), 97.0785)
if "particle_190 geometry" not in marker_sets:
  s=new_marker_set('particle_190 geometry')
  marker_sets["particle_190 geometry"]=s
s= marker_sets["particle_190 geometry"]
mark=s.place_marker((1760.7, 2417.89, 1298.19), (0.7, 0.7, 0.7), 151.857)
if "particle_191 geometry" not in marker_sets:
  s=new_marker_set('particle_191 geometry')
  marker_sets["particle_191 geometry"]=s
s= marker_sets["particle_191 geometry"]
mark=s.place_marker((2229.31, 2576.2, 987.792), (0.7, 0.7, 0.7), 199.233)
if "particle_192 geometry" not in marker_sets:
  s=new_marker_set('particle_192 geometry')
  marker_sets["particle_192 geometry"]=s
s= marker_sets["particle_192 geometry"]
mark=s.place_marker((2733.17, 2679.74, 1290.69), (0.7, 0.7, 0.7), 118.863)
if "particle_193 geometry" not in marker_sets:
  s=new_marker_set('particle_193 geometry')
  marker_sets["particle_193 geometry"]=s
s= marker_sets["particle_193 geometry"]
mark=s.place_marker((3078.41, 2959.27, 1231.85), (0.7, 0.7, 0.7), 172.415)
if "particle_194 geometry" not in marker_sets:
  s=new_marker_set('particle_194 geometry')
  marker_sets["particle_194 geometry"]=s
s= marker_sets["particle_194 geometry"]
mark=s.place_marker((3270.38, 3254.36, 860.296), (0.7, 0.7, 0.7), 134.26)
if "particle_195 geometry" not in marker_sets:
  s=new_marker_set('particle_195 geometry')
  marker_sets["particle_195 geometry"]=s
s= marker_sets["particle_195 geometry"]
mark=s.place_marker((3437.96, 3609, 5.53671), (0.7, 0.7, 0.7), 139.548)
if "particle_196 geometry" not in marker_sets:
  s=new_marker_set('particle_196 geometry')
  marker_sets["particle_196 geometry"]=s
s= marker_sets["particle_196 geometry"]
mark=s.place_marker((2964.4, 3854.82, 77.5514), (0.7, 0.7, 0.7), 196.526)
if "particle_197 geometry" not in marker_sets:
  s=new_marker_set('particle_197 geometry')
  marker_sets["particle_197 geometry"]=s
s= marker_sets["particle_197 geometry"]
mark=s.place_marker((2426.92, 3700.78, 606.478), (0.7, 0.7, 0.7), 136.206)
if "particle_198 geometry" not in marker_sets:
  s=new_marker_set('particle_198 geometry')
  marker_sets["particle_198 geometry"]=s
s= marker_sets["particle_198 geometry"]
mark=s.place_marker((2217.26, 3489.33, 1516.6), (0.7, 0.7, 0.7), 152.322)
if "particle_199 geometry" not in marker_sets:
  s=new_marker_set('particle_199 geometry')
  marker_sets["particle_199 geometry"]=s
s= marker_sets["particle_199 geometry"]
mark=s.place_marker((2153.67, 3182.36, 2094.07), (0.7, 0.7, 0.7), 126.054)
if "particle_200 geometry" not in marker_sets:
  s=new_marker_set('particle_200 geometry')
  marker_sets["particle_200 geometry"]=s
s= marker_sets["particle_200 geometry"]
mark=s.place_marker((1826.86, 2991.31, 1952.07), (0.7, 0.7, 0.7), 164.378)
if "particle_201 geometry" not in marker_sets:
  s=new_marker_set('particle_201 geometry')
  marker_sets["particle_201 geometry"]=s
s= marker_sets["particle_201 geometry"]
mark=s.place_marker((1690.34, 2760.77, 1612.54), (0.7, 0.7, 0.7), 122.205)
if "particle_202 geometry" not in marker_sets:
  s=new_marker_set('particle_202 geometry')
  marker_sets["particle_202 geometry"]=s
s= marker_sets["particle_202 geometry"]
mark=s.place_marker((1719.71, 2438.67, 1321.54), (0.7, 0.7, 0.7), 134.979)
if "particle_203 geometry" not in marker_sets:
  s=new_marker_set('particle_203 geometry')
  marker_sets["particle_203 geometry"]=s
s= marker_sets["particle_203 geometry"]
mark=s.place_marker((2066.8, 2333, 1403.59), (0.7, 0.7, 0.7), 136.375)
if "particle_204 geometry" not in marker_sets:
  s=new_marker_set('particle_204 geometry')
  marker_sets["particle_204 geometry"]=s
s= marker_sets["particle_204 geometry"]
mark=s.place_marker((2165.26, 2495.21, 1345.54), (0.7, 0.7, 0.7), 151.688)
if "particle_205 geometry" not in marker_sets:
  s=new_marker_set('particle_205 geometry')
  marker_sets["particle_205 geometry"]=s
s= marker_sets["particle_205 geometry"]
mark=s.place_marker((1930.64, 2364.69, 1283.87), (0.7, 0.7, 0.7), 116.156)
if "particle_206 geometry" not in marker_sets:
  s=new_marker_set('particle_206 geometry')
  marker_sets["particle_206 geometry"]=s
s= marker_sets["particle_206 geometry"]
mark=s.place_marker((2203.64, 2457.93, 1941.47), (0.7, 0.7, 0.7), 122.839)
if "particle_207 geometry" not in marker_sets:
  s=new_marker_set('particle_207 geometry')
  marker_sets["particle_207 geometry"]=s
s= marker_sets["particle_207 geometry"]
mark=s.place_marker((2286, 2773.51, 2323.28), (0.7, 0.7, 0.7), 164.716)
if "particle_208 geometry" not in marker_sets:
  s=new_marker_set('particle_208 geometry')
  marker_sets["particle_208 geometry"]=s
s= marker_sets["particle_208 geometry"]
mark=s.place_marker((1915.64, 3168.32, 1633.09), (0.7, 0.7, 0.7), 303.672)
if "particle_209 geometry" not in marker_sets:
  s=new_marker_set('particle_209 geometry')
  marker_sets["particle_209 geometry"]=s
s= marker_sets["particle_209 geometry"]
mark=s.place_marker((1654.31, 3156.47, 637.097), (0.7, 0.7, 0.7), 220.298)
if "particle_210 geometry" not in marker_sets:
  s=new_marker_set('particle_210 geometry')
  marker_sets["particle_210 geometry"]=s
s= marker_sets["particle_210 geometry"]
mark=s.place_marker((1428.98, 2561.64, 750.801), (0.7, 0.7, 0.7), 175.883)
if "particle_211 geometry" not in marker_sets:
  s=new_marker_set('particle_211 geometry')
  marker_sets["particle_211 geometry"]=s
s= marker_sets["particle_211 geometry"]
mark=s.place_marker((982.247, 2194.93, 1129.52), (0.7, 0.7, 0.7), 233.581)
if "particle_212 geometry" not in marker_sets:
  s=new_marker_set('particle_212 geometry')
  marker_sets["particle_212 geometry"]=s
s= marker_sets["particle_212 geometry"]
mark=s.place_marker((611.497, 2376.13, 1788.49), (0.7, 0.7, 0.7), 231.127)
if "particle_213 geometry" not in marker_sets:
  s=new_marker_set('particle_213 geometry')
  marker_sets["particle_213 geometry"]=s
s= marker_sets["particle_213 geometry"]
mark=s.place_marker((376.148, 2046.82, 2244.99), (0.7, 0.7, 0.7), 247.413)
if "particle_214 geometry" not in marker_sets:
  s=new_marker_set('particle_214 geometry')
  marker_sets["particle_214 geometry"]=s
s= marker_sets["particle_214 geometry"]
mark=s.place_marker((315.978, 1422.18, 2385.32), (0.7, 0.7, 0.7), 200.206)
if "particle_215 geometry" not in marker_sets:
  s=new_marker_set('particle_215 geometry')
  marker_sets["particle_215 geometry"]=s
s= marker_sets["particle_215 geometry"]
mark=s.place_marker((524.886, 1140.28, 2113.88), (0.7, 0.7, 0.7), 150.419)
if "particle_216 geometry" not in marker_sets:
  s=new_marker_set('particle_216 geometry')
  marker_sets["particle_216 geometry"]=s
s= marker_sets["particle_216 geometry"]
mark=s.place_marker((885.592, 1469.97, 2473.9), (0.7, 0.7, 0.7), 140.14)
if "particle_217 geometry" not in marker_sets:
  s=new_marker_set('particle_217 geometry')
  marker_sets["particle_217 geometry"]=s
s= marker_sets["particle_217 geometry"]
mark=s.place_marker((896.706, 1703.67, 2865.74), (0.7, 0.7, 0.7), 132.949)
if "particle_218 geometry" not in marker_sets:
  s=new_marker_set('particle_218 geometry')
  marker_sets["particle_218 geometry"]=s
s= marker_sets["particle_218 geometry"]
mark=s.place_marker((1070.96, 1906.97, 3154.31), (0.7, 0.7, 0.7), 141.113)
if "particle_219 geometry" not in marker_sets:
  s=new_marker_set('particle_219 geometry')
  marker_sets["particle_219 geometry"]=s
s= marker_sets["particle_219 geometry"]
mark=s.place_marker((918.67, 2202.97, 3152.53), (0.7, 0.7, 0.7), 171.526)
if "particle_220 geometry" not in marker_sets:
  s=new_marker_set('particle_220 geometry')
  marker_sets["particle_220 geometry"]=s
s= marker_sets["particle_220 geometry"]
mark=s.place_marker((572.144, 2228.05, 2687.35), (0.7, 0.7, 0.7), 326.937)
if "particle_221 geometry" not in marker_sets:
  s=new_marker_set('particle_221 geometry')
  marker_sets["particle_221 geometry"]=s
s= marker_sets["particle_221 geometry"]
mark=s.place_marker((608.664, 2178.54, 2120.97), (0.7, 0.7, 0.7), 92.0871)
if "particle_222 geometry" not in marker_sets:
  s=new_marker_set('particle_222 geometry')
  marker_sets["particle_222 geometry"]=s
s= marker_sets["particle_222 geometry"]
mark=s.place_marker((908.289, 2493.49, 2100.31), (0.7, 0.7, 0.7), 210.273)
if "particle_223 geometry" not in marker_sets:
  s=new_marker_set('particle_223 geometry')
  marker_sets["particle_223 geometry"]=s
s= marker_sets["particle_223 geometry"]
mark=s.place_marker((1406.08, 2601.16, 2628.54), (0.7, 0.7, 0.7), 122.628)
if "particle_224 geometry" not in marker_sets:
  s=new_marker_set('particle_224 geometry')
  marker_sets["particle_224 geometry"]=s
s= marker_sets["particle_224 geometry"]
mark=s.place_marker((1524.67, 2639.5, 2849.44), (0.7, 0.7, 0.7), 109.176)
if "particle_225 geometry" not in marker_sets:
  s=new_marker_set('particle_225 geometry')
  marker_sets["particle_225 geometry"]=s
s= marker_sets["particle_225 geometry"]
mark=s.place_marker((1459.21, 2537.49, 2588.6), (0.7, 0.7, 0.7), 142.213)
if "particle_226 geometry" not in marker_sets:
  s=new_marker_set('particle_226 geometry')
  marker_sets["particle_226 geometry"]=s
s= marker_sets["particle_226 geometry"]
mark=s.place_marker((1428.98, 2776.51, 2247.99), (0.7, 0.7, 0.7), 250.078)
if "particle_227 geometry" not in marker_sets:
  s=new_marker_set('particle_227 geometry')
  marker_sets["particle_227 geometry"]=s
s= marker_sets["particle_227 geometry"]
mark=s.place_marker((1743.1, 2486.51, 2061.04), (0.7, 0.7, 0.7), 123.558)
if "particle_228 geometry" not in marker_sets:
  s=new_marker_set('particle_228 geometry')
  marker_sets["particle_228 geometry"]=s
s= marker_sets["particle_228 geometry"]
mark=s.place_marker((2134.3, 2254.81, 2215.27), (0.7, 0.7, 0.7), 235.992)
if "particle_229 geometry" not in marker_sets:
  s=new_marker_set('particle_229 geometry')
  marker_sets["particle_229 geometry"]=s
s= marker_sets["particle_229 geometry"]
mark=s.place_marker((2553.08, 2005.33, 2208.93), (0.7, 0.7, 0.7), 172.373)
if "particle_230 geometry" not in marker_sets:
  s=new_marker_set('particle_230 geometry')
  marker_sets["particle_230 geometry"]=s
s= marker_sets["particle_230 geometry"]
mark=s.place_marker((2645.41, 1808.29, 1808.08), (0.7, 0.7, 0.7), 152.322)
if "particle_231 geometry" not in marker_sets:
  s=new_marker_set('particle_231 geometry')
  marker_sets["particle_231 geometry"]=s
s= marker_sets["particle_231 geometry"]
mark=s.place_marker((2585.02, 1607.08, 1562.65), (0.7, 0.7, 0.7), 196.653)
if "particle_232 geometry" not in marker_sets:
  s=new_marker_set('particle_232 geometry')
  marker_sets["particle_232 geometry"]=s
s= marker_sets["particle_232 geometry"]
mark=s.place_marker((2571.46, 1461.43, 1880.05), (0.7, 0.7, 0.7), 134.091)
if "particle_233 geometry" not in marker_sets:
  s=new_marker_set('particle_233 geometry')
  marker_sets["particle_233 geometry"]=s
s= marker_sets["particle_233 geometry"]
mark=s.place_marker((2495.99, 1397.98, 2190.32), (0.7, 0.7, 0.7), 180.325)
if "particle_234 geometry" not in marker_sets:
  s=new_marker_set('particle_234 geometry')
  marker_sets["particle_234 geometry"]=s
s= marker_sets["particle_234 geometry"]
mark=s.place_marker((2433.75, 1851.2, 2129.78), (0.7, 0.7, 0.7), 218.437)
if "particle_235 geometry" not in marker_sets:
  s=new_marker_set('particle_235 geometry')
  marker_sets["particle_235 geometry"]=s
s= marker_sets["particle_235 geometry"]
mark=s.place_marker((2115.98, 2087.59, 1890.5), (0.7, 0.7, 0.7), 148.008)
if "particle_236 geometry" not in marker_sets:
  s=new_marker_set('particle_236 geometry')
  marker_sets["particle_236 geometry"]=s
s= marker_sets["particle_236 geometry"]
mark=s.place_marker((1639.94, 2008.39, 1476.93), (0.7, 0.7, 0.7), 191.873)
if "particle_237 geometry" not in marker_sets:
  s=new_marker_set('particle_237 geometry')
  marker_sets["particle_237 geometry"]=s
s= marker_sets["particle_237 geometry"]
mark=s.place_marker((1118.36, 1862.45, 1368.95), (0.7, 0.7, 0.7), 138.575)
if "particle_238 geometry" not in marker_sets:
  s=new_marker_set('particle_238 geometry')
  marker_sets["particle_238 geometry"]=s
s= marker_sets["particle_238 geometry"]
mark=s.place_marker((1007.35, 1478.07, 1215.03), (0.7, 0.7, 0.7), 161.205)
if "particle_239 geometry" not in marker_sets:
  s=new_marker_set('particle_239 geometry')
  marker_sets["particle_239 geometry"]=s
s= marker_sets["particle_239 geometry"]
mark=s.place_marker((1356.97, 1779.78, 1091.74), (0.7, 0.7, 0.7), 288.021)
if "particle_240 geometry" not in marker_sets:
  s=new_marker_set('particle_240 geometry')
  marker_sets["particle_240 geometry"]=s
s= marker_sets["particle_240 geometry"]
mark=s.place_marker((1931.91, 1576.63, 1478.75), (0.7, 0.7, 0.7), 227.405)
if "particle_241 geometry" not in marker_sets:
  s=new_marker_set('particle_241 geometry')
  marker_sets["particle_241 geometry"]=s
s= marker_sets["particle_241 geometry"]
mark=s.place_marker((2345.9, 1699.88, 1774.97), (0.7, 0.7, 0.7), 126.519)
if "particle_242 geometry" not in marker_sets:
  s=new_marker_set('particle_242 geometry')
  marker_sets["particle_242 geometry"]=s
s= marker_sets["particle_242 geometry"]
mark=s.place_marker((2372.98, 1744.7, 1467.79), (0.7, 0.7, 0.7), 117.975)
if "particle_243 geometry" not in marker_sets:
  s=new_marker_set('particle_243 geometry')
  marker_sets["particle_243 geometry"]=s
s= marker_sets["particle_243 geometry"]
mark=s.place_marker((2386.4, 2062.86, 1709.16), (0.7, 0.7, 0.7), 200.883)
if "particle_244 geometry" not in marker_sets:
  s=new_marker_set('particle_244 geometry')
  marker_sets["particle_244 geometry"]=s
s= marker_sets["particle_244 geometry"]
mark=s.place_marker((2367.69, 1945.75, 2075.68), (0.7, 0.7, 0.7), 158.794)
if "particle_245 geometry" not in marker_sets:
  s=new_marker_set('particle_245 geometry')
  marker_sets["particle_245 geometry"]=s
s= marker_sets["particle_245 geometry"]
mark=s.place_marker((2237.92, 1774.54, 2318.28), (0.7, 0.7, 0.7), 115.86)
if "particle_246 geometry" not in marker_sets:
  s=new_marker_set('particle_246 geometry')
  marker_sets["particle_246 geometry"]=s
s= marker_sets["particle_246 geometry"]
mark=s.place_marker((2308, 1855.07, 2536.88), (0.7, 0.7, 0.7), 133.034)
if "particle_247 geometry" not in marker_sets:
  s=new_marker_set('particle_247 geometry')
  marker_sets["particle_247 geometry"]=s
s= marker_sets["particle_247 geometry"]
mark=s.place_marker((2737.85, 2036.18, 2456.88), (0.7, 0.7, 0.7), 314.627)
if "particle_248 geometry" not in marker_sets:
  s=new_marker_set('particle_248 geometry')
  marker_sets["particle_248 geometry"]=s
s= marker_sets["particle_248 geometry"]
mark=s.place_marker((2614.42, 1988.14, 2113.39), (0.7, 0.7, 0.7), 115.352)
if "particle_249 geometry" not in marker_sets:
  s=new_marker_set('particle_249 geometry')
  marker_sets["particle_249 geometry"]=s
s= marker_sets["particle_249 geometry"]
mark=s.place_marker((2320.39, 1765.33, 1908.64), (0.7, 0.7, 0.7), 180.621)
if "particle_250 geometry" not in marker_sets:
  s=new_marker_set('particle_250 geometry')
  marker_sets["particle_250 geometry"]=s
s= marker_sets["particle_250 geometry"]
mark=s.place_marker((2089.97, 1648.41, 2161.63), (0.7, 0.7, 0.7), 126.265)
if "particle_251 geometry" not in marker_sets:
  s=new_marker_set('particle_251 geometry')
  marker_sets["particle_251 geometry"]=s
s= marker_sets["particle_251 geometry"]
mark=s.place_marker((1953.47, 1786.64, 2501.52), (0.7, 0.7, 0.7), 133.541)
if "particle_252 geometry" not in marker_sets:
  s=new_marker_set('particle_252 geometry')
  marker_sets["particle_252 geometry"]=s
s= marker_sets["particle_252 geometry"]
mark=s.place_marker((1620.86, 1869.55, 2775.31), (0.7, 0.7, 0.7), 171.019)
if "particle_253 geometry" not in marker_sets:
  s=new_marker_set('particle_253 geometry')
  marker_sets["particle_253 geometry"]=s
s= marker_sets["particle_253 geometry"]
mark=s.place_marker((1231.84, 1888.05, 2896.75), (0.7, 0.7, 0.7), 115.437)
if "particle_254 geometry" not in marker_sets:
  s=new_marker_set('particle_254 geometry')
  marker_sets["particle_254 geometry"]=s
s= marker_sets["particle_254 geometry"]
mark=s.place_marker((1425.49, 1672.05, 2795.15), (0.7, 0.7, 0.7), 158.583)
if "particle_255 geometry" not in marker_sets:
  s=new_marker_set('particle_255 geometry')
  marker_sets["particle_255 geometry"]=s
s= marker_sets["particle_255 geometry"]
mark=s.place_marker((1752.57, 1974.92, 2761.05), (0.7, 0.7, 0.7), 192)
if "particle_256 geometry" not in marker_sets:
  s=new_marker_set('particle_256 geometry')
  marker_sets["particle_256 geometry"]=s
s= marker_sets["particle_256 geometry"]
mark=s.place_marker((2165.73, 2073.26, 2691.24), (0.7, 0.7, 0.7), 150.165)
if "particle_257 geometry" not in marker_sets:
  s=new_marker_set('particle_257 geometry')
  marker_sets["particle_257 geometry"]=s
s= marker_sets["particle_257 geometry"]
mark=s.place_marker((2188.74, 2177.95, 2834.84), (0.7, 0.7, 0.7), 157.567)
if "particle_258 geometry" not in marker_sets:
  s=new_marker_set('particle_258 geometry')
  marker_sets["particle_258 geometry"]=s
s= marker_sets["particle_258 geometry"]
mark=s.place_marker((2201.2, 2284.36, 2801.36), (0.7, 0.7, 0.7), 199.36)
if "particle_259 geometry" not in marker_sets:
  s=new_marker_set('particle_259 geometry')
  marker_sets["particle_259 geometry"]=s
s= marker_sets["particle_259 geometry"]
mark=s.place_marker((1845.88, 2252.07, 2496.6), (0.7, 0.7, 0.7), 105.369)
if "particle_260 geometry" not in marker_sets:
  s=new_marker_set('particle_260 geometry')
  marker_sets["particle_260 geometry"]=s
s= marker_sets["particle_260 geometry"]
mark=s.place_marker((1720.13, 2329.49, 2266.75), (0.7, 0.7, 0.7), 118.651)
if "particle_261 geometry" not in marker_sets:
  s=new_marker_set('particle_261 geometry')
  marker_sets["particle_261 geometry"]=s
s= marker_sets["particle_261 geometry"]
mark=s.place_marker((2151.02, 2321.4, 2375.87), (0.7, 0.7, 0.7), 219.664)
if "particle_262 geometry" not in marker_sets:
  s=new_marker_set('particle_262 geometry')
  marker_sets["particle_262 geometry"]=s
s= marker_sets["particle_262 geometry"]
mark=s.place_marker((2635.79, 2331.34, 2720.33), (0.7, 0.7, 0.7), 196.018)
if "particle_263 geometry" not in marker_sets:
  s=new_marker_set('particle_263 geometry')
  marker_sets["particle_263 geometry"]=s
s= marker_sets["particle_263 geometry"]
mark=s.place_marker((3068.22, 2419.36, 2974.58), (0.7, 0.7, 0.7), 218.141)
if "particle_264 geometry" not in marker_sets:
  s=new_marker_set('particle_264 geometry')
  marker_sets["particle_264 geometry"]=s
s= marker_sets["particle_264 geometry"]
mark=s.place_marker((2960.25, 2689.71, 3164.38), (0.7, 0.7, 0.7), 181.636)
if "particle_265 geometry" not in marker_sets:
  s=new_marker_set('particle_265 geometry')
  marker_sets["particle_265 geometry"]=s
s= marker_sets["particle_265 geometry"]
mark=s.place_marker((2681.22, 2738.02, 3068.58), (0.7, 0.7, 0.7), 195.003)
if "particle_266 geometry" not in marker_sets:
  s=new_marker_set('particle_266 geometry')
  marker_sets["particle_266 geometry"]=s
s= marker_sets["particle_266 geometry"]
mark=s.place_marker((2863.74, 2641.2, 3205.29), (0.7, 0.7, 0.7), 139.209)
if "particle_267 geometry" not in marker_sets:
  s=new_marker_set('particle_267 geometry')
  marker_sets["particle_267 geometry"]=s
s= marker_sets["particle_267 geometry"]
mark=s.place_marker((2835.28, 2612.04, 3280.74), (0.7, 0.7, 0.7), 189.885)
if "particle_268 geometry" not in marker_sets:
  s=new_marker_set('particle_268 geometry')
  marker_sets["particle_268 geometry"]=s
s= marker_sets["particle_268 geometry"]
mark=s.place_marker((2647.53, 2345.25, 3232.93), (0.7, 0.7, 0.7), 267.674)
if "particle_269 geometry" not in marker_sets:
  s=new_marker_set('particle_269 geometry')
  marker_sets["particle_269 geometry"]=s
s= marker_sets["particle_269 geometry"]
mark=s.place_marker((2558.82, 1826.33, 3026.72), (0.7, 0.7, 0.7), 196.568)
if "particle_270 geometry" not in marker_sets:
  s=new_marker_set('particle_270 geometry')
  marker_sets["particle_270 geometry"]=s
s= marker_sets["particle_270 geometry"]
mark=s.place_marker((2499.4, 1829.5, 3281.53), (0.7, 0.7, 0.7), 192.423)
if "particle_271 geometry" not in marker_sets:
  s=new_marker_set('particle_271 geometry')
  marker_sets["particle_271 geometry"]=s
s= marker_sets["particle_271 geometry"]
mark=s.place_marker((2640.43, 2034.4, 3576.35), (1, 0.7, 0), 202.405)
if "particle_272 geometry" not in marker_sets:
  s=new_marker_set('particle_272 geometry')
  marker_sets["particle_272 geometry"]=s
s= marker_sets["particle_272 geometry"]
mark=s.place_marker((2322.87, 1461.48, 3045.32), (0.7, 0.7, 0.7), 135.529)
if "particle_273 geometry" not in marker_sets:
  s=new_marker_set('particle_273 geometry')
  marker_sets["particle_273 geometry"]=s
s= marker_sets["particle_273 geometry"]
mark=s.place_marker((1829.5, 776.527, 2550.29), (0.7, 0.7, 0.7), 114.21)
if "particle_274 geometry" not in marker_sets:
  s=new_marker_set('particle_274 geometry')
  marker_sets["particle_274 geometry"]=s
s= marker_sets["particle_274 geometry"]
mark=s.place_marker((1682.91, 993.077, 2347.88), (0.7, 0.7, 0.7), 159.133)
if "particle_275 geometry" not in marker_sets:
  s=new_marker_set('particle_275 geometry')
  marker_sets["particle_275 geometry"]=s
s= marker_sets["particle_275 geometry"]
mark=s.place_marker((1887.83, 1317.2, 2191.99), (0.7, 0.7, 0.7), 144.412)
if "particle_276 geometry" not in marker_sets:
  s=new_marker_set('particle_276 geometry')
  marker_sets["particle_276 geometry"]=s
s= marker_sets["particle_276 geometry"]
mark=s.place_marker((2077.91, 1545, 2074.74), (0.7, 0.7, 0.7), 70.8525)
if "particle_277 geometry" not in marker_sets:
  s=new_marker_set('particle_277 geometry')
  marker_sets["particle_277 geometry"]=s
s= marker_sets["particle_277 geometry"]
mark=s.place_marker((2343.45, 1976.76, 2444.14), (0.7, 0.7, 0.7), 141.874)
if "particle_278 geometry" not in marker_sets:
  s=new_marker_set('particle_278 geometry')
  marker_sets["particle_278 geometry"]=s
s= marker_sets["particle_278 geometry"]
mark=s.place_marker((2600.78, 2323.28, 2882.32), (0.7, 0.7, 0.7), 217.337)
if "particle_279 geometry" not in marker_sets:
  s=new_marker_set('particle_279 geometry')
  marker_sets["particle_279 geometry"]=s
s= marker_sets["particle_279 geometry"]
mark=s.place_marker((2640.68, 2301.98, 2895.96), (0.7, 0.7, 0.7), 237.641)
if "particle_280 geometry" not in marker_sets:
  s=new_marker_set('particle_280 geometry')
  marker_sets["particle_280 geometry"]=s
s= marker_sets["particle_280 geometry"]
mark=s.place_marker((2673.99, 2067.87, 2493.08), (0.7, 0.7, 0.7), 229.393)
if "particle_281 geometry" not in marker_sets:
  s=new_marker_set('particle_281 geometry')
  marker_sets["particle_281 geometry"]=s
s= marker_sets["particle_281 geometry"]
mark=s.place_marker((3255.69, 2140.36, 2659.83), (0.7, 0.7, 0.7), 349.906)
if "particle_282 geometry" not in marker_sets:
  s=new_marker_set('particle_282 geometry')
  marker_sets["particle_282 geometry"]=s
s= marker_sets["particle_282 geometry"]
mark=s.place_marker((3641.48, 2070.19, 3099.48), (0.7, 0.7, 0.7), 162.347)
if "particle_283 geometry" not in marker_sets:
  s=new_marker_set('particle_283 geometry')
  marker_sets["particle_283 geometry"]=s
s= marker_sets["particle_283 geometry"]
mark=s.place_marker((3792.54, 1990.15, 3188.98), (0.7, 0.7, 0.7), 194.072)
if "particle_284 geometry" not in marker_sets:
  s=new_marker_set('particle_284 geometry')
  marker_sets["particle_284 geometry"]=s
s= marker_sets["particle_284 geometry"]
mark=s.place_marker((3888.67, 1933.56, 3042.55), (0.7, 0.7, 0.7), 242.21)
if "particle_285 geometry" not in marker_sets:
  s=new_marker_set('particle_285 geometry')
  marker_sets["particle_285 geometry"]=s
s= marker_sets["particle_285 geometry"]
mark=s.place_marker((3985.63, 1383.74, 3010.37), (0.7, 0.7, 0.7), 320.93)
if "particle_286 geometry" not in marker_sets:
  s=new_marker_set('particle_286 geometry')
  marker_sets["particle_286 geometry"]=s
s= marker_sets["particle_286 geometry"]
mark=s.place_marker((4472.83, 1074.22, 2976.17), (0.7, 0.7, 0.7), 226.432)
if "particle_287 geometry" not in marker_sets:
  s=new_marker_set('particle_287 geometry')
  marker_sets["particle_287 geometry"]=s
s= marker_sets["particle_287 geometry"]
mark=s.place_marker((4674.57, 1425.44, 3002.18), (0.7, 0.7, 0.7), 125.208)
if "particle_288 geometry" not in marker_sets:
  s=new_marker_set('particle_288 geometry')
  marker_sets["particle_288 geometry"]=s
s= marker_sets["particle_288 geometry"]
mark=s.place_marker((4680.56, 1940.01, 2954.65), (0.7, 0.7, 0.7), 197.837)
if "particle_289 geometry" not in marker_sets:
  s=new_marker_set('particle_289 geometry')
  marker_sets["particle_289 geometry"]=s
s= marker_sets["particle_289 geometry"]
mark=s.place_marker((5112.94, 2152.94, 2541.83), (0.7, 0.7, 0.7), 167.804)
if "particle_290 geometry" not in marker_sets:
  s=new_marker_set('particle_290 geometry')
  marker_sets["particle_290 geometry"]=s
s= marker_sets["particle_290 geometry"]
mark=s.place_marker((5753.3, 2111.01, 2024.13), (0.7, 0.7, 0.7), 136.84)
if "particle_291 geometry" not in marker_sets:
  s=new_marker_set('particle_291 geometry')
  marker_sets["particle_291 geometry"]=s
s= marker_sets["particle_291 geometry"]
mark=s.place_marker((5596.87, 1789.2, 1735.77), (0.7, 0.7, 0.7), 85.7421)
if "particle_292 geometry" not in marker_sets:
  s=new_marker_set('particle_292 geometry')
  marker_sets["particle_292 geometry"]=s
s= marker_sets["particle_292 geometry"]
mark=s.place_marker((4521.09, 1600.72, 2625.25), (1, 0.7, 0), 256)
if "particle_293 geometry" not in marker_sets:
  s=new_marker_set('particle_293 geometry')
  marker_sets["particle_293 geometry"]=s
s= marker_sets["particle_293 geometry"]
mark=s.place_marker((5432.76, 2236.85, 2606.15), (0.7, 0.7, 0.7), 138.702)
if "particle_294 geometry" not in marker_sets:
  s=new_marker_set('particle_294 geometry')
  marker_sets["particle_294 geometry"]=s
s= marker_sets["particle_294 geometry"]
mark=s.place_marker((5762.09, 2553.23, 2730.86), (0.7, 0.7, 0.7), 140.732)
if "particle_295 geometry" not in marker_sets:
  s=new_marker_set('particle_295 geometry')
  marker_sets["particle_295 geometry"]=s
s= marker_sets["particle_295 geometry"]
mark=s.place_marker((5664.67, 2278.49, 2733.28), (0.7, 0.7, 0.7), 81.3006)
if "particle_296 geometry" not in marker_sets:
  s=new_marker_set('particle_296 geometry')
  marker_sets["particle_296 geometry"]=s
s= marker_sets["particle_296 geometry"]
mark=s.place_marker((5883.53, 1939.84, 2610.34), (0.7, 0.7, 0.7), 133.837)
if "particle_297 geometry" not in marker_sets:
  s=new_marker_set('particle_297 geometry')
  marker_sets["particle_297 geometry"]=s
s= marker_sets["particle_297 geometry"]
mark=s.place_marker((5290.97, 1776.48, 2754.13), (0.7, 0.7, 0.7), 98.3475)
if "particle_298 geometry" not in marker_sets:
  s=new_marker_set('particle_298 geometry')
  marker_sets["particle_298 geometry"]=s
s= marker_sets["particle_298 geometry"]
mark=s.place_marker((4545.02, 1906.83, 3064.44), (0.7, 0.7, 0.7), 297.623)
if "particle_299 geometry" not in marker_sets:
  s=new_marker_set('particle_299 geometry')
  marker_sets["particle_299 geometry"]=s
s= marker_sets["particle_299 geometry"]
mark=s.place_marker((4113.99, 1872.52, 3008.07), (0.7, 0.7, 0.7), 212.938)
if "particle_300 geometry" not in marker_sets:
  s=new_marker_set('particle_300 geometry')
  marker_sets["particle_300 geometry"]=s
s= marker_sets["particle_300 geometry"]
mark=s.place_marker((4233.7, 1836, 3226.14), (0.7, 0.7, 0.7), 154.183)
if "particle_301 geometry" not in marker_sets:
  s=new_marker_set('particle_301 geometry')
  marker_sets["particle_301 geometry"]=s
s= marker_sets["particle_301 geometry"]
mark=s.place_marker((4299.06, 1414.89, 3250.22), (0.7, 0.7, 0.7), 180.832)
if "particle_302 geometry" not in marker_sets:
  s=new_marker_set('particle_302 geometry')
  marker_sets["particle_302 geometry"]=s
s= marker_sets["particle_302 geometry"]
mark=s.place_marker((4239.34, 1089.94, 3051.89), (0.7, 0.7, 0.7), 122.332)
if "particle_303 geometry" not in marker_sets:
  s=new_marker_set('particle_303 geometry')
  marker_sets["particle_303 geometry"]=s
s= marker_sets["particle_303 geometry"]
mark=s.place_marker((4139.38, 895.038, 2740.27), (0.7, 0.7, 0.7), 209.047)
if "particle_304 geometry" not in marker_sets:
  s=new_marker_set('particle_304 geometry')
  marker_sets["particle_304 geometry"]=s
s= marker_sets["particle_304 geometry"]
mark=s.place_marker((4186.07, 646.441, 3050.96), (0.7, 0.7, 0.7), 126.985)
if "particle_305 geometry" not in marker_sets:
  s=new_marker_set('particle_305 geometry')
  marker_sets["particle_305 geometry"]=s
s= marker_sets["particle_305 geometry"]
mark=s.place_marker((4434.15, 338.895, 3140.65), (0.7, 0.7, 0.7), 122.205)
if "particle_306 geometry" not in marker_sets:
  s=new_marker_set('particle_306 geometry')
  marker_sets["particle_306 geometry"]=s
s= marker_sets["particle_306 geometry"]
mark=s.place_marker((4674.07, 356.205, 3213.19), (0.7, 0.7, 0.7), 107.95)
if "particle_307 geometry" not in marker_sets:
  s=new_marker_set('particle_307 geometry')
  marker_sets["particle_307 geometry"]=s
s= marker_sets["particle_307 geometry"]
mark=s.place_marker((4357.28, 871.487, 3284.41), (0.7, 0.7, 0.7), 182.567)
if "particle_308 geometry" not in marker_sets:
  s=new_marker_set('particle_308 geometry')
  marker_sets["particle_308 geometry"]=s
s= marker_sets["particle_308 geometry"]
mark=s.place_marker((4094.61, 1448.12, 3182.2), (0.7, 0.7, 0.7), 185.274)
if "particle_309 geometry" not in marker_sets:
  s=new_marker_set('particle_309 geometry')
  marker_sets["particle_309 geometry"]=s
s= marker_sets["particle_309 geometry"]
mark=s.place_marker((3854.78, 1734.76, 2841.14), (0.7, 0.7, 0.7), 413.567)
if "particle_310 geometry" not in marker_sets:
  s=new_marker_set('particle_310 geometry')
  marker_sets["particle_310 geometry"]=s
s= marker_sets["particle_310 geometry"]
mark=s.place_marker((3805.83, 1910.49, 2977.4), (0.7, 0.7, 0.7), 240.01)
if "particle_311 geometry" not in marker_sets:
  s=new_marker_set('particle_311 geometry')
  marker_sets["particle_311 geometry"]=s
s= marker_sets["particle_311 geometry"]
mark=s.place_marker((3799.66, 1875.34, 2958.37), (0.7, 0.7, 0.7), 238.995)
if "particle_312 geometry" not in marker_sets:
  s=new_marker_set('particle_312 geometry')
  marker_sets["particle_312 geometry"]=s
s= marker_sets["particle_312 geometry"]
mark=s.place_marker((3958.28, 1756.47, 3192.43), (0.7, 0.7, 0.7), 203.674)
if "particle_313 geometry" not in marker_sets:
  s=new_marker_set('particle_313 geometry')
  marker_sets["particle_313 geometry"]=s
s= marker_sets["particle_313 geometry"]
mark=s.place_marker((3908.63, 1318.32, 3607.89), (0.7, 0.7, 0.7), 266.744)
if "particle_314 geometry" not in marker_sets:
  s=new_marker_set('particle_314 geometry')
  marker_sets["particle_314 geometry"]=s
s= marker_sets["particle_314 geometry"]
mark=s.place_marker((4246.88, 1553.08, 3794.2), (0.7, 0.7, 0.7), 147.585)
if "particle_315 geometry" not in marker_sets:
  s=new_marker_set('particle_315 geometry')
  marker_sets["particle_315 geometry"]=s
s= marker_sets["particle_315 geometry"]
mark=s.place_marker((4126, 1687.97, 3623.78), (0.7, 0.7, 0.7), 249.485)
if "particle_316 geometry" not in marker_sets:
  s=new_marker_set('particle_316 geometry')
  marker_sets["particle_316 geometry"]=s
s= marker_sets["particle_316 geometry"]
mark=s.place_marker((3812.94, 1494.59, 3451.22), (0.7, 0.7, 0.7), 119.371)
if "particle_317 geometry" not in marker_sets:
  s=new_marker_set('particle_317 geometry')
  marker_sets["particle_317 geometry"]=s
s= marker_sets["particle_317 geometry"]
mark=s.place_marker((3720.12, 980.633, 3021.5), (0.7, 0.7, 0.7), 155.875)
if "particle_318 geometry" not in marker_sets:
  s=new_marker_set('particle_318 geometry')
  marker_sets["particle_318 geometry"]=s
s= marker_sets["particle_318 geometry"]
mark=s.place_marker((3910.5, 716.405, 2323.68), (0.7, 0.7, 0.7), 189.419)
if "particle_319 geometry" not in marker_sets:
  s=new_marker_set('particle_319 geometry')
  marker_sets["particle_319 geometry"]=s
s= marker_sets["particle_319 geometry"]
mark=s.place_marker((3959.41, 1088.19, 1909.81), (0.7, 0.7, 0.7), 137.475)
if "particle_320 geometry" not in marker_sets:
  s=new_marker_set('particle_320 geometry')
  marker_sets["particle_320 geometry"]=s
s= marker_sets["particle_320 geometry"]
mark=s.place_marker((3852.87, 1522.26, 1730.37), (0.7, 0.7, 0.7), 176.179)
if "particle_321 geometry" not in marker_sets:
  s=new_marker_set('particle_321 geometry')
  marker_sets["particle_321 geometry"]=s
s= marker_sets["particle_321 geometry"]
mark=s.place_marker((3902.46, 1859.99, 1438.18), (0.7, 0.7, 0.7), 138.829)
if "particle_322 geometry" not in marker_sets:
  s=new_marker_set('particle_322 geometry')
  marker_sets["particle_322 geometry"]=s
s= marker_sets["particle_322 geometry"]
mark=s.place_marker((4087.87, 2124.74, 1193.24), (0.7, 0.7, 0.7), 148.727)
if "particle_323 geometry" not in marker_sets:
  s=new_marker_set('particle_323 geometry')
  marker_sets["particle_323 geometry"]=s
s= marker_sets["particle_323 geometry"]
mark=s.place_marker((4465.6, 2270.13, 869.833), (0.7, 0.7, 0.7), 230.323)
if "particle_324 geometry" not in marker_sets:
  s=new_marker_set('particle_324 geometry')
  marker_sets["particle_324 geometry"]=s
s= marker_sets["particle_324 geometry"]
mark=s.place_marker((4305.07, 1847.28, 1307.01), (0.7, 0.7, 0.7), 175.376)
if "particle_325 geometry" not in marker_sets:
  s=new_marker_set('particle_325 geometry')
  marker_sets["particle_325 geometry"]=s
s= marker_sets["particle_325 geometry"]
mark=s.place_marker((4077.7, 1694.73, 1722.99), (0.7, 0.7, 0.7), 161.163)
if "particle_326 geometry" not in marker_sets:
  s=new_marker_set('particle_326 geometry')
  marker_sets["particle_326 geometry"]=s
s= marker_sets["particle_326 geometry"]
mark=s.place_marker((3756.74, 1526.38, 1432.56), (0.7, 0.7, 0.7), 125.885)
if "particle_327 geometry" not in marker_sets:
  s=new_marker_set('particle_327 geometry')
  marker_sets["particle_327 geometry"]=s
s= marker_sets["particle_327 geometry"]
mark=s.place_marker((3582.72, 1211.04, 1120.95), (0.7, 0.7, 0.7), 206.635)
if "particle_328 geometry" not in marker_sets:
  s=new_marker_set('particle_328 geometry')
  marker_sets["particle_328 geometry"]=s
s= marker_sets["particle_328 geometry"]
mark=s.place_marker((3482.57, 1682.82, 1234.9), (0.7, 0.7, 0.7), 151.392)
if "particle_329 geometry" not in marker_sets:
  s=new_marker_set('particle_329 geometry')
  marker_sets["particle_329 geometry"]=s
s= marker_sets["particle_329 geometry"]
mark=s.place_marker((3526.19, 2102.81, 1318.82), (0.7, 0.7, 0.7), 173.388)
if "particle_330 geometry" not in marker_sets:
  s=new_marker_set('particle_330 geometry')
  marker_sets["particle_330 geometry"]=s
s= marker_sets["particle_330 geometry"]
mark=s.place_marker((3804.76, 2367.34, 1228.9), (0.7, 0.7, 0.7), 135.825)
if "particle_331 geometry" not in marker_sets:
  s=new_marker_set('particle_331 geometry')
  marker_sets["particle_331 geometry"]=s
s= marker_sets["particle_331 geometry"]
mark=s.place_marker((4213.21, 2474.74, 1036.43), (0.7, 0.7, 0.7), 186.839)
if "particle_332 geometry" not in marker_sets:
  s=new_marker_set('particle_332 geometry')
  marker_sets["particle_332 geometry"]=s
s= marker_sets["particle_332 geometry"]
mark=s.place_marker((4646.81, 2475.4, 807.704), (0.7, 0.7, 0.7), 121.189)
if "particle_333 geometry" not in marker_sets:
  s=new_marker_set('particle_333 geometry')
  marker_sets["particle_333 geometry"]=s
s= marker_sets["particle_333 geometry"]
mark=s.place_marker((4432.03, 2192.52, 1064.66), (0.7, 0.7, 0.7), 102.916)
if "particle_334 geometry" not in marker_sets:
  s=new_marker_set('particle_334 geometry')
  marker_sets["particle_334 geometry"]=s
s= marker_sets["particle_334 geometry"]
mark=s.place_marker((4151.72, 1866.46, 1540.68), (0.7, 0.7, 0.7), 212.769)
if "particle_335 geometry" not in marker_sets:
  s=new_marker_set('particle_335 geometry')
  marker_sets["particle_335 geometry"]=s
s= marker_sets["particle_335 geometry"]
mark=s.place_marker((3698.85, 1758.89, 2055.96), (0.7, 0.7, 0.7), 173.092)
if "particle_336 geometry" not in marker_sets:
  s=new_marker_set('particle_336 geometry')
  marker_sets["particle_336 geometry"]=s
s= marker_sets["particle_336 geometry"]
mark=s.place_marker((3510.73, 1478.03, 2427.54), (0.7, 0.7, 0.7), 264.502)
if "particle_337 geometry" not in marker_sets:
  s=new_marker_set('particle_337 geometry')
  marker_sets["particle_337 geometry"]=s
s= marker_sets["particle_337 geometry"]
mark=s.place_marker((3605.08, 957.267, 2594.69), (0.7, 0.7, 0.7), 208.666)
if "particle_338 geometry" not in marker_sets:
  s=new_marker_set('particle_338 geometry')
  marker_sets["particle_338 geometry"]=s
s= marker_sets["particle_338 geometry"]
mark=s.place_marker((3898.37, 619.159, 2800.88), (0.7, 0.7, 0.7), 186.797)
if "particle_339 geometry" not in marker_sets:
  s=new_marker_set('particle_339 geometry')
  marker_sets["particle_339 geometry"]=s
s= marker_sets["particle_339 geometry"]
mark=s.place_marker((3968.54, 704.778, 3292.94), (0.7, 0.7, 0.7), 255.534)
if "particle_340 geometry" not in marker_sets:
  s=new_marker_set('particle_340 geometry')
  marker_sets["particle_340 geometry"]=s
s= marker_sets["particle_340 geometry"]
mark=s.place_marker((4360.34, 788.464, 3445.81), (0.7, 0.7, 0.7), 153.126)
if "particle_341 geometry" not in marker_sets:
  s=new_marker_set('particle_341 geometry')
  marker_sets["particle_341 geometry"]=s
s= marker_sets["particle_341 geometry"]
mark=s.place_marker((4393.91, 410.827, 3373.47), (0.7, 0.7, 0.7), 165.816)
if "particle_342 geometry" not in marker_sets:
  s=new_marker_set('particle_342 geometry')
  marker_sets["particle_342 geometry"]=s
s= marker_sets["particle_342 geometry"]
mark=s.place_marker((4040.47, 478.779, 3484.21), (0.7, 0.7, 0.7), 134.429)
if "particle_343 geometry" not in marker_sets:
  s=new_marker_set('particle_343 geometry')
  marker_sets["particle_343 geometry"]=s
s= marker_sets["particle_343 geometry"]
mark=s.place_marker((3823.55, 624.72, 3244.28), (0.7, 0.7, 0.7), 178.971)
if "particle_344 geometry" not in marker_sets:
  s=new_marker_set('particle_344 geometry')
  marker_sets["particle_344 geometry"]=s
s= marker_sets["particle_344 geometry"]
mark=s.place_marker((3966.85, 662.703, 2781.28), (0.7, 0.7, 0.7), 189.969)
if "particle_345 geometry" not in marker_sets:
  s=new_marker_set('particle_345 geometry')
  marker_sets["particle_345 geometry"]=s
s= marker_sets["particle_345 geometry"]
mark=s.place_marker((4126.49, 248.179, 2354.35), (0.7, 0.7, 0.7), 121.359)
if "particle_346 geometry" not in marker_sets:
  s=new_marker_set('particle_346 geometry')
  marker_sets["particle_346 geometry"]=s
s= marker_sets["particle_346 geometry"]
mark=s.place_marker((4164.9, 437.862, 1845.33), (0.7, 0.7, 0.7), 187.262)
if "particle_347 geometry" not in marker_sets:
  s=new_marker_set('particle_347 geometry')
  marker_sets["particle_347 geometry"]=s
s= marker_sets["particle_347 geometry"]
mark=s.place_marker((3957.54, 980.395, 1543.74), (0.7, 0.7, 0.7), 164.335)
if "particle_348 geometry" not in marker_sets:
  s=new_marker_set('particle_348 geometry')
  marker_sets["particle_348 geometry"]=s
s= marker_sets["particle_348 geometry"]
mark=s.place_marker((4184.32, 1454.38, 1443.67), (0.7, 0.7, 0.7), 138.363)
if "particle_349 geometry" not in marker_sets:
  s=new_marker_set('particle_349 geometry')
  marker_sets["particle_349 geometry"]=s
s= marker_sets["particle_349 geometry"]
mark=s.place_marker((4341.68, 1761.38, 1246.98), (0.7, 0.7, 0.7), 138.49)
if "particle_350 geometry" not in marker_sets:
  s=new_marker_set('particle_350 geometry')
  marker_sets["particle_350 geometry"]=s
s= marker_sets["particle_350 geometry"]
mark=s.place_marker((4039.62, 1831.09, 1078.65), (0.7, 0.7, 0.7), 116.325)
if "particle_351 geometry" not in marker_sets:
  s=new_marker_set('particle_351 geometry')
  marker_sets["particle_351 geometry"]=s
s= marker_sets["particle_351 geometry"]
mark=s.place_marker((3771.31, 1558.09, 1332.23), (0.7, 0.7, 0.7), 106.511)
if "particle_352 geometry" not in marker_sets:
  s=new_marker_set('particle_352 geometry')
  marker_sets["particle_352 geometry"]=s
s= marker_sets["particle_352 geometry"]
mark=s.place_marker((3734.29, 1236.92, 1780.14), (0.7, 0.7, 0.7), 151.096)
if "particle_353 geometry" not in marker_sets:
  s=new_marker_set('particle_353 geometry')
  marker_sets["particle_353 geometry"]=s
s= marker_sets["particle_353 geometry"]
mark=s.place_marker((3892.98, 779.044, 2243.07), (0.7, 0.7, 0.7), 240.856)
if "particle_354 geometry" not in marker_sets:
  s=new_marker_set('particle_354 geometry')
  marker_sets["particle_354 geometry"]=s
s= marker_sets["particle_354 geometry"]
mark=s.place_marker((4118.71, 474.101, 2588.19), (0.7, 0.7, 0.7), 149.7)
if "particle_355 geometry" not in marker_sets:
  s=new_marker_set('particle_355 geometry')
  marker_sets["particle_355 geometry"]=s
s= marker_sets["particle_355 geometry"]
mark=s.place_marker((4081.22, 405.296, 2920.32), (0.7, 0.7, 0.7), 165.943)
if "particle_356 geometry" not in marker_sets:
  s=new_marker_set('particle_356 geometry')
  marker_sets["particle_356 geometry"]=s
s= marker_sets["particle_356 geometry"]
mark=s.place_marker((3860.38, 897.161, 3214.12), (0.7, 0.7, 0.7), 178.971)
if "particle_357 geometry" not in marker_sets:
  s=new_marker_set('particle_357 geometry')
  marker_sets["particle_357 geometry"]=s
s= marker_sets["particle_357 geometry"]
mark=s.place_marker((3470.23, 1281.47, 3723.81), (0.7, 0.7, 0.7), 154.945)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
