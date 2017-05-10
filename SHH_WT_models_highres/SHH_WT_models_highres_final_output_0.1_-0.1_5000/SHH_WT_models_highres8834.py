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
mark=s.place_marker((202.111, 673.057, 3536.85), (0.7, 0.7, 0.7), 182.271)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((157.079, 810.748, 3965.9), (0.7, 0.7, 0.7), 258.199)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((484.987, 908.853, 3794.14), (0.7, 0.7, 0.7), 123.897)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((456.188, 550.879, 3992.71), (0.7, 0.7, 0.7), 146.739)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((540.384, 168.282, 4240.07), (0.7, 0.7, 0.7), 179.098)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((938.931, 561.785, 4061.23), (0.7, 0.7, 0.7), 148.854)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((1347.19, 832.561, 3889.32), (0.7, 0.7, 0.7), 196.357)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((1356.03, 305.971, 3832.72), (0.7, 0.7, 0.7), 166.873)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((1421.89, -249.339, 3841.31), (0.7, 0.7, 0.7), 95.4711)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((1594.26, 137.287, 3880.62), (0.7, 0.7, 0.7), 185.401)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((1590.88, 641.173, 4010.03), (0.7, 0.7, 0.7), 151.984)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((1545, 1278.28, 4086.01), (0.7, 0.7, 0.7), 185.612)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((1520.89, 1636.02, 4449.94), (0.7, 0.7, 0.7), 210.273)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((1579.47, 1911.11, 4793.22), (0.7, 0.7, 0.7), 106.892)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((1676.99, 2345.02, 5145.89), (0.7, 0.7, 0.7), 202.025)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((1503.92, 2930.82, 5400.4), (0.7, 0.7, 0.7), 192.169)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((1199.44, 3463.15, 5541.24), (0.7, 0.7, 0.7), 241.11)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((822.875, 3648.79, 5447.38), (0.7, 0.7, 0.7), 128.465)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((342.568, 3663.4, 5529.42), (0.7, 0.7, 0.7), 217.38)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((-283.531, 3746.03, 5867.93), (0.7, 0.7, 0.7), 184.555)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((154.588, 3637.98, 5403.2), (0.7, 0.7, 0.7), 140.055)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((605.414, 3702.59, 5338.04), (0.7, 0.7, 0.7), 169.708)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((932.457, 3978.83, 5402.52), (0.7, 0.7, 0.7), 184.639)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((1077.06, 4076.67, 5128.67), (0.7, 0.7, 0.7), 119.286)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((792.397, 4129.25, 5031.96), (0.7, 0.7, 0.7), 147.754)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((564.833, 3868.04, 5024.62), (0.7, 0.7, 0.7), 171.4)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((788.696, 3505.19, 4981.85), (0.7, 0.7, 0.7), 156.341)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((918.66, 3134.79, 4537.93), (0.7, 0.7, 0.7), 186.501)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((1102.65, 2845.19, 4104.56), (0.7, 0.7, 0.7), 308.325)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((1328.84, 2467.49, 4001.54), (0.7, 0.7, 0.7), 138.617)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((1598.68, 2324.35, 3957.38), (0.7, 0.7, 0.7), 130.03)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((1476.45, 2551.16, 4146.42), (0.7, 0.7, 0.7), 156.552)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((1198.53, 2512.01, 4037.12), (0.7, 0.7, 0.7), 183.244)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((947.78, 2499.31, 3937.87), (0.7, 0.7, 0.7), 181.382)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((840.889, 2644.94, 3842.8), (0.7, 0.7, 0.7), 101.943)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((504.49, 2770.08, 3883.59), (1, 0.7, 0), 138.913)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((428.887, 1703.95, 3936.1), (0.7, 0.7, 0.7), 221.737)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((270.365, 906.545, 3695.03), (0.7, 0.7, 0.7), 256.38)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((410.674, 598.788, 3146.69), (0.7, 0.7, 0.7), 221.694)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((1007.86, 839.989, 2898.38), (0.7, 0.7, 0.7), 259.341)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((1573.39, 1382.59, 3102.81), (0.7, 0.7, 0.7), 117.89)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((1752.27, 2131.1, 3473.84), (0.7, 0.7, 0.7), 116.071)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((1508.59, 2548.43, 3381.99), (0.7, 0.7, 0.7), 268.224)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((1405.17, 2425.38, 3105.59), (0.7, 0.7, 0.7), 386.918)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((1591.41, 1925.95, 2789.63), (0.7, 0.7, 0.7), 121.316)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((1435.67, 1731.5, 2407.03), (0.7, 0.7, 0.7), 138.363)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((1008.05, 2194.88, 2737.37), (1, 0.7, 0), 175.207)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((943.802, 1813.58, 2132.3), (0.7, 0.7, 0.7), 131.468)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((714.878, 1581.95, 1474.96), (0.7, 0.7, 0.7), 287.894)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((1002.39, 2022.9, 1579.33), (0.7, 0.7, 0.7), 88.1109)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((1283.97, 2279.59, 2051.76), (0.7, 0.7, 0.7), 145.385)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((1503.65, 2327.31, 2163.48), (0.7, 0.7, 0.7), 155.452)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((1492.28, 2183.61, 1545.39), (0.7, 0.7, 0.7), 145.512)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((1606.47, 2031.53, 1066.34), (0.7, 0.7, 0.7), 99.9972)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((1579.15, 1846.11, 665.044), (0.7, 0.7, 0.7), 327.529)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((2047.63, 1853.67, 1090.73), (0.7, 0.7, 0.7), 137.983)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((2132.03, 2090.77, 1526.61), (0.7, 0.7, 0.7), 83.3733)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((2104.41, 2387.8, 2011.78), (0.7, 0.7, 0.7), 101.562)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((1949.18, 2610.11, 2463.09), (0.7, 0.7, 0.7), 165.689)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((1673.4, 2724.26, 2369.77), (0.7, 0.7, 0.7), 136.925)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((1568.25, 2750.4, 2300.76), (0.7, 0.7, 0.7), 123.389)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((1799.21, 2683.17, 1918.56), (0.7, 0.7, 0.7), 184.47)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((2145.34, 2685.95, 1200.49), (0.7, 0.7, 0.7), 148.473)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((2503.16, 2747.98, 280.121), (0.7, 0.7, 0.7), 241.406)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((2538.13, 2338.93, 800.116), (0.7, 0.7, 0.7), 182.736)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((2373.86, 2115.94, 1172.16), (0.7, 0.7, 0.7), 166.62)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((2117.53, 2176.18, 1288.77), (0.7, 0.7, 0.7), 113.872)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((2001.82, 2332.41, 1537.17), (0.7, 0.7, 0.7), 110.065)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((1655.42, 2368.72, 1677.78), (0.7, 0.7, 0.7), 150.08)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((1186.03, 2362.58, 1733.46), (0.7, 0.7, 0.7), 118.525)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((667.834, 2489.61, 1638.24), (0.7, 0.7, 0.7), 163.955)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((601.565, 2734.73, 1316.4), (0.7, 0.7, 0.7), 170.131)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((1217.16, 2702.8, 867.116), (0.7, 0.7, 0.7), 78.2127)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((1875.08, 2590.02, 459.491), (0.7, 0.7, 0.7), 251.896)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((2482.1, 2397.81, 278.69), (0.7, 0.7, 0.7), 167.55)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((2831.33, 2188.02, 358.465), (0.7, 0.7, 0.7), 167.846)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((2813.86, 2678.48, 200.859), (0.7, 0.7, 0.7), 259.68)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((2410.9, 2984.75, 77.2091), (0.7, 0.7, 0.7), 80.2854)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((2410.88, 2850.09, -128.9), (0.7, 0.7, 0.7), 82.4427)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((2511.94, 3207.09, -368.092), (0.7, 0.7, 0.7), 212.811)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((2928.65, 3563.5, 171.545), (0.7, 0.7, 0.7), 176.391)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((2930.49, 3550.41, 900.084), (0.7, 0.7, 0.7), 99.3204)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((2590.05, 3538.93, 1396.25), (0.7, 0.7, 0.7), 166.62)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((2457.22, 3727.4, 1622.38), (0.7, 0.7, 0.7), 102.831)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((2860.3, 4019.17, 906.821), (0.7, 0.7, 0.7), 65.0997)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((2817.16, 3502.44, 763.868), (0.7, 0.7, 0.7), 92.1294)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((2634.72, 2962.71, 940.971), (0.7, 0.7, 0.7), 194.791)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((2630.31, 2520.11, 1070.96), (0.7, 0.7, 0.7), 120.766)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((3038.49, 2427.98, 663.302), (0.7, 0.7, 0.7), 217.803)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((2715.65, 2603.19, 559.756), (0.7, 0.7, 0.7), 115.775)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((2306.63, 2621.98, 651.88), (0.7, 0.7, 0.7), 115.648)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((2302.27, 2563.77, 977.124), (0.7, 0.7, 0.7), 83.8386)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((2536.35, 2298.15, 1105.9), (0.7, 0.7, 0.7), 124.32)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((2633.46, 1862.42, 1199.03), (0.7, 0.7, 0.7), 185.993)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((2540.08, 1285.9, 942.352), (0.7, 0.7, 0.7), 238.826)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((2245.97, 1041.1, 549.969), (0.7, 0.7, 0.7), 128.465)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((1938.01, 1590.23, 569.626), (0.7, 0.7, 0.7), 203.209)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((2055.53, 1995.71, 832.132), (0.7, 0.7, 0.7), 160.486)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((2337.09, 1800.54, 863.23), (0.7, 0.7, 0.7), 149.277)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((2380.62, 1661.81, 337.287), (0.7, 0.7, 0.7), 35.7435)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((2021.57, 2313.2, 987.962), (0.7, 0.7, 0.7), 98.3898)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((1833.03, 2915.14, 1823.01), (0.7, 0.7, 0.7), 188.404)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((2067.07, 3027.45, 2264.78), (0.7, 0.7, 0.7), 110.318)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((2289.47, 2983.31, 1952.64), (0.7, 0.7, 0.7), 127.534)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((2359.71, 2834.44, 1609.47), (0.7, 0.7, 0.7), 91.368)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((2340.4, 2604.84, 1286.83), (0.7, 0.7, 0.7), 131.045)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((2173.35, 2277.88, 1090.29), (0.7, 0.7, 0.7), 143.608)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((2322.24, 1922.42, 1096.89), (0.7, 0.7, 0.7), 135.783)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((2487.51, 1636.91, 1124.06), (0.7, 0.7, 0.7), 92.5947)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((2665.25, 1732.78, 1312.67), (0.7, 0.7, 0.7), 150.123)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((2789.89, 1946.32, 1402.15), (0.7, 0.7, 0.7), 121.57)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((3100.42, 1872.3, 1324.75), (0.7, 0.7, 0.7), 104.777)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((3081.99, 2074.7, 1692.18), (0.7, 0.7, 0.7), 114.844)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((3059.07, 2286.34, 2092.32), (0.7, 0.7, 0.7), 150.588)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((2775.19, 2605.83, 2136.44), (0.7, 0.7, 0.7), 103.55)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((2621.22, 3120.5, 1945.96), (0.7, 0.7, 0.7), 215.392)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((2466.74, 3675.27, 1910.85), (0.7, 0.7, 0.7), 99.9126)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((2673.73, 4210.31, 1534.03), (0.7, 0.7, 0.7), 99.7857)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((2760.59, 4481.91, 1066.54), (0.7, 0.7, 0.7), 109.98)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((2910.26, 4069.92, 1328.84), (0.7, 0.7, 0.7), 102.831)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((2825.44, 3674.36, 1439.38), (0.7, 0.7, 0.7), 103.593)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((2733.57, 3167.13, 1433.89), (0.7, 0.7, 0.7), 173.472)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((2683.57, 2729.39, 1050.22), (0.7, 0.7, 0.7), 113.575)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((2609.39, 2224.76, 1063.7), (0.7, 0.7, 0.7), 128.296)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((2623.49, 1743.9, 1072.34), (0.7, 0.7, 0.7), 145.004)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((2625.7, 1242.62, 1299.85), (0.7, 0.7, 0.7), 148.261)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((2621.18, 600.977, 1208.98), (0.7, 0.7, 0.7), 127.704)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((2472.73, 77.5623, 979.984), (0.7, 0.7, 0.7), 129.607)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((2292.13, 466.363, 748.764), (0.7, 0.7, 0.7), 139.759)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((2088.43, 1084.18, 711.291), (0.7, 0.7, 0.7), 118.567)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((2328.4, 1432.14, 644.277), (0.7, 0.7, 0.7), 136.164)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((2532, 1808.83, 802.87), (0.7, 0.7, 0.7), 121.655)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((2815.47, 2070.49, 1011.69), (0.7, 0.7, 0.7), 127.492)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((3210.64, 2235.18, 920.261), (0.7, 0.7, 0.7), 138.617)
if "particle_134 geometry" not in marker_sets:
  s=new_marker_set('particle_134 geometry')
  marker_sets["particle_134 geometry"]=s
