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
mark=s.place_marker((3338.52, 1420.5, -687.124), (0.7, 0.7, 0.7), 182.271)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((3266.2, 1864.92, -673.274), (0.7, 0.7, 0.7), 258.199)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((3268.02, 2016.67, -298.016), (0.7, 0.7, 0.7), 123.897)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((3582.01, 2176.93, -499.893), (0.7, 0.7, 0.7), 146.739)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((3941.62, 2440.05, -647.333), (0.7, 0.7, 0.7), 179.098)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((3618.08, 2552.41, -155.352), (0.7, 0.7, 0.7), 148.854)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((3440.32, 2686.69, 336.118), (0.7, 0.7, 0.7), 196.357)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((3985.57, 2692.51, 385.424), (0.7, 0.7, 0.7), 166.873)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((4570.41, 2792.28, 425.158), (0.7, 0.7, 0.7), 95.4711)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((4177.21, 2919.35, 560.068), (0.7, 0.7, 0.7), 185.401)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((3626.33, 2964.88, 479.246), (0.7, 0.7, 0.7), 151.984)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((2949.96, 2932.53, 441.646), (0.7, 0.7, 0.7), 185.612)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((2475.29, 3125.8, 211.442), (0.7, 0.7, 0.7), 210.273)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((2085.57, 3368.15, 54.7515), (0.7, 0.7, 0.7), 106.892)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((1568.59, 3605.91, 7.59115), (0.7, 0.7, 0.7), 202.025)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((921.839, 3548.55, -116.381), (0.7, 0.7, 0.7), 192.169)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((335.596, 3325.91, -249.121), (0.7, 0.7, 0.7), 241.11)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((102.517, 2959.56, -325.061), (0.7, 0.7, 0.7), 128.465)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((-36.2878, 2663.39, -675.318), (0.7, 0.7, 0.7), 217.38)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((-326.051, 2425.24, -1275.02), (0.7, 0.7, 0.7), 184.555)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((24.0574, 2435.4, -727.562), (0.7, 0.7, 0.7), 140.055)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((86.5187, 2724.66, -400.364), (0.7, 0.7, 0.7), 169.708)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((-87.7912, 3047.06, -198.175), (0.7, 0.7, 0.7), 184.639)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((-113.397, 2864.64, 33.3901), (0.7, 0.7, 0.7), 119.286)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((-188.668, 2583.29, -11.6351), (0.7, 0.7, 0.7), 147.754)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((29.3358, 2425.93, -202.943), (0.7, 0.7, 0.7), 171.4)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((373.968, 2589.63, -60.4603), (0.7, 0.7, 0.7), 156.341)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((894.58, 2484.14, 189.771), (0.7, 0.7, 0.7), 186.501)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((1329.82, 2404.61, 499.526), (0.7, 0.7, 0.7), 308.325)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((1673.19, 2585.3, 614.167), (0.7, 0.7, 0.7), 138.617)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((1778.3, 2782.62, 808.065), (0.7, 0.7, 0.7), 130.03)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((1476.02, 2750.43, 676.15), (0.7, 0.7, 0.7), 156.552)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((1603.97, 2508.95, 515.757), (0.7, 0.7, 0.7), 183.244)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((1664.39, 2282.66, 382.312), (0.7, 0.7, 0.7), 181.382)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((1571.82, 2109.56, 405.389), (0.7, 0.7, 0.7), 101.943)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((1472.82, 1838.59, 180.446), (1, 0.7, 0), 138.913)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((478.232, 2012.89, 473.714), (0.7, 0.7, 0.7), 221.737)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((-132.743, 2132.94, 845.531), (0.7, 0.7, 0.7), 256.38)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((-522.121, 2195.54, 1125.9), (0.7, 0.7, 0.7), 221.694)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((-567.57, 2800.13, 987.859), (0.7, 0.7, 0.7), 259.341)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((224.8, 2933.65, 1127.31), (0.7, 0.7, 0.7), 117.89)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((1209.56, 2692.14, 1081.33), (0.7, 0.7, 0.7), 116.071)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((1809.34, 2296.47, 1145.03), (0.7, 0.7, 0.7), 268.224)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((2070.05, 2035.77, 1232.66), (0.7, 0.7, 0.7), 386.918)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((2667.75, 1949.31, 1450.72), (0.7, 0.7, 0.7), 121.316)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((2915.75, 1604.16, 1509.94), (0.7, 0.7, 0.7), 138.363)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((2332.01, 1541.14, 1089.92), (1, 0.7, 0), 175.207)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((2900.12, 1144.7, 1312.75), (0.7, 0.7, 0.7), 131.468)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((3358.11, 585.599, 1486.24), (0.7, 0.7, 0.7), 287.894)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((2967.68, 803.971, 1777.9), (0.7, 0.7, 0.7), 88.1109)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((2583.09, 1269.89, 1759.08), (0.7, 0.7, 0.7), 145.385)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((2516.38, 1473.75, 1847.79), (0.7, 0.7, 0.7), 155.452)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((2898.69, 1071.22, 2152.08), (0.7, 0.7, 0.7), 145.512)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((3252.35, 803.601, 2419.33), (0.7, 0.7, 0.7), 99.9972)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((3608.85, 644.976, 2638.91), (0.7, 0.7, 0.7), 327.529)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((3535.41, 1277.3, 2641.44), (0.7, 0.7, 0.7), 137.983)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((3128.02, 1555.92, 2538.33), (0.7, 0.7, 0.7), 83.3733)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((2637.09, 1799.1, 2358), (0.7, 0.7, 0.7), 101.562)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((2213.86, 1947.91, 2071.75), (0.7, 0.7, 0.7), 165.689)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((2085.84, 1670.07, 1987.56), (0.7, 0.7, 0.7), 136.925)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((2216.21, 1613.03, 1960.33), (0.7, 0.7, 0.7), 123.389)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((2619.88, 1539.71, 2233.21), (0.7, 0.7, 0.7), 184.47)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((3256.53, 1319.2, 2719.14), (0.7, 0.7, 0.7), 148.473)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((3990.4, 976.487, 3365.42), (0.7, 0.7, 0.7), 241.406)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((3808.2, 1451.15, 2899.7), (0.7, 0.7, 0.7), 182.736)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((3661.17, 1690.99, 2555.02), (0.7, 0.7, 0.7), 166.62)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((3361.15, 1681.78, 2609.15), (0.7, 0.7, 0.7), 113.872)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((3116.69, 1593.8, 2427.73), (0.7, 0.7, 0.7), 110.065)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((2896.43, 1364.14, 2189.46), (0.7, 0.7, 0.7), 150.08)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((2729.2, 1015.84, 1891.22), (0.7, 0.7, 0.7), 118.525)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((2532.62, 542.156, 1692.53), (0.7, 0.7, 0.7), 163.955)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((2523.41, 187.984, 1830.27), (0.7, 0.7, 0.7), 170.131)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((2800.38, 345.512, 2512.48), (0.7, 0.7, 0.7), 78.2127)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((3177.73, 614.968, 3195.61), (0.7, 0.7, 0.7), 251.896)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((3546.38, 979.988, 3626.36), (0.7, 0.7, 0.7), 167.55)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((3687.09, 1336.94, 3772), (0.7, 0.7, 0.7), 167.846)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((3324.24, 1118.68, 4050.38), (0.7, 0.7, 0.7), 259.68)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((3066.05, 736.8, 3995.98), (0.7, 0.7, 0.7), 80.2854)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((3188.85, 593.074, 4062.24), (0.7, 0.7, 0.7), 82.4427)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((3269.58, 679.519, 4457.96), (0.7, 0.7, 0.7), 212.811)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((2638.45, 1053.02, 4520.86), (0.7, 0.7, 0.7), 176.391)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((2341.2, 1526.81, 4043.92), (0.7, 0.7, 0.7), 99.3204)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((2110.12, 1610.51, 3498.59), (0.7, 0.7, 0.7), 166.62)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((1849.05, 1615.95, 3348.09), (0.7, 0.7, 0.7), 102.831)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((1987.87, 1385.56, 4206.53), (0.7, 0.7, 0.7), 65.0997)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((2474.97, 1352.19, 4010.17), (0.7, 0.7, 0.7), 92.1294)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((2805.8, 1435.15, 3549.19), (0.7, 0.7, 0.7), 194.791)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((3110.1, 1592.56, 3285.94), (0.7, 0.7, 0.7), 120.766)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((3395.93, 1617.5, 3792.9), (0.7, 0.7, 0.7), 217.803)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((3184.35, 1287.15, 3747.45), (0.7, 0.7, 0.7), 115.775)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((3091.57, 1043, 3412.45), (0.7, 0.7, 0.7), 115.648)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((3033.09, 1263.1, 3167.12), (0.7, 0.7, 0.7), 83.8386)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((3279.1, 1559.64, 3111.73), (0.7, 0.7, 0.7), 124.32)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((3636.61, 1772.73, 2918.33), (0.7, 0.7, 0.7), 185.993)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((4225.8, 1632.87, 2741.06), (0.7, 0.7, 0.7), 238.826)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((4542.21, 1189.5, 2691.72), (0.7, 0.7, 0.7), 128.465)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((3981.53, 879.77, 2740.13), (0.7, 0.7, 0.7), 203.209)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((3532.37, 1078.09, 2877.64), (0.7, 0.7, 0.7), 160.486)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((3724.43, 1347.42, 2988.83), (0.7, 0.7, 0.7), 149.277)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((4066.88, 1063.83, 3290.88), (0.7, 0.7, 0.7), 35.7435)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((3143.41, 1110.71, 2907.37), (0.7, 0.7, 0.7), 98.3898)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((2215.62, 1416.78, 2504.67), (0.7, 0.7, 0.7), 188.404)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((1973.42, 1860.88, 2424.69), (0.7, 0.7, 0.7), 110.318)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((2216.59, 1833.37, 2730.22), (0.7, 0.7, 0.7), 127.534)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((2527.42, 1690.13, 2920.84), (0.7, 0.7, 0.7), 91.368)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((2868.26, 1496.44, 3019.41), (0.7, 0.7, 0.7), 131.045)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((3209.72, 1298.39, 2897.28), (0.7, 0.7, 0.7), 143.608)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((3555.34, 1473.75, 2821.84), (0.7, 0.7, 0.7), 135.783)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((3828.3, 1668.09, 2785.39), (0.7, 0.7, 0.7), 92.5947)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((3700.9, 1907.74, 2839.77), (0.7, 0.7, 0.7), 150.123)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((3515.68, 2031.38, 2939.91), (0.7, 0.7, 0.7), 121.57)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((3678.92, 2231.75, 3143.42), (0.7, 0.7, 0.7), 104.777)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((3353.44, 2428.98, 2990.43), (0.7, 0.7, 0.7), 114.844)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((2996.99, 2632.87, 2826.4), (0.7, 0.7, 0.7), 150.588)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((2658.33, 2404.08, 2750.53), (0.7, 0.7, 0.7), 103.55)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((2296.93, 2088.13, 2999.93), (0.7, 0.7, 0.7), 215.392)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((1831.41, 1832.6, 3156.82), (0.7, 0.7, 0.7), 99.9126)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((1592.9, 1640.19, 3815.89), (0.7, 0.7, 0.7), 99.7857)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((1557.73, 1353.33, 4300.06), (0.7, 0.7, 0.7), 109.98)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((1784.15, 1715.68, 4010.03), (0.7, 0.7, 0.7), 102.831)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((2021.42, 1804.24, 3702.41), (0.7, 0.7, 0.7), 103.593)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((2405, 1805.79, 3413.21), (0.7, 0.7, 0.7), 173.472)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((2904.63, 1571.02, 3460.18), (0.7, 0.7, 0.7), 113.575)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((3305.75, 1611.55, 3213.42), (0.7, 0.7, 0.7), 128.296)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((3733.3, 1718.68, 3039.05), (0.7, 0.7, 0.7), 145.004)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((4095.1, 1968.53, 2702.51), (0.7, 0.7, 0.7), 148.261)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((4703.39, 2027.9, 2479.47), (0.7, 0.7, 0.7), 127.704)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((5252.51, 1873.59, 2292.43), (0.7, 0.7, 0.7), 129.607)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((4993.33, 1506.22, 2439.03), (0.7, 0.7, 0.7), 139.759)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((4460.32, 1205.29, 2532.71), (0.7, 0.7, 0.7), 118.567)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((4252.54, 1276.18, 2849.65), (0.7, 0.7, 0.7), 136.164)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((3899.71, 1462.55, 3039.24), (0.7, 0.7, 0.7), 121.655)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((3622.63, 1759.99, 3216.15), (0.7, 0.7, 0.7), 127.492)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((3591.66, 1959.41, 3605.17), (0.7, 0.7, 0.7), 138.617)
if "particle_134 geometry" not in marker_sets:
  s=new_marker_set('particle_134 geometry')
  marker_sets["particle_134 geometry"]=s