s= marker_sets["particle_134 geometry"]
mark=s.place_marker((3416.75, 2421, 1180.94), (0.7, 0.7, 0.7), 120.766)
if "particle_135 geometry" not in marker_sets:
  s=new_marker_set('particle_135 geometry')
  marker_sets["particle_135 geometry"]=s
s= marker_sets["particle_135 geometry"]
mark=s.place_marker((3362.78, 2699.1, 1351.51), (0.7, 0.7, 0.7), 145.893)
if "particle_136 geometry" not in marker_sets:
  s=new_marker_set('particle_136 geometry')
  marker_sets["particle_136 geometry"]=s
s= marker_sets["particle_136 geometry"]
mark=s.place_marker((2917.29, 2721.55, 1513.72), (0.7, 0.7, 0.7), 185.02)
if "particle_137 geometry" not in marker_sets:
  s=new_marker_set('particle_137 geometry')
  marker_sets["particle_137 geometry"]=s
s= marker_sets["particle_137 geometry"]
mark=s.place_marker((2560.35, 2741.97, 1909.58), (0.7, 0.7, 0.7), 221.314)
if "particle_138 geometry" not in marker_sets:
  s=new_marker_set('particle_138 geometry')
  marker_sets["particle_138 geometry"]=s
s= marker_sets["particle_138 geometry"]
mark=s.place_marker((2405.57, 2622.05, 2361.94), (0.7, 0.7, 0.7), 165.139)
if "particle_139 geometry" not in marker_sets:
  s=new_marker_set('particle_139 geometry')
  marker_sets["particle_139 geometry"]=s
s= marker_sets["particle_139 geometry"]
mark=s.place_marker((2228.91, 2724.14, 2257.27), (0.7, 0.7, 0.7), 179.437)
if "particle_140 geometry" not in marker_sets:
  s=new_marker_set('particle_140 geometry')
  marker_sets["particle_140 geometry"]=s
s= marker_sets["particle_140 geometry"]
mark=s.place_marker((2240.25, 3007.72, 1962.97), (0.7, 0.7, 0.7), 137.898)
if "particle_141 geometry" not in marker_sets:
  s=new_marker_set('particle_141 geometry')
  marker_sets["particle_141 geometry"]=s
s= marker_sets["particle_141 geometry"]
mark=s.place_marker((2353.61, 3098.51, 1670.94), (0.7, 0.7, 0.7), 124.658)
if "particle_142 geometry" not in marker_sets:
  s=new_marker_set('particle_142 geometry')
  marker_sets["particle_142 geometry"]=s
s= marker_sets["particle_142 geometry"]
mark=s.place_marker((2668.88, 3047.29, 1523.19), (0.7, 0.7, 0.7), 97.7553)
if "particle_143 geometry" not in marker_sets:
  s=new_marker_set('particle_143 geometry')
  marker_sets["particle_143 geometry"]=s
s= marker_sets["particle_143 geometry"]
mark=s.place_marker((2930.89, 3050.26, 1359.8), (0.7, 0.7, 0.7), 92.9331)
if "particle_144 geometry" not in marker_sets:
  s=new_marker_set('particle_144 geometry')
  marker_sets["particle_144 geometry"]=s
s= marker_sets["particle_144 geometry"]
mark=s.place_marker((3125.86, 3106.31, 1090.99), (0.7, 0.7, 0.7), 123.135)
if "particle_145 geometry" not in marker_sets:
  s=new_marker_set('particle_145 geometry')
  marker_sets["particle_145 geometry"]=s
s= marker_sets["particle_145 geometry"]
mark=s.place_marker((2848.01, 3099.28, 1369.93), (0.7, 0.7, 0.7), 125.716)
if "particle_146 geometry" not in marker_sets:
  s=new_marker_set('particle_146 geometry')
  marker_sets["particle_146 geometry"]=s
s= marker_sets["particle_146 geometry"]
mark=s.place_marker((2706.58, 2896.48, 1584.01), (0.7, 0.7, 0.7), 127.534)
if "particle_147 geometry" not in marker_sets:
  s=new_marker_set('particle_147 geometry')
  marker_sets["particle_147 geometry"]=s
s= marker_sets["particle_147 geometry"]
mark=s.place_marker((2641.73, 2605.75, 1516.15), (0.7, 0.7, 0.7), 94.9212)
if "particle_148 geometry" not in marker_sets:
  s=new_marker_set('particle_148 geometry')
  marker_sets["particle_148 geometry"]=s
s= marker_sets["particle_148 geometry"]
mark=s.place_marker((2392.89, 2465.94, 1854.87), (0.7, 0.7, 0.7), 137.644)
if "particle_149 geometry" not in marker_sets:
  s=new_marker_set('particle_149 geometry')
  marker_sets["particle_149 geometry"]=s
s= marker_sets["particle_149 geometry"]
mark=s.place_marker((2260.59, 2248.41, 2112.85), (0.7, 0.7, 0.7), 149.277)
if "particle_150 geometry" not in marker_sets:
  s=new_marker_set('particle_150 geometry')
  marker_sets["particle_150 geometry"]=s
s= marker_sets["particle_150 geometry"]
mark=s.place_marker((2603.78, 2198.42, 2178.49), (0.7, 0.7, 0.7), 103.677)
if "particle_151 geometry" not in marker_sets:
  s=new_marker_set('particle_151 geometry')
  marker_sets["particle_151 geometry"]=s
s= marker_sets["particle_151 geometry"]
mark=s.place_marker((3041.34, 2049.43, 2045.29), (0.7, 0.7, 0.7), 99.6588)
if "particle_152 geometry" not in marker_sets:
  s=new_marker_set('particle_152 geometry')
  marker_sets["particle_152 geometry"]=s
s= marker_sets["particle_152 geometry"]
mark=s.place_marker((3368.81, 1897.56, 1950.93), (0.7, 0.7, 0.7), 134.133)
if "particle_153 geometry" not in marker_sets:
  s=new_marker_set('particle_153 geometry')
  marker_sets["particle_153 geometry"]=s
s= marker_sets["particle_153 geometry"]
mark=s.place_marker((3277.81, 2213.86, 2020.12), (0.7, 0.7, 0.7), 173.007)
if "particle_154 geometry" not in marker_sets:
  s=new_marker_set('particle_154 geometry')
  marker_sets["particle_154 geometry"]=s
s= marker_sets["particle_154 geometry"]
mark=s.place_marker((2804.96, 2393.83, 2282.6), (0.7, 0.7, 0.7), 141.028)
if "particle_155 geometry" not in marker_sets:
  s=new_marker_set('particle_155 geometry')
  marker_sets["particle_155 geometry"]=s
s= marker_sets["particle_155 geometry"]
mark=s.place_marker((2386, 2563.07, 2402.69), (0.7, 0.7, 0.7), 161.121)
if "particle_156 geometry" not in marker_sets:
  s=new_marker_set('particle_156 geometry')
  marker_sets["particle_156 geometry"]=s
s= marker_sets["particle_156 geometry"]
mark=s.place_marker((2144.41, 2448.53, 2179.59), (0.7, 0.7, 0.7), 119.582)
if "particle_157 geometry" not in marker_sets:
  s=new_marker_set('particle_157 geometry')
  marker_sets["particle_157 geometry"]=s
s= marker_sets["particle_157 geometry"]
mark=s.place_marker((2313.63, 2383.66, 1814.96), (0.7, 0.7, 0.7), 137.094)
if "particle_158 geometry" not in marker_sets:
  s=new_marker_set('particle_158 geometry')
  marker_sets["particle_158 geometry"]=s
s= marker_sets["particle_158 geometry"]
mark=s.place_marker((2500.88, 2519.4, 1367.68), (0.7, 0.7, 0.7), 149.234)
if "particle_159 geometry" not in marker_sets:
  s=new_marker_set('particle_159 geometry')
  marker_sets["particle_159 geometry"]=s
s= marker_sets["particle_159 geometry"]
mark=s.place_marker((2397.01, 2947.55, 1417.95), (0.7, 0.7, 0.7), 151.011)
if "particle_160 geometry" not in marker_sets:
  s=new_marker_set('particle_160 geometry')
  marker_sets["particle_160 geometry"]=s
s= marker_sets["particle_160 geometry"]
mark=s.place_marker((2258.16, 3270.45, 1813.95), (0.7, 0.7, 0.7), 184.216)
if "particle_161 geometry" not in marker_sets:
  s=new_marker_set('particle_161 geometry')
  marker_sets["particle_161 geometry"]=s
s= marker_sets["particle_161 geometry"]
mark=s.place_marker((2586.27, 3359.57, 2053.98), (0.7, 0.7, 0.7), 170.596)
if "particle_162 geometry" not in marker_sets:
  s=new_marker_set('particle_162 geometry')
  marker_sets["particle_162 geometry"]=s
s= marker_sets["particle_162 geometry"]
mark=s.place_marker((3006.75, 3411.16, 1576.12), (0.7, 0.7, 0.7), 215.603)
if "particle_163 geometry" not in marker_sets:
  s=new_marker_set('particle_163 geometry')
  marker_sets["particle_163 geometry"]=s
s= marker_sets["particle_163 geometry"]
mark=s.place_marker((3523.42, 3488.67, 853.315), (0.7, 0.7, 0.7), 79.0164)
if "particle_164 geometry" not in marker_sets:
  s=new_marker_set('particle_164 geometry')
  marker_sets["particle_164 geometry"]=s
s= marker_sets["particle_164 geometry"]
mark=s.place_marker((3809.54, 3318.86, 925.855), (0.7, 0.7, 0.7), 77.2821)
if "particle_165 geometry" not in marker_sets:
  s=new_marker_set('particle_165 geometry')
  marker_sets["particle_165 geometry"]=s
s= marker_sets["particle_165 geometry"]
mark=s.place_marker((3734.03, 3052.6, 1146.22), (0.7, 0.7, 0.7), 188.658)
if "particle_166 geometry" not in marker_sets:
  s=new_marker_set('particle_166 geometry')
  marker_sets["particle_166 geometry"]=s
s= marker_sets["particle_166 geometry"]
mark=s.place_marker((3917.83, 3070.43, 1392.58), (0.7, 0.7, 0.7), 115.437)
if "particle_167 geometry" not in marker_sets:
  s=new_marker_set('particle_167 geometry')
  marker_sets["particle_167 geometry"]=s
s= marker_sets["particle_167 geometry"]
mark=s.place_marker((3382.22, 2994.28, 1668.32), (0.7, 0.7, 0.7), 88.4916)
if "particle_168 geometry" not in marker_sets:
  s=new_marker_set('particle_168 geometry')
  marker_sets["particle_168 geometry"]=s
s= marker_sets["particle_168 geometry"]
mark=s.place_marker((2823.5, 2918.08, 1947.98), (0.7, 0.7, 0.7), 108.88)
if "particle_169 geometry" not in marker_sets:
  s=new_marker_set('particle_169 geometry')
  marker_sets["particle_169 geometry"]=s
s= marker_sets["particle_169 geometry"]
mark=s.place_marker((2465.4, 2972.51, 1945.15), (0.7, 0.7, 0.7), 172.119)
if "particle_170 geometry" not in marker_sets:
  s=new_marker_set('particle_170 geometry')
  marker_sets["particle_170 geometry"]=s
s= marker_sets["particle_170 geometry"]
mark=s.place_marker((2762.56, 3104.84, 1588.09), (0.7, 0.7, 0.7), 139.505)
if "particle_171 geometry" not in marker_sets:
  s=new_marker_set('particle_171 geometry')
  marker_sets["particle_171 geometry"]=s
s= marker_sets["particle_171 geometry"]
mark=s.place_marker((3066.88, 3236.5, 1225.36), (0.7, 0.7, 0.7), 92.7639)
if "particle_172 geometry" not in marker_sets:
  s=new_marker_set('particle_172 geometry')
  marker_sets["particle_172 geometry"]=s
s= marker_sets["particle_172 geometry"]
mark=s.place_marker((2859.61, 3371.88, 1181.09), (0.7, 0.7, 0.7), 89.8452)
if "particle_173 geometry" not in marker_sets:
  s=new_marker_set('particle_173 geometry')
  marker_sets["particle_173 geometry"]=s
s= marker_sets["particle_173 geometry"]
mark=s.place_marker((2958.59, 3450.94, 1439.13), (0.7, 0.7, 0.7), 149.446)
if "particle_174 geometry" not in marker_sets:
  s=new_marker_set('particle_174 geometry')
  marker_sets["particle_174 geometry"]=s
s= marker_sets["particle_174 geometry"]
mark=s.place_marker((3291.02, 3484.1, 1491.19), (0.7, 0.7, 0.7), 126.858)
if "particle_175 geometry" not in marker_sets:
  s=new_marker_set('particle_175 geometry')
  marker_sets["particle_175 geometry"]=s
s= marker_sets["particle_175 geometry"]
mark=s.place_marker((3370.33, 3398.26, 1170.2), (0.7, 0.7, 0.7), 106.046)
if "particle_176 geometry" not in marker_sets:
  s=new_marker_set('particle_176 geometry')
  marker_sets["particle_176 geometry"]=s
s= marker_sets["particle_176 geometry"]
mark=s.place_marker((3033.67, 3254.03, 811.025), (0.7, 0.7, 0.7), 156.298)
if "particle_177 geometry" not in marker_sets:
  s=new_marker_set('particle_177 geometry')
  marker_sets["particle_177 geometry"]=s
s= marker_sets["particle_177 geometry"]
mark=s.place_marker((2663.86, 2981.24, 415.475), (0.7, 0.7, 0.7), 231.212)
if "particle_178 geometry" not in marker_sets:
  s=new_marker_set('particle_178 geometry')
  marker_sets["particle_178 geometry"]=s
s= marker_sets["particle_178 geometry"]
mark=s.place_marker((2117.94, 2940.87, 520.944), (0.7, 0.7, 0.7), 88.4916)
if "particle_179 geometry" not in marker_sets:
  s=new_marker_set('particle_179 geometry')
  marker_sets["particle_179 geometry"]=s
s= marker_sets["particle_179 geometry"]
mark=s.place_marker((1891.93, 3003.64, 943.407), (0.7, 0.7, 0.7), 111.334)
if "particle_180 geometry" not in marker_sets:
  s=new_marker_set('particle_180 geometry')
  marker_sets["particle_180 geometry"]=s
s= marker_sets["particle_180 geometry"]
mark=s.place_marker((1984.3, 3032.02, 1545.2), (0.7, 0.7, 0.7), 127.619)
if "particle_181 geometry" not in marker_sets:
  s=new_marker_set('particle_181 geometry')
  marker_sets["particle_181 geometry"]=s
s= marker_sets["particle_181 geometry"]
mark=s.place_marker((2097.27, 3002.15, 1980.21), (0.7, 0.7, 0.7), 230.746)
if "particle_182 geometry" not in marker_sets:
  s=new_marker_set('particle_182 geometry')
  marker_sets["particle_182 geometry"]=s
s= marker_sets["particle_182 geometry"]
mark=s.place_marker((2338.78, 2940.09, 1654.29), (0.7, 0.7, 0.7), 124.573)
if "particle_183 geometry" not in marker_sets:
  s=new_marker_set('particle_183 geometry')
  marker_sets["particle_183 geometry"]=s
s= marker_sets["particle_183 geometry"]
mark=s.place_marker((2620.97, 3025.88, 1096.28), (0.7, 0.7, 0.7), 124.489)
if "particle_184 geometry" not in marker_sets:
  s=new_marker_set('particle_184 geometry')
  marker_sets["particle_184 geometry"]=s
s= marker_sets["particle_184 geometry"]
mark=s.place_marker((2995.46, 2970.48, 1062.63), (0.7, 0.7, 0.7), 196.61)
if "particle_185 geometry" not in marker_sets:
  s=new_marker_set('particle_185 geometry')
  marker_sets["particle_185 geometry"]=s
s= marker_sets["particle_185 geometry"]
mark=s.place_marker((2841.53, 3206.36, 1243.55), (0.7, 0.7, 0.7), 134.049)
if "particle_186 geometry" not in marker_sets:
  s=new_marker_set('particle_186 geometry')
  marker_sets["particle_186 geometry"]=s
s= marker_sets["particle_186 geometry"]
mark=s.place_marker((2707.71, 3475.7, 1154.39), (0.7, 0.7, 0.7), 141.493)
if "particle_187 geometry" not in marker_sets:
  s=new_marker_set('particle_187 geometry')
  marker_sets["particle_187 geometry"]=s
s= marker_sets["particle_187 geometry"]
mark=s.place_marker((2683.05, 3738.52, 842.104), (0.7, 0.7, 0.7), 172.203)
if "particle_188 geometry" not in marker_sets:
  s=new_marker_set('particle_188 geometry')
  marker_sets["particle_188 geometry"]=s
s= marker_sets["particle_188 geometry"]
mark=s.place_marker((3039.53, 3385.67, 1253.64), (0.7, 0.7, 0.7), 271.354)
if "particle_189 geometry" not in marker_sets:
  s=new_marker_set('particle_189 geometry')
  marker_sets["particle_189 geometry"]=s
s= marker_sets["particle_189 geometry"]
mark=s.place_marker((3171.66, 2896.88, 1394.68), (0.7, 0.7, 0.7), 97.0785)
if "particle_190 geometry" not in marker_sets:
  s=new_marker_set('particle_190 geometry')
  marker_sets["particle_190 geometry"]=s
s= marker_sets["particle_190 geometry"]
mark=s.place_marker((3202.96, 2474.95, 1319.7), (0.7, 0.7, 0.7), 151.857)
if "particle_191 geometry" not in marker_sets:
  s=new_marker_set('particle_191 geometry')
  marker_sets["particle_191 geometry"]=s
s= marker_sets["particle_191 geometry"]
mark=s.place_marker((3373.81, 1924.19, 1471.59), (0.7, 0.7, 0.7), 199.233)
if "particle_192 geometry" not in marker_sets:
  s=new_marker_set('particle_192 geometry')
  marker_sets["particle_192 geometry"]=s