s= marker_sets["particle_134 geometry"]
mark=s.place_marker((3400.86, 2271.9, 3639.7), (0.7, 0.7, 0.7), 120.766)
if "particle_135 geometry" not in marker_sets:
  s=new_marker_set('particle_135 geometry')
  marker_sets["particle_135 geometry"]=s
s= marker_sets["particle_135 geometry"]
mark=s.place_marker((3116.59, 2313.32, 3607.26), (0.7, 0.7, 0.7), 145.893)
if "particle_136 geometry" not in marker_sets:
  s=new_marker_set('particle_136 geometry')
  marker_sets["particle_136 geometry"]=s
s= marker_sets["particle_136 geometry"]
mark=s.place_marker((3036.56, 2070.01, 3219.35), (0.7, 0.7, 0.7), 185.02)
if "particle_137 geometry" not in marker_sets:
  s=new_marker_set('particle_137 geometry')
  marker_sets["particle_137 geometry"]=s
s= marker_sets["particle_137 geometry"]
mark=s.place_marker((2847.62, 2084.57, 2722.6), (0.7, 0.7, 0.7), 221.314)
if "particle_138 geometry" not in marker_sets:
  s=new_marker_set('particle_138 geometry')
  marker_sets["particle_138 geometry"]=s
s= marker_sets["particle_138 geometry"]
mark=s.place_marker((2707.57, 2298.99, 2285.54), (0.7, 0.7, 0.7), 165.139)
if "particle_139 geometry" not in marker_sets:
  s=new_marker_set('particle_139 geometry')
  marker_sets["particle_139 geometry"]=s
s= marker_sets["particle_139 geometry"]
mark=s.place_marker((2776.88, 2252.25, 2146.14), (0.7, 0.7, 0.7), 179.437)
if "particle_140 geometry" not in marker_sets:
  s=new_marker_set('particle_140 geometry')
  marker_sets["particle_140 geometry"]=s
s= marker_sets["particle_140 geometry"]
mark=s.place_marker((2777.01, 1981.57, 2480.5), (0.7, 0.7, 0.7), 137.898)
if "particle_141 geometry" not in marker_sets:
  s=new_marker_set('particle_141 geometry')
  marker_sets["particle_141 geometry"]=s
s= marker_sets["particle_141 geometry"]
mark=s.place_marker((2792.3, 1744.01, 2777.21), (0.7, 0.7, 0.7), 124.658)
if "particle_142 geometry" not in marker_sets:
  s=new_marker_set('particle_142 geometry')
  marker_sets["particle_142 geometry"]=s
s= marker_sets["particle_142 geometry"]
mark=s.place_marker((2859.83, 1868.51, 3082.23), (0.7, 0.7, 0.7), 97.7553)
if "particle_143 geometry" not in marker_sets:
  s=new_marker_set('particle_143 geometry')
  marker_sets["particle_143 geometry"]=s
s= marker_sets["particle_143 geometry"]
mark=s.place_marker((2877.15, 1914.16, 3397.85), (0.7, 0.7, 0.7), 92.9331)
if "particle_144 geometry" not in marker_sets:
  s=new_marker_set('particle_144 geometry')
  marker_sets["particle_144 geometry"]=s
s= marker_sets["particle_144 geometry"]
mark=s.place_marker((2885.64, 1839.2, 3760.3), (0.7, 0.7, 0.7), 123.135)
if "particle_145 geometry" not in marker_sets:
  s=new_marker_set('particle_145 geometry')
  marker_sets["particle_145 geometry"]=s
s= marker_sets["particle_145 geometry"]
mark=s.place_marker((2637.14, 1808.56, 3442.23), (0.7, 0.7, 0.7), 125.716)
if "particle_146 geometry" not in marker_sets:
  s=new_marker_set('particle_146 geometry')
  marker_sets["particle_146 geometry"]=s
s= marker_sets["particle_146 geometry"]
mark=s.place_marker((2569.1, 1896.67, 3159.31), (0.7, 0.7, 0.7), 127.534)
if "particle_147 geometry" not in marker_sets:
  s=new_marker_set('particle_147 geometry')
  marker_sets["particle_147 geometry"]=s
s= marker_sets["particle_147 geometry"]
mark=s.place_marker((2828.83, 1855.17, 3074.87), (0.7, 0.7, 0.7), 94.9212)
if "particle_148 geometry" not in marker_sets:
  s=new_marker_set('particle_148 geometry')
  marker_sets["particle_148 geometry"]=s
s= marker_sets["particle_148 geometry"]
mark=s.place_marker((2734.68, 1925.2, 2655.92), (0.7, 0.7, 0.7), 137.644)
if "particle_149 geometry" not in marker_sets:
  s=new_marker_set('particle_149 geometry')
  marker_sets["particle_149 geometry"]=s
s= marker_sets["particle_149 geometry"]
mark=s.place_marker((2765.18, 2038.33, 2328.59), (0.7, 0.7, 0.7), 149.277)
if "particle_150 geometry" not in marker_sets:
  s=new_marker_set('particle_150 geometry')
  marker_sets["particle_150 geometry"]=s
s= marker_sets["particle_150 geometry"]
mark=s.place_marker((2817.53, 2332.19, 2518.81), (0.7, 0.7, 0.7), 103.677)
if "particle_151 geometry" not in marker_sets:
  s=new_marker_set('particle_151 geometry')
  marker_sets["particle_151 geometry"]=s
s= marker_sets["particle_151 geometry"]
mark=s.place_marker((3081.02, 2590.32, 2836.81), (0.7, 0.7, 0.7), 99.6588)
if "particle_152 geometry" not in marker_sets:
  s=new_marker_set('particle_152 geometry')
  marker_sets["particle_152 geometry"]=s
s= marker_sets["particle_152 geometry"]
mark=s.place_marker((3326.92, 2789.62, 3036.88), (0.7, 0.7, 0.7), 134.133)
if "particle_153 geometry" not in marker_sets:
  s=new_marker_set('particle_153 geometry')
  marker_sets["particle_153 geometry"]=s
s= marker_sets["particle_153 geometry"]
mark=s.place_marker((3007.84, 2695.41, 3061.73), (0.7, 0.7, 0.7), 173.007)
if "particle_154 geometry" not in marker_sets:
  s=new_marker_set('particle_154 geometry')
  marker_sets["particle_154 geometry"]=s
s= marker_sets["particle_154 geometry"]
mark=s.place_marker((2668.59, 2501.83, 2647.18), (0.7, 0.7, 0.7), 141.028)
if "particle_155 geometry" not in marker_sets:
  s=new_marker_set('particle_155 geometry')
  marker_sets["particle_155 geometry"]=s
s= marker_sets["particle_155 geometry"]
mark=s.place_marker((2392.24, 2255.37, 2362.42), (0.7, 0.7, 0.7), 161.121)
if "particle_156 geometry" not in marker_sets:
  s=new_marker_set('particle_156 geometry')
  marker_sets["particle_156 geometry"]=s
s= marker_sets["particle_156 geometry"]
mark=s.place_marker((2501.7, 1928.36, 2319.1), (0.7, 0.7, 0.7), 119.582)
if "particle_157 geometry" not in marker_sets:
  s=new_marker_set('particle_157 geometry')
  marker_sets["particle_157 geometry"]=s
s= marker_sets["particle_157 geometry"]
mark=s.place_marker((2693.18, 1819.73, 2653.45), (0.7, 0.7, 0.7), 137.094)
if "particle_158 geometry" not in marker_sets:
  s=new_marker_set('particle_158 geometry')
  marker_sets["particle_158 geometry"]=s
s= marker_sets["particle_158 geometry"]
mark=s.place_marker((2759.6, 1640.91, 3116.56), (0.7, 0.7, 0.7), 149.234)
if "particle_159 geometry" not in marker_sets:
  s=new_marker_set('particle_159 geometry')
  marker_sets["particle_159 geometry"]=s