s= marker_sets["particle_192 geometry"]
mark=s.place_marker((3171.57, 1692.74, 1982.17), (0.7, 0.7, 0.7), 118.863)
if "particle_193 geometry" not in marker_sets:
  s=new_marker_set('particle_193 geometry')
  marker_sets["particle_193 geometry"]=s
s= marker_sets["particle_193 geometry"]
mark=s.place_marker((3056.36, 1275.66, 2128.12), (0.7, 0.7, 0.7), 172.415)
if "particle_194 geometry" not in marker_sets:
  s=new_marker_set('particle_194 geometry')
  marker_sets["particle_194 geometry"]=s
s= marker_sets["particle_194 geometry"]
mark=s.place_marker((3112.95, 778.433, 1994.29), (0.7, 0.7, 0.7), 134.26)
if "particle_195 geometry" not in marker_sets:
  s=new_marker_set('particle_195 geometry')
  marker_sets["particle_195 geometry"]=s
s= marker_sets["particle_195 geometry"]
mark=s.place_marker((3450.32, 18.9921, 1562.54), (0.7, 0.7, 0.7), 139.548)
if "particle_196 geometry" not in marker_sets:
  s=new_marker_set('particle_196 geometry')
  marker_sets["particle_196 geometry"]=s
s= marker_sets["particle_196 geometry"]
mark=s.place_marker((3190.05, 225.247, 1119.03), (0.7, 0.7, 0.7), 196.526)
if "particle_197 geometry" not in marker_sets:
  s=new_marker_set('particle_197 geometry')
  marker_sets["particle_197 geometry"]=s
s= marker_sets["particle_197 geometry"]
mark=s.place_marker((2860.24, 929.706, 1021.9), (0.7, 0.7, 0.7), 136.206)
if "particle_198 geometry" not in marker_sets:
  s=new_marker_set('particle_198 geometry')
  marker_sets["particle_198 geometry"]=s
s= marker_sets["particle_198 geometry"]
mark=s.place_marker((2353.02, 1661.3, 1414.73), (0.7, 0.7, 0.7), 152.322)
if "particle_199 geometry" not in marker_sets:
  s=new_marker_set('particle_199 geometry')
  marker_sets["particle_199 geometry"]=s
s= marker_sets["particle_199 geometry"]
mark=s.place_marker((2175.77, 2197.02, 1770.28), (0.7, 0.7, 0.7), 126.054)
if "particle_200 geometry" not in marker_sets:
  s=new_marker_set('particle_200 geometry')
  marker_sets["particle_200 geometry"]=s
s= marker_sets["particle_200 geometry"]
mark=s.place_marker((2369.72, 2490.79, 1523.25), (0.7, 0.7, 0.7), 164.378)
if "particle_201 geometry" not in marker_sets:
  s=new_marker_set('particle_201 geometry')
  marker_sets["particle_201 geometry"]=s
s= marker_sets["particle_201 geometry"]
mark=s.place_marker((2753.12, 2614.26, 1337.69), (0.7, 0.7, 0.7), 122.205)
if "particle_202 geometry" not in marker_sets:
  s=new_marker_set('particle_202 geometry')
  marker_sets["particle_202 geometry"]=s
s= marker_sets["particle_202 geometry"]
mark=s.place_marker((3192.54, 2682.48, 1341.32), (0.7, 0.7, 0.7), 134.979)
if "particle_203 geometry" not in marker_sets:
  s=new_marker_set('particle_203 geometry')
  marker_sets["particle_203 geometry"]=s
s= marker_sets["particle_203 geometry"]
mark=s.place_marker((3261.52, 2595.62, 1687.6), (0.7, 0.7, 0.7), 136.375)
if "particle_204 geometry" not in marker_sets:
  s=new_marker_set('particle_204 geometry')
  marker_sets["particle_204 geometry"]=s
s= marker_sets["particle_204 geometry"]
mark=s.place_marker((3080.15, 2537.23, 1463.55), (0.7, 0.7, 0.7), 151.688)
if "particle_205 geometry" not in marker_sets:
  s=new_marker_set('particle_205 geometry')
  marker_sets["particle_205 geometry"]=s
s= marker_sets["particle_205 geometry"]
mark=s.place_marker((3251.47, 2702.62, 1430.98), (0.7, 0.7, 0.7), 116.156)
if "particle_206 geometry" not in marker_sets:
  s=new_marker_set('particle_206 geometry')
  marker_sets["particle_206 geometry"]=s
s= marker_sets["particle_206 geometry"]
mark=s.place_marker((2762.59, 2696.73, 1943.26), (0.7, 0.7, 0.7), 122.839)
if "particle_207 geometry" not in marker_sets:
  s=new_marker_set('particle_207 geometry')
  marker_sets["particle_207 geometry"]=s
s= marker_sets["particle_207 geometry"]
mark=s.place_marker((2293.5, 2574.56, 2098.36), (0.7, 0.7, 0.7), 164.716)
if "particle_208 geometry" not in marker_sets:
  s=new_marker_set('particle_208 geometry')
  marker_sets["particle_208 geometry"]=s
s= marker_sets["particle_208 geometry"]
mark=s.place_marker((2457.4, 2241.81, 1322.09), (0.7, 0.7, 0.7), 303.672)
if "particle_209 geometry" not in marker_sets:
  s=new_marker_set('particle_209 geometry')
  marker_sets["particle_209 geometry"]=s
s= marker_sets["particle_209 geometry"]
mark=s.place_marker((3135.04, 1941.52, 582.489), (0.7, 0.7, 0.7), 220.298)
if "particle_210 geometry" not in marker_sets:
  s=new_marker_set('particle_210 geometry')
  marker_sets["particle_210 geometry"]=s
s= marker_sets["particle_210 geometry"]
mark=s.place_marker((3425.95, 2496.08, 708.096), (0.7, 0.7, 0.7), 175.883)
if "particle_211 geometry" not in marker_sets:
  s=new_marker_set('particle_211 geometry')
  marker_sets["particle_211 geometry"]=s
s= marker_sets["particle_211 geometry"]
mark=s.place_marker((3342.62, 3179.3, 726.711), (0.7, 0.7, 0.7), 233.581)
if "particle_212 geometry" not in marker_sets:
  s=new_marker_set('particle_212 geometry')
  marker_sets["particle_212 geometry"]=s
s= marker_sets["particle_212 geometry"]
mark=s.place_marker((2697.43, 3622.94, 752.844), (0.7, 0.7, 0.7), 231.127)
if "particle_213 geometry" not in marker_sets:
  s=new_marker_set('particle_213 geometry')
  marker_sets["particle_213 geometry"]=s
s= marker_sets["particle_213 geometry"]
mark=s.place_marker((2590.92, 4202.47, 959.368), (0.7, 0.7, 0.7), 247.413)
if "particle_214 geometry" not in marker_sets:
  s=new_marker_set('particle_214 geometry')
  marker_sets["particle_214 geometry"]=s
s= marker_sets["particle_214 geometry"]
mark=s.place_marker((2905.38, 4700.89, 1247.12), (0.7, 0.7, 0.7), 200.206)
if "particle_215 geometry" not in marker_sets:
  s=new_marker_set('particle_215 geometry')
  marker_sets["particle_215 geometry"]=s
s= marker_sets["particle_215 geometry"]
mark=s.place_marker((3305.93, 4657.42, 1401.43), (0.7, 0.7, 0.7), 150.419)
if "particle_216 geometry" not in marker_sets:
  s=new_marker_set('particle_216 geometry')
  marker_sets["particle_216 geometry"]=s
s= marker_sets["particle_216 geometry"]
mark=s.place_marker((2880, 4364.68, 1726.24), (0.7, 0.7, 0.7), 140.14)
if "particle_217 geometry" not in marker_sets:
  s=new_marker_set('particle_217 geometry')
  marker_sets["particle_217 geometry"]=s
s= marker_sets["particle_217 geometry"]
mark=s.place_marker((2439.44, 4350.58, 1839.62), (0.7, 0.7, 0.7), 132.949)
if "particle_218 geometry" not in marker_sets:
  s=new_marker_set('particle_218 geometry')
  marker_sets["particle_218 geometry"]=s
s= marker_sets["particle_218 geometry"]
mark=s.place_marker((2128.39, 4198.25, 2015.47), (0.7, 0.7, 0.7), 141.113)
if "particle_219 geometry" not in marker_sets:
  s=new_marker_set('particle_219 geometry')
  marker_sets["particle_219 geometry"]=s
s= marker_sets["particle_219 geometry"]
mark=s.place_marker((1987.92, 4059.46, 1728.22), (0.7, 0.7, 0.7), 171.526)
if "particle_220 geometry" not in marker_sets:
  s=new_marker_set('particle_220 geometry')
  marker_sets["particle_220 geometry"]=s
s= marker_sets["particle_220 geometry"]
mark=s.place_marker((2206.78, 3986.57, 1175.17), (0.7, 0.7, 0.7), 326.937)
if "particle_221 geometry" not in marker_sets:
  s=new_marker_set('particle_221 geometry')
  marker_sets["particle_221 geometry"]=s
s= marker_sets["particle_221 geometry"]
mark=s.place_marker((2612.85, 3665.36, 913.849), (0.7, 0.7, 0.7), 92.0871)
if "particle_222 geometry" not in marker_sets:
  s=new_marker_set('particle_222 geometry')
  marker_sets["particle_222 geometry"]=s
s= marker_sets["particle_222 geometry"]
mark=s.place_marker((2452.17, 3244.89, 1039.28), (0.7, 0.7, 0.7), 210.273)
if "particle_223 geometry" not in marker_sets:
  s=new_marker_set('particle_223 geometry')
  marker_sets["particle_223 geometry"]=s
s= marker_sets["particle_223 geometry"]
mark=s.place_marker((2076.11, 3114.19, 1679.23), (0.7, 0.7, 0.7), 122.628)
if "particle_224 geometry" not in marker_sets:
  s=new_marker_set('particle_224 geometry')
  marker_sets["particle_224 geometry"]=s
s= marker_sets["particle_224 geometry"]
mark=s.place_marker((1939.01, 3175.48, 1886.79), (0.7, 0.7, 0.7), 109.176)
if "particle_225 geometry" not in marker_sets:
  s=new_marker_set('particle_225 geometry')
  marker_sets["particle_225 geometry"]=s