s= marker_sets["particle_159 geometry"]
mark=s.place_marker((2349.66, 1544.25, 3158.66), (0.7, 0.7, 0.7), 151.011)
if "particle_160 geometry" not in marker_sets:
  s=new_marker_set('particle_160 geometry')
  marker_sets["particle_160 geometry"]=s
s= marker_sets["particle_160 geometry"]
mark=s.place_marker((1912.5, 1651.33, 2928.37), (0.7, 0.7, 0.7), 184.216)
if "particle_161 geometry" not in marker_sets:
  s=new_marker_set('particle_161 geometry')
  marker_sets["particle_161 geometry"]=s
s= marker_sets["particle_161 geometry"]
mark=s.place_marker((1822.06, 2039.59, 3029.04), (0.7, 0.7, 0.7), 170.596)
if "particle_162 geometry" not in marker_sets:
  s=new_marker_set('particle_162 geometry')
  marker_sets["particle_162 geometry"]=s
s= marker_sets["particle_162 geometry"]
mark=s.place_marker((2017.35, 2020.1, 3628.39), (0.7, 0.7, 0.7), 215.603)
if "particle_163 geometry" not in marker_sets:
  s=new_marker_set('particle_163 geometry')
  marker_sets["particle_163 geometry"]=s
s= marker_sets["particle_163 geometry"]
mark=s.place_marker((2289.57, 1903.24, 4459.59), (0.7, 0.7, 0.7), 79.0164)
if "particle_164 geometry" not in marker_sets:
  s=new_marker_set('particle_164 geometry')
  marker_sets["particle_164 geometry"]=s
s= marker_sets["particle_164 geometry"]
mark=s.place_marker((2465.63, 2186.75, 4541.26), (0.7, 0.7, 0.7), 77.2821)
if "particle_165 geometry" not in marker_sets:
  s=new_marker_set('particle_165 geometry')
  marker_sets["particle_165 geometry"]=s
s= marker_sets["particle_165 geometry"]
mark=s.place_marker((2605.33, 2332.25, 4252.64), (0.7, 0.7, 0.7), 188.658)
if "particle_166 geometry" not in marker_sets:
  s=new_marker_set('particle_166 geometry')
  marker_sets["particle_166 geometry"]=s
s= marker_sets["particle_166 geometry"]
mark=s.place_marker((2512.77, 2627.84, 4223.42), (0.7, 0.7, 0.7), 115.437)
if "particle_167 geometry" not in marker_sets:
  s=new_marker_set('particle_167 geometry')
  marker_sets["particle_167 geometry"]=s
s= marker_sets["particle_167 geometry"]
mark=s.place_marker((2414.8, 2438.87, 3654.31), (0.7, 0.7, 0.7), 88.4916)
if "particle_168 geometry" not in marker_sets:
  s=new_marker_set('particle_168 geometry')
  marker_sets["particle_168 geometry"]=s
s= marker_sets["particle_168 geometry"]
mark=s.place_marker((2315.01, 2235.4, 3072.47), (0.7, 0.7, 0.7), 108.88)
if "particle_169 geometry" not in marker_sets:
  s=new_marker_set('particle_169 geometry')
  marker_sets["particle_169 geometry"]=s
s= marker_sets["particle_169 geometry"]
mark=s.place_marker((2226.71, 1963.47, 2857.78), (0.7, 0.7, 0.7), 172.119)
if "particle_170 geometry" not in marker_sets:
  s=new_marker_set('particle_170 geometry')
  marker_sets["particle_170 geometry"]=s
s= marker_sets["particle_170 geometry"]
mark=s.place_marker((2257.96, 1924, 3343.54), (0.7, 0.7, 0.7), 139.505)
if "particle_171 geometry" not in marker_sets:
  s=new_marker_set('particle_171 geometry')
  marker_sets["particle_171 geometry"]=s
s= marker_sets["particle_171 geometry"]
mark=s.place_marker((2301.01, 1885.05, 3826.39), (0.7, 0.7, 0.7), 92.7639)
if "particle_172 geometry" not in marker_sets:
  s=new_marker_set('particle_172 geometry')
  marker_sets["particle_172 geometry"]=s
s= marker_sets["particle_172 geometry"]
mark=s.place_marker((2174.7, 1678.41, 3769.46), (0.7, 0.7, 0.7), 89.8452)
if "particle_173 geometry" not in marker_sets:
  s=new_marker_set('particle_173 geometry')
  marker_sets["particle_173 geometry"]=s
s= marker_sets["particle_173 geometry"]
mark=s.place_marker((2024.58, 1913.54, 3697.82), (0.7, 0.7, 0.7), 149.446)
if "particle_174 geometry" not in marker_sets:
  s=new_marker_set('particle_174 geometry')
  marker_sets["particle_174 geometry"]=s
s= marker_sets["particle_174 geometry"]
mark=s.place_marker((2052.34, 2184.33, 3900.85), (0.7, 0.7, 0.7), 126.858)
if "particle_175 geometry" not in marker_sets:
  s=new_marker_set('particle_175 geometry')
  marker_sets["particle_175 geometry"]=s
s= marker_sets["particle_175 geometry"]
mark=s.place_marker((2275.98, 2042.66, 4129.3), (0.7, 0.7, 0.7), 106.046)
if "particle_176 geometry" not in marker_sets:
  s=new_marker_set('particle_176 geometry')
  marker_sets["particle_176 geometry"]=s
s= marker_sets["particle_176 geometry"]
mark=s.place_marker((2512.41, 1580.06, 4078.74), (0.7, 0.7, 0.7), 156.298)
if "particle_177 geometry" not in marker_sets:
  s=new_marker_set('particle_177 geometry')
  marker_sets["particle_177 geometry"]=s
s= marker_sets["particle_177 geometry"]
mark=s.place_marker((2887.97, 1098.01, 3966.81), (0.7, 0.7, 0.7), 231.212)
if "particle_178 geometry" not in marker_sets:
  s=new_marker_set('particle_178 geometry')
  marker_sets["particle_178 geometry"]=s
s= marker_sets["particle_178 geometry"]
mark=s.place_marker((2835.24, 774.352, 3505.05), (0.7, 0.7, 0.7), 88.4916)
if "particle_179 geometry" not in marker_sets:
  s=new_marker_set('particle_179 geometry')
  marker_sets["particle_179 geometry"]=s
s= marker_sets["particle_179 geometry"]
mark=s.place_marker((2586.2, 872.873, 3103.25), (0.7, 0.7, 0.7), 111.334)
if "particle_180 geometry" not in marker_sets:
  s=new_marker_set('particle_180 geometry')
  marker_sets["particle_180 geometry"]=s
s= marker_sets["particle_180 geometry"]
mark=s.place_marker((2293.21, 1325.49, 2809.01), (0.7, 0.7, 0.7), 127.619)
if "particle_181 geometry" not in marker_sets:
  s=new_marker_set('particle_181 geometry')
  marker_sets["particle_181 geometry"]=s
s= marker_sets["particle_181 geometry"]
mark=s.place_marker((2065.08, 1666.73, 2615.5), (0.7, 0.7, 0.7), 230.746)
if "particle_182 geometry" not in marker_sets:
  s=new_marker_set('particle_182 geometry')
  marker_sets["particle_182 geometry"]=s
s= marker_sets["particle_182 geometry"]
mark=s.place_marker((2147.08, 1643.65, 2998.45), (0.7, 0.7, 0.7), 124.573)
if "particle_183 geometry" not in marker_sets:
  s=new_marker_set('particle_183 geometry')
  marker_sets["particle_183 geometry"]=s
s= marker_sets["particle_183 geometry"]
mark=s.place_marker((2222.32, 1504.96, 3590.68), (0.7, 0.7, 0.7), 124.489)
if "particle_184 geometry" not in marker_sets:
  s=new_marker_set('particle_184 geometry')
  marker_sets["particle_184 geometry"]=s
s= marker_sets["particle_184 geometry"]
mark=s.place_marker((2241.36, 1780.18, 3854.91), (0.7, 0.7, 0.7), 196.61)
if "particle_185 geometry" not in marker_sets:
  s=new_marker_set('particle_185 geometry')
  marker_sets["particle_185 geometry"]=s
s= marker_sets["particle_185 geometry"]
mark=s.place_marker((1922.63, 1775.52, 3726.77), (0.7, 0.7, 0.7), 134.049)
if "particle_186 geometry" not in marker_sets:
  s=new_marker_set('particle_186 geometry')
  marker_sets["particle_186 geometry"]=s
s= marker_sets["particle_186 geometry"]
mark=s.place_marker((1682.46, 1566.94, 3739.28), (0.7, 0.7, 0.7), 141.493)
if "particle_187 geometry" not in marker_sets:
  s=new_marker_set('particle_187 geometry')
  marker_sets["particle_187 geometry"]=s
s= marker_sets["particle_187 geometry"]
mark=s.place_marker((1498.32, 1296.42, 3977.58), (0.7, 0.7, 0.7), 172.203)
if "particle_188 geometry" not in marker_sets:
  s=new_marker_set('particle_188 geometry')
  marker_sets["particle_188 geometry"]=s
s= marker_sets["particle_188 geometry"]
mark=s.place_marker((1746.34, 1876.92, 3838.32), (0.7, 0.7, 0.7), 271.354)
if "particle_189 geometry" not in marker_sets:
  s=new_marker_set('particle_189 geometry')
  marker_sets["particle_189 geometry"]=s
s= marker_sets["particle_189 geometry"]
mark=s.place_marker((2198.96, 2125.61, 3724.66), (0.7, 0.7, 0.7), 97.0785)
if "particle_190 geometry" not in marker_sets:
  s=new_marker_set('particle_190 geometry')
  marker_sets["particle_190 geometry"]=s
s= marker_sets["particle_190 geometry"]
mark=s.place_marker((2637.31, 2158.57, 3694.37), (0.7, 0.7, 0.7), 151.857)
if "particle_191 geometry" not in marker_sets:
  s=new_marker_set('particle_191 geometry')
  marker_sets["particle_191 geometry"]=s
s= marker_sets["particle_191 geometry"]
mark=s.place_marker((3173.01, 2437.91, 3580.33), (0.7, 0.7, 0.7), 199.233)
if "particle_192 geometry" not in marker_sets:
  s=new_marker_set('particle_192 geometry')
  marker_sets["particle_192 geometry"]=s
s= marker_sets["particle_192 geometry"]
mark=s.place_marker((3216.13, 2672.8, 3024.19), (0.7, 0.7, 0.7), 118.863)
if "particle_193 geometry" not in marker_sets:
  s=new_marker_set('particle_193 geometry')
  marker_sets["particle_193 geometry"]=s
s= marker_sets["particle_193 geometry"]
mark=s.place_marker((3573.97, 2732.26, 2726.12), (0.7, 0.7, 0.7), 172.415)
if "particle_194 geometry" not in marker_sets:
  s=new_marker_set('particle_194 geometry')
  marker_sets["particle_194 geometry"]=s
s= marker_sets["particle_194 geometry"]
mark=s.place_marker((4129.67, 2735.34, 2704.68), (0.7, 0.7, 0.7), 134.26)
if "particle_195 geometry" not in marker_sets:
  s=new_marker_set('particle_195 geometry')
  marker_sets["particle_195 geometry"]=s
s= marker_sets["particle_195 geometry"]
mark=s.place_marker((5044.5, 2785.86, 2966.91), (0.7, 0.7, 0.7), 139.548)
if "particle_196 geometry" not in marker_sets:
  s=new_marker_set('particle_196 geometry')
  marker_sets["particle_196 geometry"]=s
s= marker_sets["particle_196 geometry"]
mark=s.place_marker((4975.14, 2283.59, 3128.21), (0.7, 0.7, 0.7), 196.526)
if "particle_197 geometry" not in marker_sets:
  s=new_marker_set('particle_197 geometry')
  marker_sets["particle_197 geometry"]=s
s= marker_sets["particle_197 geometry"]
mark=s.place_marker((4300.42, 1899.72, 3177.94), (0.7, 0.7, 0.7), 136.206)
if "particle_198 geometry" not in marker_sets:
  s=new_marker_set('particle_198 geometry')
  marker_sets["particle_198 geometry"]=s
s= marker_sets["particle_198 geometry"]
mark=s.place_marker((3427.18, 1694.76, 2769.22), (0.7, 0.7, 0.7), 152.322)
if "particle_199 geometry" not in marker_sets:
  s=new_marker_set('particle_199 geometry')
  marker_sets["particle_199 geometry"]=s
s= marker_sets["particle_199 geometry"]
mark=s.place_marker((2804.8, 1718.17, 2561.2), (0.7, 0.7, 0.7), 126.054)
if "particle_200 geometry" not in marker_sets:
  s=new_marker_set('particle_200 geometry')
  marker_sets["particle_200 geometry"]=s
s= marker_sets["particle_200 geometry"]
mark=s.place_marker((2624.49, 1667.25, 2948.14), (0.7, 0.7, 0.7), 164.378)
if "particle_201 geometry" not in marker_sets:
  s=new_marker_set('particle_201 geometry')
  marker_sets["particle_201 geometry"]=s
s= marker_sets["particle_201 geometry"]
mark=s.place_marker((2580.32, 1821.55, 3368.93), (0.7, 0.7, 0.7), 122.205)
if "particle_202 geometry" not in marker_sets:
  s=new_marker_set('particle_202 geometry')
  marker_sets["particle_202 geometry"]=s
s= marker_sets["particle_202 geometry"]
mark=s.place_marker((2559.82, 2137.54, 3676.56), (0.7, 0.7, 0.7), 134.979)
if "particle_203 geometry" not in marker_sets:
  s=new_marker_set('particle_203 geometry')
  marker_sets["particle_203 geometry"]=s
s= marker_sets["particle_203 geometry"]
mark=s.place_marker((2552.72, 2426.7, 3451.89), (0.7, 0.7, 0.7), 136.375)
if "particle_204 geometry" not in marker_sets:
  s=new_marker_set('particle_204 geometry')
  marker_sets["particle_204 geometry"]=s
s= marker_sets["particle_204 geometry"]
mark=s.place_marker((2811.42, 2274.58, 3442.73), (0.7, 0.7, 0.7), 151.688)
if "particle_205 geometry" not in marker_sets:
  s=new_marker_set('particle_205 geometry')
  marker_sets["particle_205 geometry"]=s
s= marker_sets["particle_205 geometry"]
mark=s.place_marker((2641.93, 2207.58, 3649.46), (0.7, 0.7, 0.7), 116.156)
if "particle_206 geometry" not in marker_sets:
  s=new_marker_set('particle_206 geometry')
  marker_sets["particle_206 geometry"]=s
s= marker_sets["particle_206 geometry"]
mark=s.place_marker((2401.32, 2185.13, 2995.07), (0.7, 0.7, 0.7), 122.839)
if "particle_207 geometry" not in marker_sets:
  s=new_marker_set('particle_207 geometry')
  marker_sets["particle_207 geometry"]=s
s= marker_sets["particle_207 geometry"]
mark=s.place_marker((2444.53, 1974.4, 2519.49), (0.7, 0.7, 0.7), 164.716)
if "particle_208 geometry" not in marker_sets:
  s=new_marker_set('particle_208 geometry')
  marker_sets["particle_208 geometry"]=s
s= marker_sets["particle_208 geometry"]
mark=s.place_marker((3154.73, 1661.37, 2941.99), (0.7, 0.7, 0.7), 303.672)
if "particle_209 geometry" not in marker_sets:
  s=new_marker_set('particle_209 geometry')
  marker_sets["particle_209 geometry"]=s
s= marker_sets["particle_209 geometry"]
mark=s.place_marker((3919.47, 1743.65, 3671.33), (0.7, 0.7, 0.7), 220.298)
if "particle_210 geometry" not in marker_sets:
  s=new_marker_set('particle_210 geometry')
  marker_sets["particle_210 geometry"]=s
s= marker_sets["particle_210 geometry"]
mark=s.place_marker((3452.78, 1954.96, 4016.96), (0.7, 0.7, 0.7), 175.883)
if "particle_211 geometry" not in marker_sets:
  s=new_marker_set('particle_211 geometry')
  marker_sets["particle_211 geometry"]=s
s= marker_sets["particle_211 geometry"]
mark=s.place_marker((2860.74, 1775.97, 4247.87), (0.7, 0.7, 0.7), 233.581)
if "particle_212 geometry" not in marker_sets:
  s=new_marker_set('particle_212 geometry')
  marker_sets["particle_212 geometry"]=s
s= marker_sets["particle_212 geometry"]
mark=s.place_marker((2389.85, 1224.29, 4016.98), (0.7, 0.7, 0.7), 231.127)
if "particle_213 geometry" not in marker_sets:
  s=new_marker_set('particle_213 geometry')
  marker_sets["particle_213 geometry"]=s
s= marker_sets["particle_213 geometry"]
mark=s.place_marker((1786.8, 1184.83, 4120.11), (0.7, 0.7, 0.7), 247.413)
if "particle_214 geometry" not in marker_sets:
  s=new_marker_set('particle_214 geometry')
  marker_sets["particle_214 geometry"]=s
s= marker_sets["particle_214 geometry"]
mark=s.place_marker((1268.63, 1506.25, 4355.03), (0.7, 0.7, 0.7), 200.206)
if "particle_215 geometry" not in marker_sets:
  s=new_marker_set('particle_215 geometry')
  marker_sets["particle_215 geometry"]=s
s= marker_sets["particle_215 geometry"]
mark=s.place_marker((1196.85, 1908.57, 4451.43), (0.7, 0.7, 0.7), 150.419)
if "particle_216 geometry" not in marker_sets:
  s=new_marker_set('particle_216 geometry')
  marker_sets["particle_216 geometry"]=s
s= marker_sets["particle_216 geometry"]
mark=s.place_marker((1229.18, 1853.22, 3834.82), (0.7, 0.7, 0.7), 140.14)
if "particle_217 geometry" not in marker_sets:
  s=new_marker_set('particle_217 geometry')
  marker_sets["particle_217 geometry"]=s
s= marker_sets["particle_217 geometry"]
mark=s.place_marker((1111.38, 1605.17, 3464.83), (0.7, 0.7, 0.7), 132.949)
if "particle_218 geometry" not in marker_sets:
  s=new_marker_set('particle_218 geometry')
  marker_sets["particle_218 geometry"]=s
s= marker_sets["particle_218 geometry"]
mark=s.place_marker((1075.04, 1537.52, 3095.57), (0.7, 0.7, 0.7), 141.113)
if "particle_219 geometry" not in marker_sets:
  s=new_marker_set('particle_219 geometry')
  marker_sets["particle_219 geometry"]=s
s= marker_sets["particle_219 geometry"]
mark=s.place_marker((1233.5, 1248.6, 3082.99), (0.7, 0.7, 0.7), 171.526)
if "particle_220 geometry" not in marker_sets:
  s=new_marker_set('particle_220 geometry')
  marker_sets["particle_220 geometry"]=s
s= marker_sets["particle_220 geometry"]
mark=s.place_marker((1505.48, 1088.96, 3575.32), (0.7, 0.7, 0.7), 326.937)
if "particle_221 geometry" not in marker_sets:
  s=new_marker_set('particle_221 geometry')
  marker_sets["particle_221 geometry"]=s
s= marker_sets["particle_221 geometry"]
mark=s.place_marker((1955.63, 1266.06, 3890), (0.7, 0.7, 0.7), 92.0871)
if "particle_222 geometry" not in marker_sets:
  s=new_marker_set('particle_222 geometry')
  marker_sets["particle_222 geometry"]=s
s= marker_sets["particle_222 geometry"]
mark=s.place_marker((2285.57, 1300.41, 3552.27), (0.7, 0.7, 0.7), 210.273)
if "particle_223 geometry" not in marker_sets:
  s=new_marker_set('particle_223 geometry')
  marker_sets["particle_223 geometry"]=s
s= marker_sets["particle_223 geometry"]
mark=s.place_marker((2115.11, 1474.26, 2825.87), (0.7, 0.7, 0.7), 122.628)
if "particle_224 geometry" not in marker_sets:
  s=new_marker_set('particle_224 geometry')
  marker_sets["particle_224 geometry"]=s
s= marker_sets["particle_224 geometry"]
mark=s.place_marker((1968.84, 1506.79, 2618.54), (0.7, 0.7, 0.7), 109.176)
if "particle_225 geometry" not in marker_sets:
  s=new_marker_set('particle_225 geometry')
  marker_sets["particle_225 geometry"]=s