s= marker_sets["particle_225 geometry"]
mark=s.place_marker((2189.21, 3264.49, 1751.2), (0.7, 0.7, 0.7), 142.213)
if "particle_226 geometry" not in marker_sets:
  s=new_marker_set('particle_226 geometry')
  marker_sets["particle_226 geometry"]=s
s= marker_sets["particle_226 geometry"]
mark=s.place_marker((2247.92, 3008.84, 1440.13), (0.7, 0.7, 0.7), 250.078)
if "particle_227 geometry" not in marker_sets:
  s=new_marker_set('particle_227 geometry')
  marker_sets["particle_227 geometry"]=s
s= marker_sets["particle_227 geometry"]
mark=s.place_marker((2621.74, 2922.52, 1691.75), (0.7, 0.7, 0.7), 123.558)
if "particle_228 geometry" not in marker_sets:
  s=new_marker_set('particle_228 geometry')
  marker_sets["particle_228 geometry"]=s
s= marker_sets["particle_228 geometry"]
mark=s.place_marker((2738.12, 2880.33, 2152.35), (0.7, 0.7, 0.7), 235.992)
if "particle_229 geometry" not in marker_sets:
  s=new_marker_set('particle_229 geometry')
  marker_sets["particle_229 geometry"]=s
s= marker_sets["particle_229 geometry"]
mark=s.place_marker((2984.72, 2754.29, 2554.72), (0.7, 0.7, 0.7), 172.373)
if "particle_230 geometry" not in marker_sets:
  s=new_marker_set('particle_230 geometry')
  marker_sets["particle_230 geometry"]=s
s= marker_sets["particle_230 geometry"]
mark=s.place_marker((3419.5, 2645.77, 2474.6), (0.7, 0.7, 0.7), 152.322)
if "particle_231 geometry" not in marker_sets:
  s=new_marker_set('particle_231 geometry')
  marker_sets["particle_231 geometry"]=s
s= marker_sets["particle_231 geometry"]
mark=s.place_marker((3681.73, 2498.85, 2307.99), (0.7, 0.7, 0.7), 196.653)
if "particle_232 geometry" not in marker_sets:
  s=new_marker_set('particle_232 geometry')
  marker_sets["particle_232 geometry"]=s
s= marker_sets["particle_232 geometry"]
mark=s.place_marker((3590.92, 2705.34, 2578.45), (0.7, 0.7, 0.7), 134.091)
if "particle_233 geometry" not in marker_sets:
  s=new_marker_set('particle_233 geometry')
  marker_sets["particle_233 geometry"]=s
s= marker_sets["particle_233 geometry"]
mark=s.place_marker((3429.12, 2915.73, 2761.67), (0.7, 0.7, 0.7), 180.325)
if "particle_234 geometry" not in marker_sets:
  s=new_marker_set('particle_234 geometry')
  marker_sets["particle_234 geometry"]=s
s= marker_sets["particle_234 geometry"]
mark=s.place_marker((3096.2, 2754.27, 2463.9), (0.7, 0.7, 0.7), 218.437)
if "particle_235 geometry" not in marker_sets:
  s=new_marker_set('particle_235 geometry')
  marker_sets["particle_235 geometry"]=s
s= marker_sets["particle_235 geometry"]
mark=s.place_marker((3054.33, 2741.7, 1999.7), (0.7, 0.7, 0.7), 148.008)
if "particle_236 geometry" not in marker_sets:
  s=new_marker_set('particle_236 geometry')
  marker_sets["particle_236 geometry"]=s
s= marker_sets["particle_236 geometry"]
mark=s.place_marker((3306.83, 2895.91, 1434.46), (0.7, 0.7, 0.7), 191.873)
if "particle_237 geometry" not in marker_sets:
  s=new_marker_set('particle_237 geometry')
  marker_sets["particle_237 geometry"]=s
s= marker_sets["particle_237 geometry"]
mark=s.place_marker((3411.44, 3257.59, 1026.42), (0.7, 0.7, 0.7), 138.575)
if "particle_238 geometry" not in marker_sets:
  s=new_marker_set('particle_238 geometry')
  marker_sets["particle_238 geometry"]=s
s= marker_sets["particle_238 geometry"]
mark=s.place_marker((3782.13, 3489.36, 987.607), (0.7, 0.7, 0.7), 161.205)
if "particle_239 geometry" not in marker_sets:
  s=new_marker_set('particle_239 geometry')
  marker_sets["particle_239 geometry"]=s
s= marker_sets["particle_239 geometry"]
mark=s.place_marker((3674.08, 3040.95, 1073.05), (0.7, 0.7, 0.7), 288.021)
if "particle_240 geometry" not in marker_sets:
  s=new_marker_set('particle_240 geometry')
  marker_sets["particle_240 geometry"]=s
s= marker_sets["particle_240 geometry"]
mark=s.place_marker((3647.22, 3021.99, 1796.95), (0.7, 0.7, 0.7), 227.405)
if "particle_241 geometry" not in marker_sets:
  s=new_marker_set('particle_241 geometry')
  marker_sets["particle_241 geometry"]=s
s= marker_sets["particle_241 geometry"]
mark=s.place_marker((3439.29, 2863.22, 2241.97), (0.7, 0.7, 0.7), 126.519)
if "particle_242 geometry" not in marker_sets:
  s=new_marker_set('particle_242 geometry')
  marker_sets["particle_242 geometry"]=s
s= marker_sets["particle_242 geometry"]
mark=s.place_marker((3635.63, 2677.72, 2085.44), (0.7, 0.7, 0.7), 117.975)
if "particle_243 geometry" not in marker_sets:
  s=new_marker_set('particle_243 geometry')
  marker_sets["particle_243 geometry"]=s
s= marker_sets["particle_243 geometry"]
mark=s.place_marker((3248.67, 2584.58, 2115.36), (0.7, 0.7, 0.7), 200.883)
if "particle_244 geometry" not in marker_sets:
  s=new_marker_set('particle_244 geometry')
  marker_sets["particle_244 geometry"]=s
s= marker_sets["particle_244 geometry"]
mark=s.place_marker((3075.7, 2820.67, 2357.26), (0.7, 0.7, 0.7), 158.794)
if "particle_245 geometry" not in marker_sets:
  s=new_marker_set('particle_245 geometry')
  marker_sets["particle_245 geometry"]=s
s= marker_sets["particle_245 geometry"]
mark=s.place_marker((2994.33, 3117.44, 2446.73), (0.7, 0.7, 0.7), 115.86)
if "particle_246 geometry" not in marker_sets:
  s=new_marker_set('particle_246 geometry')
  marker_sets["particle_246 geometry"]=s
s= marker_sets["particle_246 geometry"]
mark=s.place_marker((2811.31, 3164.88, 2605.06), (0.7, 0.7, 0.7), 133.034)
if "particle_247 geometry" not in marker_sets:
  s=new_marker_set('particle_247 geometry')
  marker_sets["particle_247 geometry"]=s
s= marker_sets["particle_247 geometry"]
mark=s.place_marker((2825.46, 2736.75, 2818.55), (0.7, 0.7, 0.7), 314.627)
if "particle_248 geometry" not in marker_sets:
  s=new_marker_set('particle_248 geometry')
  marker_sets["particle_248 geometry"]=s
s= marker_sets["particle_248 geometry"]
mark=s.place_marker((3084.59, 2749.57, 2567.38), (0.7, 0.7, 0.7), 115.352)
if "particle_249 geometry" not in marker_sets:
  s=new_marker_set('particle_249 geometry')
  marker_sets["particle_249 geometry"]=s
s= marker_sets["particle_249 geometry"]
mark=s.place_marker((3330.95, 3009.78, 2332.35), (0.7, 0.7, 0.7), 180.621)
if "particle_250 geometry" not in marker_sets:
  s=new_marker_set('particle_250 geometry')
  marker_sets["particle_250 geometry"]=s
s= marker_sets["particle_250 geometry"]
mark=s.place_marker((3203.55, 3351.77, 2371.76), (0.7, 0.7, 0.7), 126.265)
if "particle_251 geometry" not in marker_sets:
  s=new_marker_set('particle_251 geometry')
  marker_sets["particle_251 geometry"]=s
s= marker_sets["particle_251 geometry"]
mark=s.place_marker((2851.17, 3516.16, 2412.57), (0.7, 0.7, 0.7), 133.541)
if "particle_252 geometry" not in marker_sets:
  s=new_marker_set('particle_252 geometry')
  marker_sets["particle_252 geometry"]=s
s= marker_sets["particle_252 geometry"]
mark=s.place_marker((2542.91, 3813.61, 2306.7), (0.7, 0.7, 0.7), 171.019)
if "particle_253 geometry" not in marker_sets:
  s=new_marker_set('particle_253 geometry')
  marker_sets["particle_253 geometry"]=s
s= marker_sets["particle_253 geometry"]
mark=s.place_marker((2369.72, 4124.41, 2106.73), (0.7, 0.7, 0.7), 115.437)
if "particle_254 geometry" not in marker_sets:
  s=new_marker_set('particle_254 geometry')
  marker_sets["particle_254 geometry"]=s
s= marker_sets["particle_254 geometry"]
mark=s.place_marker((2614.6, 4090.13, 2291.37), (0.7, 0.7, 0.7), 158.583)
if "particle_255 geometry" not in marker_sets:
  s=new_marker_set('particle_255 geometry')
  marker_sets["particle_255 geometry"]=s
s= marker_sets["particle_255 geometry"]
mark=s.place_marker((2494.92, 3667.9, 2360.83), (0.7, 0.7, 0.7), 192)
if "particle_256 geometry" not in marker_sets:
  s=new_marker_set('particle_256 geometry')
  marker_sets["particle_256 geometry"]=s
s= marker_sets["particle_256 geometry"]
mark=s.place_marker((2549.28, 3274.68, 2546.07), (0.7, 0.7, 0.7), 150.165)
if "particle_257 geometry" not in marker_sets:
  s=new_marker_set('particle_257 geometry')
  marker_sets["particle_257 geometry"]=s
s= marker_sets["particle_257 geometry"]
mark=s.place_marker((2355.65, 3216.01, 2558.94), (0.7, 0.7, 0.7), 157.567)
if "particle_258 geometry" not in marker_sets:
  s=new_marker_set('particle_258 geometry')
  marker_sets["particle_258 geometry"]=s