s= marker_sets["particle_225 geometry"]
mark=s.place_marker((1948.89, 1577.99, 2915.36), (0.7, 0.7, 0.7), 142.213)
if "particle_226 geometry" not in marker_sets:
  s=new_marker_set('particle_226 geometry')
  marker_sets["particle_226 geometry"]=s
s= marker_sets["particle_226 geometry"]
mark=s.place_marker((2290.92, 1448.99, 3067.5), (0.7, 0.7, 0.7), 250.078)
if "particle_227 geometry" not in marker_sets:
  s=new_marker_set('particle_227 geometry')
  marker_sets["particle_227 geometry"]=s
s= marker_sets["particle_227 geometry"]
mark=s.place_marker((2307.35, 1900.9, 3130.51), (0.7, 0.7, 0.7), 123.558)
if "particle_228 geometry" not in marker_sets:
  s=new_marker_set('particle_228 geometry')
  marker_sets["particle_228 geometry"]=s
s= marker_sets["particle_228 geometry"]
mark=s.place_marker((2202.6, 2303.09, 2899.63), (0.7, 0.7, 0.7), 235.992)
if "particle_229 geometry" not in marker_sets:
  s=new_marker_set('particle_229 geometry')
  marker_sets["particle_229 geometry"]=s
s= marker_sets["particle_229 geometry"]
mark=s.place_marker((2204.87, 2776.07, 2754.23), (0.7, 0.7, 0.7), 172.373)
if "particle_230 geometry" not in marker_sets:
  s=new_marker_set('particle_230 geometry')
  marker_sets["particle_230 geometry"]=s
s= marker_sets["particle_230 geometry"]
mark=s.place_marker((2375.54, 3069.4, 3053.9), (0.7, 0.7, 0.7), 152.322)
if "particle_231 geometry" not in marker_sets:
  s=new_marker_set('particle_231 geometry')
  marker_sets["particle_231 geometry"]=s
s= marker_sets["particle_231 geometry"]
mark=s.place_marker((2595.42, 3162.42, 3284.02), (0.7, 0.7, 0.7), 196.653)
if "particle_232 geometry" not in marker_sets:
  s=new_marker_set('particle_232 geometry')
  marker_sets["particle_232 geometry"]=s
s= marker_sets["particle_232 geometry"]
mark=s.place_marker((2264.83, 3180.99, 3167.31), (0.7, 0.7, 0.7), 134.091)
if "particle_233 geometry" not in marker_sets:
  s=new_marker_set('particle_233 geometry')
  marker_sets["particle_233 geometry"]=s
s= marker_sets["particle_233 geometry"]
mark=s.place_marker((1977.8, 3190.89, 3010.37), (0.7, 0.7, 0.7), 180.325)
if "particle_234 geometry" not in marker_sets:
  s=new_marker_set('particle_234 geometry')
  marker_sets["particle_234 geometry"]=s
s= marker_sets["particle_234 geometry"]
mark=s.place_marker((2188.16, 2798.24, 2918.82), (0.7, 0.7, 0.7), 218.437)
if "particle_235 geometry" not in marker_sets:
  s=new_marker_set('particle_235 geometry')
  marker_sets["particle_235 geometry"]=s
s= marker_sets["particle_235 geometry"]
mark=s.place_marker((2306.85, 2448.35, 3190.52), (0.7, 0.7, 0.7), 148.008)
if "particle_236 geometry" not in marker_sets:
  s=new_marker_set('particle_236 geometry')
  marker_sets["particle_236 geometry"]=s
s= marker_sets["particle_236 geometry"]
mark=s.place_marker((2346.45, 2235.95, 3786.69), (0.7, 0.7, 0.7), 191.873)
if "particle_237 geometry" not in marker_sets:
  s=new_marker_set('particle_237 geometry')
  marker_sets["particle_237 geometry"]=s
s= marker_sets["particle_237 geometry"]
mark=s.place_marker((2139.39, 1990.31, 4228.6), (0.7, 0.7, 0.7), 138.575)
if "particle_238 geometry" not in marker_sets:
  s=new_marker_set('particle_238 geometry')
  marker_sets["particle_238 geometry"]=s
s= marker_sets["particle_238 geometry"]
mark=s.place_marker((1949.92, 2200.29, 4562.38), (0.7, 0.7, 0.7), 161.205)
if "particle_239 geometry" not in marker_sets:
  s=new_marker_set('particle_239 geometry')
  marker_sets["particle_239 geometry"]=s
s= marker_sets["particle_239 geometry"]
mark=s.place_marker((2320.44, 2262.54, 4304.65), (0.7, 0.7, 0.7), 288.021)
if "particle_240 geometry" not in marker_sets:
  s=new_marker_set('particle_240 geometry')
  marker_sets["particle_240 geometry"]=s
s= marker_sets["particle_240 geometry"]
mark=s.place_marker((2117.75, 2730.73, 3820.06), (0.7, 0.7, 0.7), 227.405)
if "particle_241 geometry" not in marker_sets:
  s=new_marker_set('particle_241 geometry')
  marker_sets["particle_241 geometry"]=s
s= marker_sets["particle_241 geometry"]
mark=s.place_marker((2130.67, 2888.77, 3329.16), (0.7, 0.7, 0.7), 126.519)
if "particle_242 geometry" not in marker_sets:
  s=new_marker_set('particle_242 geometry')
  marker_sets["particle_242 geometry"]=s
s= marker_sets["particle_242 geometry"]
mark=s.place_marker((2383.83, 2960.78, 3488.97), (0.7, 0.7, 0.7), 117.975)
if "particle_243 geometry" not in marker_sets:
  s=new_marker_set('particle_243 geometry')
  marker_sets["particle_243 geometry"]=s
s= marker_sets["particle_243 geometry"]
mark=s.place_marker((2450.76, 2709.58, 3176.85), (0.7, 0.7, 0.7), 200.883)
if "particle_244 geometry" not in marker_sets:
  s=new_marker_set('particle_244 geometry')
  marker_sets["particle_244 geometry"]=s
s= marker_sets["particle_244 geometry"]
mark=s.place_marker((2151.5, 2725.73, 2989.48), (0.7, 0.7, 0.7), 158.794)
if "particle_245 geometry" not in marker_sets:
  s=new_marker_set('particle_245 geometry')
  marker_sets["particle_245 geometry"]=s
s= marker_sets["particle_245 geometry"]
mark=s.place_marker((1840.11, 2664.34, 2994.78), (0.7, 0.7, 0.7), 115.86)
if "particle_246 geometry" not in marker_sets:
  s=new_marker_set('particle_246 geometry')
  marker_sets["particle_246 geometry"]=s
s= marker_sets["particle_246 geometry"]
mark=s.place_marker((1823.44, 2642.6, 2756.15), (0.7, 0.7, 0.7), 133.034)
if "particle_247 geometry" not in marker_sets:
  s=new_marker_set('particle_247 geometry')
  marker_sets["particle_247 geometry"]=s
s= marker_sets["particle_247 geometry"]
mark=s.place_marker((2128.81, 2843.6, 2448.31), (0.7, 0.7, 0.7), 314.627)
if "particle_248 geometry" not in marker_sets:
  s=new_marker_set('particle_248 geometry')
  marker_sets["particle_248 geometry"]=s
s= marker_sets["particle_248 geometry"]
mark=s.place_marker((2217.83, 2876.41, 2805.9), (0.7, 0.7, 0.7), 115.352)
if "particle_249 geometry" not in marker_sets:
  s=new_marker_set('particle_249 geometry')
  marker_sets["particle_249 geometry"]=s
s= marker_sets["particle_249 geometry"]
mark=s.place_marker((2084, 2864.14, 3215.52), (0.7, 0.7, 0.7), 180.621)
if "particle_250 geometry" not in marker_sets:
  s=new_marker_set('particle_250 geometry')
  marker_sets["particle_250 geometry"]=s
s= marker_sets["particle_250 geometry"]
mark=s.place_marker((1734.88, 2742.21, 3237.21), (0.7, 0.7, 0.7), 126.265)
if "particle_251 geometry" not in marker_sets:
  s=new_marker_set('particle_251 geometry')
  marker_sets["particle_251 geometry"]=s
s= marker_sets["particle_251 geometry"]
mark=s.place_marker((1510.42, 2482.03, 3056.57), (0.7, 0.7, 0.7), 133.541)
if "particle_252 geometry" not in marker_sets:
  s=new_marker_set('particle_252 geometry')
  marker_sets["particle_252 geometry"]=s
s= marker_sets["particle_252 geometry"]
mark=s.place_marker((1224.63, 2140.38, 3024.46), (0.7, 0.7, 0.7), 171.019)
if "particle_253 geometry" not in marker_sets:
  s=new_marker_set('particle_253 geometry')
  marker_sets["particle_253 geometry"]=s
s= marker_sets["particle_253 geometry"]
mark=s.place_marker((981.081, 1832.09, 3132.23), (0.7, 0.7, 0.7), 115.437)
if "particle_254 geometry" not in marker_sets:
  s=new_marker_set('particle_254 geometry')
  marker_sets["particle_254 geometry"]=s
s= marker_sets["particle_254 geometry"]
mark=s.place_marker((1006.2, 2138.5, 3153.47), (0.7, 0.7, 0.7), 158.583)
if "particle_255 geometry" not in marker_sets:
  s=new_marker_set('particle_255 geometry')
  marker_sets["particle_255 geometry"]=s
s= marker_sets["particle_255 geometry"]
mark=s.place_marker((1377.74, 2152.8, 2882.39), (0.7, 0.7, 0.7), 192)
if "particle_256 geometry" not in marker_sets:
  s=new_marker_set('particle_256 geometry')
  marker_sets["particle_256 geometry"]=s
s= marker_sets["particle_256 geometry"]
mark=s.place_marker((1701.61, 2368.73, 2654.84), (0.7, 0.7, 0.7), 150.165)
if "particle_257 geometry" not in marker_sets:
  s=new_marker_set('particle_257 geometry')
  marker_sets["particle_257 geometry"]=s
s= marker_sets["particle_257 geometry"]
mark=s.place_marker((1702.18, 2214.86, 2505.09), (0.7, 0.7, 0.7), 157.567)
if "particle_258 geometry" not in marker_sets:
  s=new_marker_set('particle_258 geometry')
  marker_sets["particle_258 geometry"]=s
s= marker_sets["particle_258 geometry"]
mark=s.place_marker((1834.3, 2203.2, 2476.05), (0.7, 0.7, 0.7), 199.36)
if "particle_259 geometry" not in marker_sets:
  s=new_marker_set('particle_259 geometry')
  marker_sets["particle_259 geometry"]=s
s= marker_sets["particle_259 geometry"]
mark=s.place_marker((1957.67, 2059.79, 2902.53), (0.7, 0.7, 0.7), 105.369)
if "particle_260 geometry" not in marker_sets:
  s=new_marker_set('particle_260 geometry')
  marker_sets["particle_260 geometry"]=s
s= marker_sets["particle_260 geometry"]
mark=s.place_marker((2169.42, 1988.12, 3064.36), (0.7, 0.7, 0.7), 118.651)
if "particle_261 geometry" not in marker_sets:
  s=new_marker_set('particle_261 geometry')
  marker_sets["particle_261 geometry"]=s
s= marker_sets["particle_261 geometry"]
mark=s.place_marker((2217.2, 2277.79, 2725.02), (0.7, 0.7, 0.7), 219.664)
if "particle_262 geometry" not in marker_sets:
  s=new_marker_set('particle_262 geometry')
  marker_sets["particle_262 geometry"]=s
s= marker_sets["particle_262 geometry"]
mark=s.place_marker((2100.81, 2528.19, 2202.18), (0.7, 0.7, 0.7), 196.018)
if "particle_263 geometry" not in marker_sets:
  s=new_marker_set('particle_263 geometry')
  marker_sets["particle_263 geometry"]=s
s= marker_sets["particle_263 geometry"]
mark=s.place_marker((2068.19, 2714.24, 1746.65), (0.7, 0.7, 0.7), 218.141)
if "particle_264 geometry" not in marker_sets:
  s=new_marker_set('particle_264 geometry')
  marker_sets["particle_264 geometry"]=s
s= marker_sets["particle_264 geometry"]
mark=s.place_marker((2043.58, 2396.11, 1588.96), (0.7, 0.7, 0.7), 181.636)
if "particle_265 geometry" not in marker_sets:
  s=new_marker_set('particle_265 geometry')
  marker_sets["particle_265 geometry"]=s
s= marker_sets["particle_265 geometry"]
mark=s.place_marker((2061.76, 2177.35, 1797.35), (0.7, 0.7, 0.7), 195.003)
if "particle_266 geometry" not in marker_sets:
  s=new_marker_set('particle_266 geometry')
  marker_sets["particle_266 geometry"]=s
s= marker_sets["particle_266 geometry"]
mark=s.place_marker((1967.49, 2362.08, 1629.64), (0.7, 0.7, 0.7), 139.209)
if "particle_267 geometry" not in marker_sets:
  s=new_marker_set('particle_267 geometry')
  marker_sets["particle_267 geometry"]=s
s= marker_sets["particle_267 geometry"]
mark=s.place_marker((1886.59, 2352.95, 1601.42), (0.7, 0.7, 0.7), 189.885)
if "particle_268 geometry" not in marker_sets:
  s=new_marker_set('particle_268 geometry')
  marker_sets["particle_268 geometry"]=s
s= marker_sets["particle_268 geometry"]
mark=s.place_marker((1741.64, 2503.47, 1786.99), (0.7, 0.7, 0.7), 267.674)
if "particle_269 geometry" not in marker_sets:
  s=new_marker_set('particle_269 geometry')
  marker_sets["particle_269 geometry"]=s
s= marker_sets["particle_269 geometry"]
mark=s.place_marker((1549.83, 2842.76, 2196.67), (0.7, 0.7, 0.7), 196.568)
if "particle_270 geometry" not in marker_sets:
  s=new_marker_set('particle_270 geometry')
  marker_sets["particle_270 geometry"]=s
s= marker_sets["particle_270 geometry"]
mark=s.place_marker((1271.52, 2604.3, 2161.64), (0.7, 0.7, 0.7), 192.423)
if "particle_271 geometry" not in marker_sets:
  s=new_marker_set('particle_271 geometry')
  marker_sets["particle_271 geometry"]=s
s= marker_sets["particle_271 geometry"]
mark=s.place_marker((1293.38, 2478.33, 1795.81), (1, 0.7, 0), 202.405)
if "particle_272 geometry" not in marker_sets:
  s=new_marker_set('particle_272 geometry')
  marker_sets["particle_272 geometry"]=s
s= marker_sets["particle_272 geometry"]
mark=s.place_marker((1146.8, 2773.89, 2580.74), (0.7, 0.7, 0.7), 135.529)
if "particle_273 geometry" not in marker_sets:
  s=new_marker_set('particle_273 geometry')
  marker_sets["particle_273 geometry"]=s
s= marker_sets["particle_273 geometry"]
mark=s.place_marker((858.807, 2964.27, 3475.37), (0.7, 0.7, 0.7), 114.21)
if "particle_274 geometry" not in marker_sets:
  s=new_marker_set('particle_274 geometry')
  marker_sets["particle_274 geometry"]=s
s= marker_sets["particle_274 geometry"]
mark=s.place_marker((1079.33, 2765.47, 3606.17), (0.7, 0.7, 0.7), 159.133)
if "particle_275 geometry" not in marker_sets:
  s=new_marker_set('particle_275 geometry')
  marker_sets["particle_275 geometry"]=s
s= marker_sets["particle_275 geometry"]
mark=s.place_marker((1463.72, 2733.46, 3459.67), (0.7, 0.7, 0.7), 144.412)
if "particle_276 geometry" not in marker_sets:
  s=new_marker_set('particle_276 geometry')
  marker_sets["particle_276 geometry"]=s
s= marker_sets["particle_276 geometry"]
mark=s.place_marker((1757.3, 2740.01, 3328.13), (0.7, 0.7, 0.7), 70.8525)
if "particle_277 geometry" not in marker_sets:
  s=new_marker_set('particle_277 geometry')
  marker_sets["particle_277 geometry"]=s
s= marker_sets["particle_277 geometry"]
mark=s.place_marker((1894.95, 2579.64, 2753.15), (0.7, 0.7, 0.7), 141.874)
if "particle_278 geometry" not in marker_sets:
  s=new_marker_set('particle_278 geometry')
  marker_sets["particle_278 geometry"]=s
s= marker_sets["particle_278 geometry"]
mark=s.place_marker((1912.33, 2440.89, 2153.88), (0.7, 0.7, 0.7), 217.337)
if "particle_279 geometry" not in marker_sets:
  s=new_marker_set('particle_279 geometry')
  marker_sets["particle_279 geometry"]=s
s= marker_sets["particle_279 geometry"]
mark=s.place_marker((1936.06, 2504.78, 2109.51), (0.7, 0.7, 0.7), 237.641)
if "particle_280 geometry" not in marker_sets:
  s=new_marker_set('particle_280 geometry')
  marker_sets["particle_280 geometry"]=s
s= marker_sets["particle_280 geometry"]
mark=s.place_marker((2152.93, 2770.49, 2419.04), (0.7, 0.7, 0.7), 229.393)
if "particle_281 geometry" not in marker_sets:
  s=new_marker_set('particle_281 geometry')
  marker_sets["particle_281 geometry"]=s
s= marker_sets["particle_281 geometry"]
mark=s.place_marker((2258.98, 3099.91, 1920.01), (0.7, 0.7, 0.7), 349.906)
if "particle_282 geometry" not in marker_sets:
  s=new_marker_set('particle_282 geometry')
  marker_sets["particle_282 geometry"]=s
s= marker_sets["particle_282 geometry"]
mark=s.place_marker((1980.32, 3337.05, 1476.77), (0.7, 0.7, 0.7), 162.347)
if "particle_283 geometry" not in marker_sets:
  s=new_marker_set('particle_283 geometry')
  marker_sets["particle_283 geometry"]=s
s= marker_sets["particle_283 geometry"]
mark=s.place_marker((1913.31, 3474.21, 1394.13), (0.7, 0.7, 0.7), 194.072)
if "particle_284 geometry" not in marker_sets:
  s=new_marker_set('particle_284 geometry')
  marker_sets["particle_284 geometry"]=s
s= marker_sets["particle_284 geometry"]
mark=s.place_marker((2004.62, 3617.71, 1460.72), (0.7, 0.7, 0.7), 242.21)
if "particle_285 geometry" not in marker_sets:
  s=new_marker_set('particle_285 geometry')
  marker_sets["particle_285 geometry"]=s
s= marker_sets["particle_285 geometry"]
mark=s.place_marker((1791.89, 4005.96, 1771.01), (0.7, 0.7, 0.7), 320.93)
if "particle_286 geometry" not in marker_sets:
  s=new_marker_set('particle_286 geometry')
  marker_sets["particle_286 geometry"]=s
s= marker_sets["particle_286 geometry"]
mark=s.place_marker((1692.46, 4558, 1581.91), (0.7, 0.7, 0.7), 226.432)
if "particle_287 geometry" not in marker_sets:
  s=new_marker_set('particle_287 geometry')
  marker_sets["particle_287 geometry"]=s
s= marker_sets["particle_287 geometry"]
mark=s.place_marker((1970.67, 4493.45, 1249.28), (0.7, 0.7, 0.7), 125.208)
if "particle_288 geometry" not in marker_sets:
  s=new_marker_set('particle_288 geometry')
  marker_sets["particle_288 geometry"]=s
s= marker_sets["particle_288 geometry"]
mark=s.place_marker((2397, 4163.56, 1099.43), (0.7, 0.7, 0.7), 197.837)
if "particle_289 geometry" not in marker_sets:
  s=new_marker_set('particle_289 geometry')
  marker_sets["particle_289 geometry"]=s
s= marker_sets["particle_289 geometry"]
mark=s.place_marker((3000.65, 4393.24, 1099.67), (0.7, 0.7, 0.7), 167.804)
if "particle_290 geometry" not in marker_sets:
  s=new_marker_set('particle_290 geometry')
  marker_sets["particle_290 geometry"]=s
s= marker_sets["particle_290 geometry"]
mark=s.place_marker((3583.96, 4981.09, 1126.01), (0.7, 0.7, 0.7), 136.84)
if "particle_291 geometry" not in marker_sets:
  s=new_marker_set('particle_291 geometry')
  marker_sets["particle_291 geometry"]=s