s= marker_sets["particle_258 geometry"]
mark=s.place_marker((2327.76, 3100.95, 2514.69), (0.7, 0.7, 0.7), 199.36)
if "particle_259 geometry" not in marker_sets:
  s=new_marker_set('particle_259 geometry')
  marker_sets["particle_259 geometry"]=s
s= marker_sets["particle_259 geometry"]
mark=s.place_marker((2521.47, 3215.41, 2107.21), (0.7, 0.7, 0.7), 105.369)
if "particle_260 geometry" not in marker_sets:
  s=new_marker_set('particle_260 geometry')
  marker_sets["particle_260 geometry"]=s
s= marker_sets["particle_260 geometry"]
mark=s.place_marker((2628.25, 3147.33, 1871.27), (0.7, 0.7, 0.7), 118.651)
if "particle_261 geometry" not in marker_sets:
  s=new_marker_set('particle_261 geometry')
  marker_sets["particle_261 geometry"]=s
s= marker_sets["particle_261 geometry"]
mark=s.place_marker((2605.54, 2897.69, 2244.09), (0.7, 0.7, 0.7), 219.664)
if "particle_262 geometry" not in marker_sets:
  s=new_marker_set('particle_262 geometry')
  marker_sets["particle_262 geometry"]=s
s= marker_sets["particle_262 geometry"]
mark=s.place_marker((2425.07, 2717.28, 2782.73), (0.7, 0.7, 0.7), 196.018)
if "particle_263 geometry" not in marker_sets:
  s=new_marker_set('particle_263 geometry')
  marker_sets["particle_263 geometry"]=s
s= marker_sets["particle_263 geometry"]
mark=s.place_marker((2251.89, 2504.86, 3205.59), (0.7, 0.7, 0.7), 218.141)
if "particle_264 geometry" not in marker_sets:
  s=new_marker_set('particle_264 geometry')
  marker_sets["particle_264 geometry"]=s
s= marker_sets["particle_264 geometry"]
mark=s.place_marker((1908.22, 2509.12, 3116.95), (0.7, 0.7, 0.7), 181.636)
if "particle_265 geometry" not in marker_sets:
  s=new_marker_set('particle_265 geometry')
  marker_sets["particle_265 geometry"]=s
s= marker_sets["particle_265 geometry"]
mark=s.place_marker((1895.29, 2613.38, 2837.28), (0.7, 0.7, 0.7), 195.003)
if "particle_266 geometry" not in marker_sets:
  s=new_marker_set('particle_266 geometry')
  marker_sets["particle_266 geometry"]=s
s= marker_sets["particle_266 geometry"]
mark=s.place_marker((1901.82, 2606.37, 3093.28), (0.7, 0.7, 0.7), 139.209)
if "particle_267 geometry" not in marker_sets:
  s=new_marker_set('particle_267 geometry')
  marker_sets["particle_267 geometry"]=s
s= marker_sets["particle_267 geometry"]
mark=s.place_marker((1867.1, 2673.39, 3129.95), (0.7, 0.7, 0.7), 189.885)
if "particle_268 geometry" not in marker_sets:
  s=new_marker_set('particle_268 geometry')
  marker_sets["particle_268 geometry"]=s
s= marker_sets["particle_268 geometry"]
mark=s.place_marker((2078.51, 2900.92, 3105.19), (0.7, 0.7, 0.7), 267.674)
if "particle_269 geometry" not in marker_sets:
  s=new_marker_set('particle_269 geometry')
  marker_sets["particle_269 geometry"]=s
s= marker_sets["particle_269 geometry"]
mark=s.place_marker((2562.43, 3189.36, 3142.05), (0.7, 0.7, 0.7), 196.568)
if "particle_270 geometry" not in marker_sets:
  s=new_marker_set('particle_270 geometry')
  marker_sets["particle_270 geometry"]=s
s= marker_sets["particle_270 geometry"]
mark=s.place_marker((2339.55, 3390.76, 3181.73), (0.7, 0.7, 0.7), 192.423)
if "particle_271 geometry" not in marker_sets:
  s=new_marker_set('particle_271 geometry')
  marker_sets["particle_271 geometry"]=s
s= marker_sets["particle_271 geometry"]
mark=s.place_marker((2008.6, 3267.71, 3356.63), (1, 0.7, 0), 202.405)
if "particle_272 geometry" not in marker_sets:
  s=new_marker_set('particle_272 geometry')
  marker_sets["particle_272 geometry"]=s
s= marker_sets["particle_272 geometry"]
mark=s.place_marker((2721.44, 3631, 3056.84), (0.7, 0.7, 0.7), 135.529)
if "particle_273 geometry" not in marker_sets:
  s=new_marker_set('particle_273 geometry')
  marker_sets["particle_273 geometry"]=s
s= marker_sets["particle_273 geometry"]
mark=s.place_marker((3452.32, 4174.79, 2678.62), (0.7, 0.7, 0.7), 114.21)
if "particle_274 geometry" not in marker_sets:
  s=new_marker_set('particle_274 geometry')
  marker_sets["particle_274 geometry"]=s
s= marker_sets["particle_274 geometry"]
mark=s.place_marker((3417.05, 4059.71, 2377.98), (0.7, 0.7, 0.7), 159.133)
if "particle_275 geometry" not in marker_sets:
  s=new_marker_set('particle_275 geometry')
  marker_sets["particle_275 geometry"]=s
s= marker_sets["particle_275 geometry"]
mark=s.place_marker((3342.59, 3660.44, 2322.49), (0.7, 0.7, 0.7), 144.412)
if "particle_276 geometry" not in marker_sets:
  s=new_marker_set('particle_276 geometry')
  marker_sets["particle_276 geometry"]=s
s= marker_sets["particle_276 geometry"]
mark=s.place_marker((3304.58, 3342.72, 2307.61), (0.7, 0.7, 0.7), 70.8525)
if "particle_277 geometry" not in marker_sets:
  s=new_marker_set('particle_277 geometry')
  marker_sets["particle_277 geometry"]=s
s= marker_sets["particle_277 geometry"]
mark=s.place_marker((2802.13, 3054.94, 2540.37), (0.7, 0.7, 0.7), 141.874)
if "particle_278 geometry" not in marker_sets:
  s=new_marker_set('particle_278 geometry')
  marker_sets["particle_278 geometry"]=s
s= marker_sets["particle_278 geometry"]
mark=s.place_marker((2302.94, 2848.89, 2834.26), (0.7, 0.7, 0.7), 217.337)
if "particle_279 geometry" not in marker_sets:
  s=new_marker_set('particle_279 geometry')
  marker_sets["particle_279 geometry"]=s
s= marker_sets["particle_279 geometry"]
mark=s.place_marker((2321.62, 2814.75, 2889.26), (0.7, 0.7, 0.7), 237.641)
if "particle_280 geometry" not in marker_sets:
  s=new_marker_set('particle_280 geometry')
  marker_sets["particle_280 geometry"]=s
s= marker_sets["particle_280 geometry"]
mark=s.place_marker((2757.09, 2708.27, 2787.04), (0.7, 0.7, 0.7), 229.393)
if "particle_281 geometry" not in marker_sets:
  s=new_marker_set('particle_281 geometry')
  marker_sets["particle_281 geometry"]=s
s= marker_sets["particle_281 geometry"]
mark=s.place_marker((2678.29, 2350.91, 3279.56), (0.7, 0.7, 0.7), 349.906)
if "particle_282 geometry" not in marker_sets:
  s=new_marker_set('particle_282 geometry')
  marker_sets["particle_282 geometry"]=s
s= marker_sets["particle_282 geometry"]
mark=s.place_marker((2512.15, 2381.06, 3833.65), (0.7, 0.7, 0.7), 162.347)
if "particle_283 geometry" not in marker_sets:
  s=new_marker_set('particle_283 geometry')
  marker_sets["particle_283 geometry"]=s
s= marker_sets["particle_283 geometry"]
mark=s.place_marker((2549.58, 2405.33, 4018.09), (0.7, 0.7, 0.7), 194.072)
if "particle_284 geometry" not in marker_sets:
  s=new_marker_set('particle_284 geometry')
  marker_sets["particle_284 geometry"]=s
s= marker_sets["particle_284 geometry"]
mark=s.place_marker((2710.46, 2318.68, 4030.66), (0.7, 0.7, 0.7), 242.21)
if "particle_285 geometry" not in marker_sets:
  s=new_marker_set('particle_285 geometry')
  marker_sets["particle_285 geometry"]=s
s= marker_sets["particle_285 geometry"]
mark=s.place_marker((3149.28, 2601.58, 4242.54), (0.7, 0.7, 0.7), 320.93)
if "particle_286 geometry" not in marker_sets:
  s=new_marker_set('particle_286 geometry')
  marker_sets["particle_286 geometry"]=s
s= marker_sets["particle_286 geometry"]
mark=s.place_marker((3375.98, 2479.71, 4765.63), (0.7, 0.7, 0.7), 226.432)
if "particle_287 geometry" not in marker_sets:
  s=new_marker_set('particle_287 geometry')
  marker_sets["particle_287 geometry"]=s
s= marker_sets["particle_287 geometry"]
mark=s.place_marker((3190.21, 2109.76, 4775.82), (0.7, 0.7, 0.7), 125.208)
if "particle_288 geometry" not in marker_sets:
  s=new_marker_set('particle_288 geometry')
  marker_sets["particle_288 geometry"]=s
s= marker_sets["particle_288 geometry"]
mark=s.place_marker((2914.3, 1761.76, 4513.04), (0.7, 0.7, 0.7), 197.837)
if "particle_289 geometry" not in marker_sets:
  s=new_marker_set('particle_289 geometry')
  marker_sets["particle_289 geometry"]=s
s= marker_sets["particle_289 geometry"]
mark=s.place_marker((3137.03, 1173.54, 4488.97), (0.7, 0.7, 0.7), 167.804)
if "particle_290 geometry" not in marker_sets:
  s=new_marker_set('particle_290 geometry')
  marker_sets["particle_290 geometry"]=s
s= marker_sets["particle_290 geometry"]
mark=s.place_marker((3640.6, 538.333, 4667.97), (0.7, 0.7, 0.7), 136.84)
if "particle_291 geometry" not in marker_sets:
  s=new_marker_set('particle_291 geometry')
  marker_sets["particle_291 geometry"]=s