s= marker_sets["particle_291 geometry"]
mark=s.place_marker((3457.18, 5192.09, 1521.74), (0.7, 0.7, 0.7), 85.7421)
if "particle_292 geometry" not in marker_sets:
  s=new_marker_set('particle_292 geometry')
  marker_sets["particle_292 geometry"]=s
s= marker_sets["particle_292 geometry"]
mark=s.place_marker((2287.06, 4413.09, 1492.18), (1, 0.7, 0), 256)
if "particle_293 geometry" not in marker_sets:
  s=new_marker_set('particle_293 geometry')
  marker_sets["particle_293 geometry"]=s
s= marker_sets["particle_293 geometry"]
mark=s.place_marker((3347.95, 4454.26, 1116.97), (0.7, 0.7, 0.7), 138.702)
if "particle_294 geometry" not in marker_sets:
  s=new_marker_set('particle_294 geometry')
  marker_sets["particle_294 geometry"]=s
s= marker_sets["particle_294 geometry"]
mark=s.place_marker((3710.35, 4417.83, 806.729), (0.7, 0.7, 0.7), 140.732)
if "particle_295 geometry" not in marker_sets:
  s=new_marker_set('particle_295 geometry')
  marker_sets["particle_295 geometry"]=s
s= marker_sets["particle_295 geometry"]
mark=s.place_marker((3431.74, 4567.17, 808.85), (0.7, 0.7, 0.7), 81.3006)
if "particle_296 geometry" not in marker_sets:
  s=new_marker_set('particle_296 geometry')
  marker_sets["particle_296 geometry"]=s
s= marker_sets["particle_296 geometry"]
mark=s.place_marker((3337.34, 5003.82, 802.028), (0.7, 0.7, 0.7), 133.837)
if "particle_297 geometry" not in marker_sets:
  s=new_marker_set('particle_297 geometry')
  marker_sets["particle_297 geometry"]=s
s= marker_sets["particle_297 geometry"]
mark=s.place_marker((2849.98, 4698.39, 1030.53), (0.7, 0.7, 0.7), 98.3475)
if "particle_298 geometry" not in marker_sets:
  s=new_marker_set('particle_298 geometry')
  marker_sets["particle_298 geometry"]=s
s= marker_sets["particle_298 geometry"]
mark=s.place_marker((2382.16, 4030.28, 1150.06), (0.7, 0.7, 0.7), 297.623)
if "particle_299 geometry" not in marker_sets:
  s=new_marker_set('particle_299 geometry')
  marker_sets["particle_299 geometry"]=s
s= marker_sets["particle_299 geometry"]
mark=s.place_marker((2060.7, 3847.76, 1361.43), (0.7, 0.7, 0.7), 212.938)
if "particle_300 geometry" not in marker_sets:
  s=new_marker_set('particle_300 geometry')
  marker_sets["particle_300 geometry"]=s
s= marker_sets["particle_300 geometry"]
mark=s.place_marker((1944.8, 3894.55, 1166.74), (0.7, 0.7, 0.7), 154.183)
if "particle_301 geometry" not in marker_sets:
  s=new_marker_set('particle_301 geometry')
  marker_sets["particle_301 geometry"]=s
s= marker_sets["particle_301 geometry"]
mark=s.place_marker((1669.56, 4183.04, 1313.98), (0.7, 0.7, 0.7), 180.832)
if "particle_302 geometry" not in marker_sets:
  s=new_marker_set('particle_302 geometry')
  marker_sets["particle_302 geometry"]=s
s= marker_sets["particle_302 geometry"]
mark=s.place_marker((1577.78, 4378.1, 1628.64), (0.7, 0.7, 0.7), 122.332)
if "particle_303 geometry" not in marker_sets:
  s=new_marker_set('particle_303 geometry')
  marker_sets["particle_303 geometry"]=s
s= marker_sets["particle_303 geometry"]
mark=s.place_marker((1619.51, 4499.31, 1979.54), (0.7, 0.7, 0.7), 209.047)
if "particle_304 geometry" not in marker_sets:
  s=new_marker_set('particle_304 geometry')
  marker_sets["particle_304 geometry"]=s
s= marker_sets["particle_304 geometry"]
mark=s.place_marker((1253.05, 4623.97, 1837.72), (0.7, 0.7, 0.7), 126.985)
if "particle_305 geometry" not in marker_sets:
  s=new_marker_set('particle_305 geometry')
  marker_sets["particle_305 geometry"]=s
s= marker_sets["particle_305 geometry"]
mark=s.place_marker((1090.13, 4996.95, 1742.97), (0.7, 0.7, 0.7), 122.205)
if "particle_306 geometry" not in marker_sets:
  s=new_marker_set('particle_306 geometry')
  marker_sets["particle_306 geometry"]=s
s= marker_sets["particle_306 geometry"]
mark=s.place_marker((1178.35, 5167.17, 1553.09), (0.7, 0.7, 0.7), 107.95)
if "particle_307 geometry" not in marker_sets:
  s=new_marker_set('particle_307 geometry')
  marker_sets["particle_307 geometry"]=s
s= marker_sets["particle_307 geometry"]
mark=s.place_marker((1335.34, 4584.64, 1460.96), (0.7, 0.7, 0.7), 182.567)
if "particle_308 geometry" not in marker_sets:
  s=new_marker_set('particle_308 geometry')
  marker_sets["particle_308 geometry"]=s
s= marker_sets["particle_308 geometry"]
mark=s.place_marker((1674.86, 4040.7, 1442.45), (0.7, 0.7, 0.7), 185.274)
if "particle_309 geometry" not in marker_sets:
  s=new_marker_set('particle_309 geometry')
  marker_sets["particle_309 geometry"]=s
s= marker_sets["particle_309 geometry"]
mark=s.place_marker((1995.73, 3774.66, 1675.89), (0.7, 0.7, 0.7), 413.567)
if "particle_310 geometry" not in marker_sets:
  s=new_marker_set('particle_310 geometry')
  marker_sets["particle_310 geometry"]=s
s= marker_sets["particle_310 geometry"]
mark=s.place_marker((1994.57, 3582.68, 1548.38), (0.7, 0.7, 0.7), 240.01)
if "particle_311 geometry" not in marker_sets:
  s=new_marker_set('particle_311 geometry')
  marker_sets["particle_311 geometry"]=s
s= marker_sets["particle_311 geometry"]
mark=s.place_marker((1984.19, 3606.82, 1585.94), (0.7, 0.7, 0.7), 238.995)
if "particle_312 geometry" not in marker_sets:
  s=new_marker_set('particle_312 geometry')
  marker_sets["particle_312 geometry"]=s
s= marker_sets["particle_312 geometry"]
mark=s.place_marker((1812.59, 3741.41, 1403.66), (0.7, 0.7, 0.7), 203.674)
if "particle_313 geometry" not in marker_sets:
  s=new_marker_set('particle_313 geometry')
  marker_sets["particle_313 geometry"]=s
s= marker_sets["particle_313 geometry"]
mark=s.place_marker((1226.52, 3882.48, 1348.45), (0.7, 0.7, 0.7), 266.744)
if "particle_314 geometry" not in marker_sets:
  s=new_marker_set('particle_314 geometry')
  marker_sets["particle_314 geometry"]=s
s= marker_sets["particle_314 geometry"]
mark=s.place_marker((1347.92, 3950.9, 914.517), (0.7, 0.7, 0.7), 147.585)
if "particle_315 geometry" not in marker_sets:
  s=new_marker_set('particle_315 geometry')
  marker_sets["particle_315 geometry"]=s
s= marker_sets["particle_315 geometry"]
mark=s.place_marker((1534.78, 3805.82, 1060.85), (0.7, 0.7, 0.7), 249.485)
if "particle_316 geometry" not in marker_sets:
  s=new_marker_set('particle_316 geometry')
  marker_sets["particle_316 geometry"]=s
s= marker_sets["particle_316 geometry"]
mark=s.place_marker((1494.04, 3713.05, 1468.86), (0.7, 0.7, 0.7), 119.371)
if "particle_317 geometry" not in marker_sets:
  s=new_marker_set('particle_317 geometry')
  marker_sets["particle_317 geometry"]=s
s= marker_sets["particle_317 geometry"]
mark=s.place_marker((1500.01, 4033.14, 2102.78), (0.7, 0.7, 0.7), 155.875)
if "particle_318 geometry" not in marker_sets:
  s=new_marker_set('particle_318 geometry')
  marker_sets["particle_318 geometry"]=s
s= marker_sets["particle_318 geometry"]
mark=s.place_marker((1937.35, 4484.02, 2548.59), (0.7, 0.7, 0.7), 189.419)
if "particle_319 geometry" not in marker_sets:
  s=new_marker_set('particle_319 geometry')
  marker_sets["particle_319 geometry"]=s
s= marker_sets["particle_319 geometry"]
mark=s.place_marker((2490.57, 4381.17, 2527.47), (0.7, 0.7, 0.7), 137.475)
if "particle_320 geometry" not in marker_sets:
  s=new_marker_set('particle_320 geometry')
  marker_sets["particle_320 geometry"]=s
s= marker_sets["particle_320 geometry"]
mark=s.place_marker((2887.11, 4077.87, 2380.54), (0.7, 0.7, 0.7), 176.179)
if "particle_321 geometry" not in marker_sets:
  s=new_marker_set('particle_321 geometry')
  marker_sets["particle_321 geometry"]=s
s= marker_sets["particle_321 geometry"]
mark=s.place_marker((3322.93, 3938.83, 2226.78), (0.7, 0.7, 0.7), 138.829)
if "particle_322 geometry" not in marker_sets:
  s=new_marker_set('particle_322 geometry')
  marker_sets["particle_322 geometry"]=s
s= marker_sets["particle_322 geometry"]
mark=s.place_marker((3712.81, 3958.01, 2037.21), (0.7, 0.7, 0.7), 148.727)
if "particle_323 geometry" not in marker_sets:
  s=new_marker_set('particle_323 geometry')
  marker_sets["particle_323 geometry"]=s
s= marker_sets["particle_323 geometry"]
mark=s.place_marker((4165, 4188.24, 1873.86), (0.7, 0.7, 0.7), 230.323)
if "particle_324 geometry" not in marker_sets:
  s=new_marker_set('particle_324 geometry')
  marker_sets["particle_324 geometry"]=s
s= marker_sets["particle_324 geometry"]
mark=s.place_marker((3549.09, 4273.17, 1983.57), (0.7, 0.7, 0.7), 175.376)
if "particle_325 geometry" not in marker_sets:
  s=new_marker_set('particle_325 geometry')
  marker_sets["particle_325 geometry"]=s
s= marker_sets["particle_325 geometry"]
mark=s.place_marker((3070.92, 4142.75, 2073.2), (0.7, 0.7, 0.7), 161.163)
if "particle_326 geometry" not in marker_sets:
  s=new_marker_set('particle_326 geometry')
  marker_sets["particle_326 geometry"]=s
s= marker_sets["particle_326 geometry"]
mark=s.place_marker((3198.64, 4089.91, 2533.24), (0.7, 0.7, 0.7), 125.885)
if "particle_327 geometry" not in marker_sets:
  s=new_marker_set('particle_327 geometry')
  marker_sets["particle_327 geometry"]=s
s= marker_sets["particle_327 geometry"]
mark=s.place_marker((3280.05, 4222.39, 2965.19), (0.7, 0.7, 0.7), 206.635)
if "particle_328 geometry" not in marker_sets:
  s=new_marker_set('particle_328 geometry')
  marker_sets["particle_328 geometry"]=s
s= marker_sets["particle_328 geometry"]
mark=s.place_marker((3284.11, 3801.26, 2800.67), (0.7, 0.7, 0.7), 151.392)
if "particle_329 geometry" not in marker_sets:
  s=new_marker_set('particle_329 geometry')
  marker_sets["particle_329 geometry"]=s
s= marker_sets["particle_329 geometry"]
mark=s.place_marker((3364.05, 3529.29, 2575), (0.7, 0.7, 0.7), 173.388)
if "particle_330 geometry" not in marker_sets:
  s=new_marker_set('particle_330 geometry')
  marker_sets["particle_330 geometry"]=s
s= marker_sets["particle_330 geometry"]
mark=s.place_marker((3609.98, 3671.74, 2413.1), (0.7, 0.7, 0.7), 135.825)
if "particle_331 geometry" not in marker_sets:
  s=new_marker_set('particle_331 geometry')
  marker_sets["particle_331 geometry"]=s
s= marker_sets["particle_331 geometry"]
mark=s.place_marker((3899.28, 3969.43, 2305.06), (0.7, 0.7, 0.7), 186.839)
if "particle_332 geometry" not in marker_sets:
  s=new_marker_set('particle_332 geometry')
  marker_sets["particle_332 geometry"]=s
s= marker_sets["particle_332 geometry"]
mark=s.place_marker((4193.14, 4324.18, 2213.01), (0.7, 0.7, 0.7), 121.189)
if "particle_333 geometry" not in marker_sets:
  s=new_marker_set('particle_333 geometry')
  marker_sets["particle_333 geometry"]=s
s= marker_sets["particle_333 geometry"]
mark=s.place_marker((3776.61, 4249.15, 2284.42), (0.7, 0.7, 0.7), 102.916)
if "particle_334 geometry" not in marker_sets:
  s=new_marker_set('particle_334 geometry')
  marker_sets["particle_334 geometry"]=s
s= marker_sets["particle_334 geometry"]
mark=s.place_marker((3162.92, 4135.3, 2245.42), (0.7, 0.7, 0.7), 212.769)
if "particle_335 geometry" not in marker_sets:
  s=new_marker_set('particle_335 geometry')
  marker_sets["particle_335 geometry"]=s
s= marker_sets["particle_335 geometry"]
mark=s.place_marker((2597.88, 3771.78, 2220.57), (0.7, 0.7, 0.7), 173.092)
if "particle_336 geometry" not in marker_sets:
  s=new_marker_set('particle_336 geometry')
  marker_sets["particle_336 geometry"]=s
s= marker_sets["particle_336 geometry"]
mark=s.place_marker((2089.66, 3739.11, 2256.69), (0.7, 0.7, 0.7), 264.502)
if "particle_337 geometry" not in marker_sets:
  s=new_marker_set('particle_337 geometry')
  marker_sets["particle_337 geometry"]=s
s= marker_sets["particle_337 geometry"]
mark=s.place_marker((1660.65, 4088.15, 2366.63), (0.7, 0.7, 0.7), 208.666)
if "particle_338 geometry" not in marker_sets:
  s=new_marker_set('particle_338 geometry')
  marker_sets["particle_338 geometry"]=s
s= marker_sets["particle_338 geometry"]
mark=s.place_marker((1369.29, 4475.43, 2227.26), (0.7, 0.7, 0.7), 186.797)
if "particle_339 geometry" not in marker_sets:
  s=new_marker_set('particle_339 geometry')
  marker_sets["particle_339 geometry"]=s
s= marker_sets["particle_339 geometry"]
mark=s.place_marker((1086.33, 4388.49, 1808.16), (0.7, 0.7, 0.7), 255.534)
if "particle_340 geometry" not in marker_sets:
  s=new_marker_set('particle_340 geometry')
  marker_sets["particle_340 geometry"]=s
s= marker_sets["particle_340 geometry"]
mark=s.place_marker((1147.59, 4594, 1432.32), (0.7, 0.7, 0.7), 153.126)
if "particle_341 geometry" not in marker_sets:
  s=new_marker_set('particle_341 geometry')
  marker_sets["particle_341 geometry"]=s
s= marker_sets["particle_341 geometry"]
mark=s.place_marker((979.163, 4867.55, 1661.9), (0.7, 0.7, 0.7), 165.816)
if "particle_342 geometry" not in marker_sets:
  s=new_marker_set('particle_342 geometry')
  marker_sets["particle_342 geometry"]=s
s= marker_sets["particle_342 geometry"]
mark=s.place_marker((854.475, 4538.15, 1829.86), (0.7, 0.7, 0.7), 134.429)
if "particle_343 geometry" not in marker_sets:
  s=new_marker_set('particle_343 geometry')
  marker_sets["particle_343 geometry"]=s
s= marker_sets["particle_343 geometry"]
mark=s.place_marker((1085.76, 4338.51, 2072.6), (0.7, 0.7, 0.7), 178.971)
if "particle_344 geometry" not in marker_sets:
  s=new_marker_set('particle_344 geometry')
  marker_sets["particle_344 geometry"]=s
s= marker_sets["particle_344 geometry"]
mark=s.place_marker((1544.4, 4484.16, 2290.99), (0.7, 0.7, 0.7), 189.969)
if "particle_345 geometry" not in marker_sets:
  s=new_marker_set('particle_345 geometry')
  marker_sets["particle_345 geometry"]=s
s= marker_sets["particle_345 geometry"]
mark=s.place_marker((1764.38, 4951.72, 2677.48), (0.7, 0.7, 0.7), 121.359)
if "particle_346 geometry" not in marker_sets:
  s=new_marker_set('particle_346 geometry')
  marker_sets["particle_346 geometry"]=s
s= marker_sets["particle_346 geometry"]
mark=s.place_marker((2310.31, 4931.61, 2819.4), (0.7, 0.7, 0.7), 187.262)
if "particle_347 geometry" not in marker_sets:
  s=new_marker_set('particle_347 geometry')
  marker_sets["particle_347 geometry"]=s
s= marker_sets["particle_347 geometry"]
mark=s.place_marker((2797.79, 4470.88, 2793.8), (0.7, 0.7, 0.7), 164.335)
if "particle_348 geometry" not in marker_sets:
  s=new_marker_set('particle_348 geometry')
  marker_sets["particle_348 geometry"]=s
s= marker_sets["particle_348 geometry"]
mark=s.place_marker((3142.05, 4370.7, 2421.14), (0.7, 0.7, 0.7), 138.363)
if "particle_349 geometry" not in marker_sets:
  s=new_marker_set('particle_349 geometry')
  marker_sets["particle_349 geometry"]=s
s= marker_sets["particle_349 geometry"]
mark=s.place_marker((3492.59, 4356.98, 2271.92), (0.7, 0.7, 0.7), 138.49)
if "particle_350 geometry" not in marker_sets:
  s=new_marker_set('particle_350 geometry')
  marker_sets["particle_350 geometry"]=s
s= marker_sets["particle_350 geometry"]
mark=s.place_marker((3573.84, 4125.49, 2526.19), (0.7, 0.7, 0.7), 116.325)
if "particle_351 geometry" not in marker_sets:
  s=new_marker_set('particle_351 geometry')
  marker_sets["particle_351 geometry"]=s
s= marker_sets["particle_351 geometry"]
mark=s.place_marker((3144.85, 4072.69, 2709.39), (0.7, 0.7, 0.7), 106.511)
if "particle_352 geometry" not in marker_sets:
  s=new_marker_set('particle_352 geometry')
  marker_sets["particle_352 geometry"]=s
s= marker_sets["particle_352 geometry"]
mark=s.place_marker((2600.35, 4163.27, 2642.19), (0.7, 0.7, 0.7), 151.096)
if "particle_353 geometry" not in marker_sets:
  s=new_marker_set('particle_353 geometry')
  marker_sets["particle_353 geometry"]=s
s= marker_sets["particle_353 geometry"]
mark=s.place_marker((2006.56, 4485.8, 2534.11), (0.7, 0.7, 0.7), 240.856)
if "particle_354 geometry" not in marker_sets:
  s=new_marker_set('particle_354 geometry')
  marker_sets["particle_354 geometry"]=s
s= marker_sets["particle_354 geometry"]
mark=s.place_marker((1586.62, 4771.19, 2365.25), (0.7, 0.7, 0.7), 149.7)
if "particle_355 geometry" not in marker_sets:
  s=new_marker_set('particle_355 geometry')
  marker_sets["particle_355 geometry"]=s
s= marker_sets["particle_355 geometry"]
mark=s.place_marker((1253.56, 4697.61, 2235.33), (0.7, 0.7, 0.7), 165.943)
if "particle_356 geometry" not in marker_sets:
  s=new_marker_set('particle_356 geometry')
  marker_sets["particle_356 geometry"]=s
s= marker_sets["particle_356 geometry"]
mark=s.place_marker((1254.23, 4166.34, 1906.73), (0.7, 0.7, 0.7), 178.971)
if "particle_357 geometry" not in marker_sets:
  s=new_marker_set('particle_357 geometry')
  marker_sets["particle_357 geometry"]=s
s= marker_sets["particle_357 geometry"]
mark=s.place_marker((1018.53, 3507.7, 1597.48), (0.7, 0.7, 0.7), 154.945)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