s= marker_sets["particle_291 geometry"]
mark=s.place_marker((4047.59, 735.554, 4553.19), (0.7, 0.7, 0.7), 85.7421)
if "particle_292 geometry" not in marker_sets:
  s=new_marker_set('particle_292 geometry')
  marker_sets["particle_292 geometry"]=s
s= marker_sets["particle_292 geometry"]
mark=s.place_marker((3364.09, 1965.06, 4417.51), (1, 0.7, 0), 256)
if "particle_293 geometry" not in marker_sets:
  s=new_marker_set('particle_293 geometry')
  marker_sets["particle_293 geometry"]=s
s= marker_sets["particle_293 geometry"]
mark=s.place_marker((3219.86, 843.016, 4414.69), (0.7, 0.7, 0.7), 138.702)
if "particle_294 geometry" not in marker_sets:
  s=new_marker_set('particle_294 geometry')
  marker_sets["particle_294 geometry"]=s
s= marker_sets["particle_294 geometry"]
mark=s.place_marker((3023.64, 413.773, 4494.62), (0.7, 0.7, 0.7), 140.732)
if "particle_295 geometry" not in marker_sets:
  s=new_marker_set('particle_295 geometry')
  marker_sets["particle_295 geometry"]=s
s= marker_sets["particle_295 geometry"]
mark=s.place_marker((3133.02, 656.364, 4658.93), (0.7, 0.7, 0.7), 81.3006)
if "particle_296 geometry" not in marker_sets:
  s=new_marker_set('particle_296 geometry')
  marker_sets["particle_296 geometry"]=s
s= marker_sets["particle_296 geometry"]
mark=s.place_marker((3446.05, 683.869, 4967.34), (0.7, 0.7, 0.7), 133.837)
if "particle_297 geometry" not in marker_sets:
  s=new_marker_set('particle_297 geometry')
  marker_sets["particle_297 geometry"]=s
s= marker_sets["particle_297 geometry"]
mark=s.place_marker((3311.07, 1267.65, 4771.54), (0.7, 0.7, 0.7), 98.3475)
if "particle_298 geometry" not in marker_sets:
  s=new_marker_set('particle_298 geometry')
  marker_sets["particle_298 geometry"]=s
s= marker_sets["particle_298 geometry"]
mark=s.place_marker((2848.9, 1841.38, 4416.29), (0.7, 0.7, 0.7), 297.623)
if "particle_299 geometry" not in marker_sets:
  s=new_marker_set('particle_299 geometry')
  marker_sets["particle_299 geometry"]=s
s= marker_sets["particle_299 geometry"]
mark=s.place_marker((2830.21, 2217.76, 4225.47), (0.7, 0.7, 0.7), 212.938)
if "particle_300 geometry" not in marker_sets:
  s=new_marker_set('particle_300 geometry')
  marker_sets["particle_300 geometry"]=s
s= marker_sets["particle_300 geometry"]
mark=s.place_marker((2723.99, 2258.96, 4421.43), (0.7, 0.7, 0.7), 154.183)
if "particle_301 geometry" not in marker_sets:
  s=new_marker_set('particle_301 geometry')
  marker_sets["particle_301 geometry"]=s
s= marker_sets["particle_301 geometry"]
mark=s.place_marker((3009.04, 2517.89, 4597.3), (0.7, 0.7, 0.7), 180.832)
if "particle_302 geometry" not in marker_sets:
  s=new_marker_set('particle_302 geometry')
  marker_sets["particle_302 geometry"]=s
s= marker_sets["particle_302 geometry"]
mark=s.place_marker((3355.21, 2672.52, 4541.5), (0.7, 0.7, 0.7), 122.332)
if "particle_303 geometry" not in marker_sets:
  s=new_marker_set('particle_303 geometry')
  marker_sets["particle_303 geometry"]=s
s= marker_sets["particle_303 geometry"]
mark=s.place_marker((3685.14, 2722.6, 4363.1), (0.7, 0.7, 0.7), 209.047)
if "particle_304 geometry" not in marker_sets:
  s=new_marker_set('particle_304 geometry')
  marker_sets["particle_304 geometry"]=s
s= marker_sets["particle_304 geometry"]
mark=s.place_marker((3644.85, 3003.73, 4663.42), (0.7, 0.7, 0.7), 126.985)
if "particle_305 geometry" not in marker_sets:
  s=new_marker_set('particle_305 geometry')
  marker_sets["particle_305 geometry"]=s
s= marker_sets["particle_305 geometry"]
mark=s.place_marker((3823.49, 3072.83, 5039.18), (0.7, 0.7, 0.7), 122.205)
if "particle_306 geometry" not in marker_sets:
  s=new_marker_set('particle_306 geometry')
  marker_sets["particle_306 geometry"]=s
s= marker_sets["particle_306 geometry"]
mark=s.place_marker((3798.2, 2920.78, 5268.52), (0.7, 0.7, 0.7), 107.95)
if "particle_307 geometry" not in marker_sets:
  s=new_marker_set('particle_307 geometry')
  marker_sets["particle_307 geometry"]=s
s= marker_sets["particle_307 geometry"]
mark=s.place_marker((3336.08, 2814.88, 4898.23), (0.7, 0.7, 0.7), 182.567)
if "particle_308 geometry" not in marker_sets:
  s=new_marker_set('particle_308 geometry')
  marker_sets["particle_308 geometry"]=s
s= marker_sets["particle_308 geometry"]
mark=s.place_marker((2977.43, 2567.09, 4439.79), (0.7, 0.7, 0.7), 185.274)
if "particle_309 geometry" not in marker_sets:
  s=new_marker_set('particle_309 geometry')
  marker_sets["particle_309 geometry"]=s
s= marker_sets["particle_309 geometry"]
mark=s.place_marker((2972.99, 2376.37, 3980.96), (0.7, 0.7, 0.7), 413.567)
if "particle_310 geometry" not in marker_sets:
  s=new_marker_set('particle_310 geometry')
  marker_sets["particle_310 geometry"]=s
s= marker_sets["particle_310 geometry"]
mark=s.place_marker((2746.7, 2364.89, 3949.1), (0.7, 0.7, 0.7), 240.01)
if "particle_311 geometry" not in marker_sets:
  s=new_marker_set('particle_311 geometry')
  marker_sets["particle_311 geometry"]=s
s= marker_sets["particle_311 geometry"]
mark=s.place_marker((2786.73, 2383.58, 3945.33), (0.7, 0.7, 0.7), 238.995)
if "particle_312 geometry" not in marker_sets:
  s=new_marker_set('particle_312 geometry')
  marker_sets["particle_312 geometry"]=s
s= marker_sets["particle_312 geometry"]
mark=s.place_marker((2740.47, 2458.7, 4224.46), (0.7, 0.7, 0.7), 203.674)
if "particle_313 geometry" not in marker_sets:
  s=new_marker_set('particle_313 geometry')
  marker_sets["particle_313 geometry"]=s
s= marker_sets["particle_313 geometry"]
mark=s.place_marker((2731.45, 2955.64, 4572.69), (0.7, 0.7, 0.7), 266.744)
if "particle_314 geometry" not in marker_sets:
  s=new_marker_set('particle_314 geometry')
  marker_sets["particle_314 geometry"]=s
s= marker_sets["particle_314 geometry"]
mark=s.place_marker((2510.2, 2675.07, 4853.71), (0.7, 0.7, 0.7), 147.585)
if "particle_315 geometry" not in marker_sets:
  s=new_marker_set('particle_315 geometry')
  marker_sets["particle_315 geometry"]=s
s= marker_sets["particle_315 geometry"]
mark=s.place_marker((2544.62, 2613.41, 4577.98), (0.7, 0.7, 0.7), 249.485)
if "particle_316 geometry" not in marker_sets:
  s=new_marker_set('particle_316 geometry')
  marker_sets["particle_316 geometry"]=s
s= marker_sets["particle_316 geometry"]
mark=s.place_marker((2753.45, 2800.8, 4243.55), (0.7, 0.7, 0.7), 119.371)
if "particle_317 geometry" not in marker_sets:
  s=new_marker_set('particle_317 geometry')
  marker_sets["particle_317 geometry"]=s
s= marker_sets["particle_317 geometry"]
mark=s.place_marker((3416.63, 2933.6, 3996.12), (0.7, 0.7, 0.7), 155.875)
if "particle_318 geometry" not in marker_sets:
  s=new_marker_set('particle_318 geometry')
  marker_sets["particle_318 geometry"]=s
s= marker_sets["particle_318 geometry"]
mark=s.place_marker((4088.6, 2573.34, 3842.44), (0.7, 0.7, 0.7), 189.419)
if "particle_319 geometry" not in marker_sets:
  s=new_marker_set('particle_319 geometry')
  marker_sets["particle_319 geometry"]=s
s= marker_sets["particle_319 geometry"]
mark=s.place_marker((4042.99, 2049.94, 3618.22), (0.7, 0.7, 0.7), 137.475)
if "particle_320 geometry" not in marker_sets:
  s=new_marker_set('particle_320 geometry')
  marker_sets["particle_320 geometry"]=s
s= marker_sets["particle_320 geometry"]
mark=s.place_marker((3750.68, 1676.71, 3404.39), (0.7, 0.7, 0.7), 176.179)
if "particle_321 geometry" not in marker_sets:
  s=new_marker_set('particle_321 geometry')
  marker_sets["particle_321 geometry"]=s
s= marker_sets["particle_321 geometry"]
mark=s.place_marker((3580.5, 1240.18, 3295.42), (0.7, 0.7, 0.7), 138.829)
if "particle_322 geometry" not in marker_sets:
  s=new_marker_set('particle_322 geometry')
  marker_sets["particle_322 geometry"]=s
s= marker_sets["particle_322 geometry"]
mark=s.place_marker((3501.27, 816.876, 3333.01), (0.7, 0.7, 0.7), 148.727)
if "particle_323 geometry" not in marker_sets:
  s=new_marker_set('particle_323 geometry')
  marker_sets["particle_323 geometry"]=s
s= marker_sets["particle_323 geometry"]
mark=s.place_marker((3601.47, 312.763, 3463.94), (0.7, 0.7, 0.7), 230.323)
if "particle_324 geometry" not in marker_sets:
  s=new_marker_set('particle_324 geometry')
  marker_sets["particle_324 geometry"]=s
s= marker_sets["particle_324 geometry"]
mark=s.place_marker((3682.48, 899.108, 3646.98), (0.7, 0.7, 0.7), 175.376)
if "particle_325 geometry" not in marker_sets:
  s=new_marker_set('particle_325 geometry')
  marker_sets["particle_325 geometry"]=s
s= marker_sets["particle_325 geometry"]
mark=s.place_marker((3603.63, 1382.67, 3630.18), (0.7, 0.7, 0.7), 161.163)
if "particle_326 geometry" not in marker_sets:
  s=new_marker_set('particle_326 geometry')
  marker_sets["particle_326 geometry"]=s
s= marker_sets["particle_326 geometry"]
mark=s.place_marker((3874.41, 1372.14, 3246.59), (0.7, 0.7, 0.7), 125.885)
if "particle_327 geometry" not in marker_sets:
  s=new_marker_set('particle_327 geometry')
  marker_sets["particle_327 geometry"]=s
s= marker_sets["particle_327 geometry"]
mark=s.place_marker((4287.77, 1430.35, 3056.21), (0.7, 0.7, 0.7), 206.635)
if "particle_328 geometry" not in marker_sets:
  s=new_marker_set('particle_328 geometry')
  marker_sets["particle_328 geometry"]=s
s= marker_sets["particle_328 geometry"]
mark=s.place_marker((3895.24, 1462.59, 2833.29), (0.7, 0.7, 0.7), 151.392)
if "particle_329 geometry" not in marker_sets:
  s=new_marker_set('particle_329 geometry')
  marker_sets["particle_329 geometry"]=s
s= marker_sets["particle_329 geometry"]
mark=s.place_marker((3538.95, 1376.59, 2771.26), (0.7, 0.7, 0.7), 173.388)
if "particle_330 geometry" not in marker_sets:
  s=new_marker_set('particle_330 geometry')
  marker_sets["particle_330 geometry"]=s
s= marker_sets["particle_330 geometry"]
mark=s.place_marker((3519.66, 1075.99, 2890.34), (0.7, 0.7, 0.7), 135.825)
if "particle_331 geometry" not in marker_sets:
  s=new_marker_set('particle_331 geometry')
  marker_sets["particle_331 geometry"]=s
s= marker_sets["particle_331 geometry"]
mark=s.place_marker((3691.77, 737.212, 3061.74), (0.7, 0.7, 0.7), 186.839)
if "particle_332 geometry" not in marker_sets:
  s=new_marker_set('particle_332 geometry')
  marker_sets["particle_332 geometry"]=s
s= marker_sets["particle_332 geometry"]
mark=s.place_marker((3932.97, 389.663, 3246.82), (0.7, 0.7, 0.7), 121.189)
if "particle_333 geometry" not in marker_sets:
  s=new_marker_set('particle_333 geometry')
  marker_sets["particle_333 geometry"]=s
s= marker_sets["particle_333 geometry"]
mark=s.place_marker((3896.95, 811.229, 3300.71), (0.7, 0.7, 0.7), 102.916)
if "particle_334 geometry" not in marker_sets:
  s=new_marker_set('particle_334 geometry')
  marker_sets["particle_334 geometry"]=s
s= marker_sets["particle_334 geometry"]
mark=s.place_marker((3739.68, 1393.23, 3454.4), (0.7, 0.7, 0.7), 212.769)
if "particle_335 geometry" not in marker_sets:
  s=new_marker_set('particle_335 geometry')
  marker_sets["particle_335 geometry"]=s
s= marker_sets["particle_335 geometry"]
mark=s.place_marker((3396.55, 1983.25, 3410.61), (0.7, 0.7, 0.7), 173.092)
if "particle_336 geometry" not in marker_sets:
  s=new_marker_set('particle_336 geometry')
  marker_sets["particle_336 geometry"]=s
s= marker_sets["particle_336 geometry"]
mark=s.place_marker((3348.01, 2486.44, 3521.73), (0.7, 0.7, 0.7), 264.502)
if "particle_337 geometry" not in marker_sets:
  s=new_marker_set('particle_337 geometry')
  marker_sets["particle_337 geometry"]=s
s= marker_sets["particle_337 geometry"]
mark=s.place_marker((3634.85, 2875.87, 3824.67), (0.7, 0.7, 0.7), 208.666)
if "particle_338 geometry" not in marker_sets:
  s=new_marker_set('particle_338 geometry')
  marker_sets["particle_338 geometry"]=s
s= marker_sets["particle_338 geometry"]
mark=s.place_marker((3796.83, 3043.13, 4275.54), (0.7, 0.7, 0.7), 186.797)
if "particle_339 geometry" not in marker_sets:
  s=new_marker_set('particle_339 geometry')
  marker_sets["particle_339 geometry"]=s
s= marker_sets["particle_339 geometry"]
mark=s.place_marker((3421.11, 3188.67, 4593.39), (0.7, 0.7, 0.7), 255.534)
if "particle_340 geometry" not in marker_sets:
  s=new_marker_set('particle_340 geometry')
  marker_sets["particle_340 geometry"]=s
s= marker_sets["particle_340 geometry"]
mark=s.place_marker((3317.01, 2981.96, 4960.69), (0.7, 0.7, 0.7), 153.126)
if "particle_341 geometry" not in marker_sets:
  s=new_marker_set('particle_341 geometry')
  marker_sets["particle_341 geometry"]=s
s= marker_sets["particle_341 geometry"]
mark=s.place_marker((3644.34, 3164.59, 5062.09), (0.7, 0.7, 0.7), 165.816)
if "particle_342 geometry" not in marker_sets:
  s=new_marker_set('particle_342 geometry')
  marker_sets["particle_342 geometry"]=s
s= marker_sets["particle_342 geometry"]
mark=s.place_marker((3497.44, 3385.29, 4779.65), (0.7, 0.7, 0.7), 134.429)
if "particle_343 geometry" not in marker_sets:
  s=new_marker_set('particle_343 geometry')
  marker_sets["particle_343 geometry"]=s
s= marker_sets["particle_343 geometry"]
mark=s.place_marker((3544.85, 3290.18, 4399.42), (0.7, 0.7, 0.7), 178.971)
if "particle_344 geometry" not in marker_sets:
  s=new_marker_set('particle_344 geometry')
  marker_sets["particle_344 geometry"]=s
s= marker_sets["particle_344 geometry"]
mark=s.place_marker((3853.58, 2924.9, 4185.93), (0.7, 0.7, 0.7), 189.969)
if "particle_345 geometry" not in marker_sets:
  s=new_marker_set('particle_345 geometry')
  marker_sets["particle_345 geometry"]=s
s= marker_sets["particle_345 geometry"]
mark=s.place_marker((4475.62, 2806.53, 4177.42), (0.7, 0.7, 0.7), 121.359)
if "particle_346 geometry" not in marker_sets:
  s=new_marker_set('particle_346 geometry')
  marker_sets["particle_346 geometry"]=s
s= marker_sets["particle_346 geometry"]
mark=s.place_marker((4634.99, 2360.6, 3883.26), (0.7, 0.7, 0.7), 187.262)
if "particle_347 geometry" not in marker_sets:
  s=new_marker_set('particle_347 geometry')
  marker_sets["particle_347 geometry"]=s
s= marker_sets["particle_347 geometry"]
mark=s.place_marker((4347.84, 1967.72, 3425.26), (0.7, 0.7, 0.7), 164.335)
if "particle_348 geometry" not in marker_sets:
  s=new_marker_set('particle_348 geometry')
  marker_sets["particle_348 geometry"]=s
s= marker_sets["particle_348 geometry"]
mark=s.place_marker((4076.43, 1520.69, 3472.14), (0.7, 0.7, 0.7), 138.363)
if "particle_349 geometry" not in marker_sets:
  s=new_marker_set('particle_349 geometry')
  marker_sets["particle_349 geometry"]=s
s= marker_sets["particle_349 geometry"]
mark=s.place_marker((4004.51, 1141.31, 3434.81), (0.7, 0.7, 0.7), 138.49)
if "particle_350 geometry" not in marker_sets:
  s=new_marker_set('particle_350 geometry')
  marker_sets["particle_350 geometry"]=s
s= marker_sets["particle_350 geometry"]
mark=s.place_marker((4007.89, 1185.04, 3086.18), (0.7, 0.7, 0.7), 116.325)
if "particle_351 geometry" not in marker_sets:
  s=new_marker_set('particle_351 geometry')
  marker_sets["particle_351 geometry"]=s
s= marker_sets["particle_351 geometry"]
mark=s.place_marker((4030.33, 1647.66, 3092.17), (0.7, 0.7, 0.7), 106.511)
if "particle_352 geometry" not in marker_sets:
  s=new_marker_set('particle_352 geometry')
  marker_sets["particle_352 geometry"]=s
s= marker_sets["particle_352 geometry"]
mark=s.place_marker((3988.58, 2120.46, 3393.27), (0.7, 0.7, 0.7), 151.096)
if "particle_353 geometry" not in marker_sets:
  s=new_marker_set('particle_353 geometry')
  marker_sets["particle_353 geometry"]=s
s= marker_sets["particle_353 geometry"]
mark=s.place_marker((4070.93, 2587.83, 3896.95), (0.7, 0.7, 0.7), 240.856)
if "particle_354 geometry" not in marker_sets:
  s=new_marker_set('particle_354 geometry')
  marker_sets["particle_354 geometry"]=s
s= marker_sets["particle_354 geometry"]
mark=s.place_marker((4109.61, 2866.58, 4348.19), (0.7, 0.7, 0.7), 149.7)
if "particle_355 geometry" not in marker_sets:
  s=new_marker_set('particle_355 geometry')
  marker_sets["particle_355 geometry"]=s
s= marker_sets["particle_355 geometry"]
mark=s.place_marker((3933.62, 3131.67, 4500.17), (0.7, 0.7, 0.7), 165.943)
if "particle_356 geometry" not in marker_sets:
  s=new_marker_set('particle_356 geometry')
  marker_sets["particle_356 geometry"]=s
s= marker_sets["particle_356 geometry"]
mark=s.place_marker((3336.68, 3094.6, 4362.82), (0.7, 0.7, 0.7), 178.971)
if "particle_357 geometry" not in marker_sets:
  s=new_marker_set('particle_357 geometry')
  marker_sets["particle_357 geometry"]=s
s= marker_sets["particle_357 geometry"]
mark=s.place_marker((2630.37, 3316.79, 4226.58), (0.7, 0.7, 0.7), 154.945)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
