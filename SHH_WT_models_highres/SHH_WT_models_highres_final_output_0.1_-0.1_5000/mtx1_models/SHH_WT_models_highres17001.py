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
mark=s.place_marker((2179.98, -333.827, 3056.82), (0.7, 0.7, 0.7), 182.271)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((1790.79, -543.354, 3138.45), (0.7, 0.7, 0.7), 258.199)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((1938.19, -185.103, 3200.62), (0.7, 0.7, 0.7), 123.897)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((2203.23, -481.881, 3266.49), (0.7, 0.7, 0.7), 146.739)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((2593.21, -761.4, 3275.68), (0.7, 0.7, 0.7), 179.098)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((2579.1, -205.227, 3014.54), (0.7, 0.7, 0.7), 148.854)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((2699.43, 308.693, 2837.12), (0.7, 0.7, 0.7), 196.357)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((3153.64, 280.152, 3179.11), (0.7, 0.7, 0.7), 166.873)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((3694.33, 192.151, 3482.57), (0.7, 0.7, 0.7), 95.4711)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((3485.65, 371.796, 3153.27), (0.7, 0.7, 0.7), 185.401)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((3052.46, 392.111, 2783.16), (0.7, 0.7, 0.7), 151.984)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((2511.05, 521.692, 2395.28), (0.7, 0.7, 0.7), 185.612)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((2201.13, 360.09, 1997.72), (0.7, 0.7, 0.7), 210.273)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((2045.73, 166.302, 1634.95), (0.7, 0.7, 0.7), 106.892)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((1812.34, 176.492, 1141.17), (0.7, 0.7, 0.7), 202.025)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((1275.27, 194.415, 757.654), (0.7, 0.7, 0.7), 192.169)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((648.904, 252.891, 530.552), (0.7, 0.7, 0.7), 241.11)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((201.944, 403.323, 605.213), (0.7, 0.7, 0.7), 128.465)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((-248.611, 272.25, 748.965), (0.7, 0.7, 0.7), 217.38)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((-818.367, -137.825, 763.936), (0.7, 0.7, 0.7), 184.555)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((-381.977, 277.057, 976.432), (0.7, 0.7, 0.7), 140.055)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((-67.387, 484.453, 774.171), (0.7, 0.7, 0.7), 169.708)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((29.6081, 657.911, 410.37), (0.7, 0.7, 0.7), 184.639)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((25.4878, 961.79, 521.626), (0.7, 0.7, 0.7), 119.286)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((-208.117, 1022.45, 711.442), (0.7, 0.7, 0.7), 147.754)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((-219.475, 836.755, 979.206), (0.7, 0.7, 0.7), 171.4)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((204.761, 823.447, 1033.35), (0.7, 0.7, 0.7), 156.341)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((603.624, 951.206, 1450.11), (0.7, 0.7, 0.7), 186.501)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((973.39, 1144.38, 1796.92), (0.7, 0.7, 0.7), 308.325)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((1368.01, 1119.36, 1858.78), (0.7, 0.7, 0.7), 138.617)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((1615.83, 1250.91, 1768.78), (0.7, 0.7, 0.7), 130.03)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((1321.29, 1231.92, 1611.17), (0.7, 0.7, 0.7), 156.552)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((1240.63, 1061.6, 1872.98), (0.7, 0.7, 0.7), 183.244)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((1115.89, 942.345, 2080.74), (0.7, 0.7, 0.7), 181.382)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((958.463, 1015.89, 2170.41), (0.7, 0.7, 0.7), 101.943)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((657.396, 870.849, 2313.08), (1, 0.7, 0), 138.913)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((394.705, 1886.95, 2621.54), (0.7, 0.7, 0.7), 221.737)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((687.029, 2662.44, 2969.42), (0.7, 0.7, 0.7), 256.38)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((1164.57, 2937.59, 3498.09), (0.7, 0.7, 0.7), 221.694)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((1820.91, 2623.38, 3688.44), (0.7, 0.7, 0.7), 259.341)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((2058.86, 2279.62, 3036.01), (0.7, 0.7, 0.7), 117.89)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((1910.27, 1858.08, 2344.54), (0.7, 0.7, 0.7), 116.071)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((1538.98, 1587.72, 2269.23), (0.7, 0.7, 0.7), 268.224)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((1576.3, 1623.46, 2579.92), (0.7, 0.7, 0.7), 386.918)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((2033.97, 1705.79, 2995.97), (0.7, 0.7, 0.7), 121.316)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((2070.36, 1697.63, 3426.19), (0.7, 0.7, 0.7), 138.363)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((1453.7, 1456.52, 3141.06), (1, 0.7, 0), 175.207)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((1733.47, 1560.95, 3796.59), (0.7, 0.7, 0.7), 131.468)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((1807.78, 1702.92, 4516), (0.7, 0.7, 0.7), 287.894)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((1725.1, 2066.96, 4122.19), (0.7, 0.7, 0.7), 88.1109)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((1700.05, 2079.51, 3519.82), (0.7, 0.7, 0.7), 145.385)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((1790.07, 2133.36, 3345.93), (0.7, 0.7, 0.7), 155.452)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((1962.28, 2365.24, 3903.4), (0.7, 0.7, 0.7), 145.512)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((2169.43, 2556.72, 4335.77), (0.7, 0.7, 0.7), 99.9972)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((2437.22, 2673.91, 4676.12), (0.7, 0.7, 0.7), 327.529)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((2741.4, 2597.77, 4119.57), (0.7, 0.7, 0.7), 137.983)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((2558.16, 2589.57, 3645.35), (0.7, 0.7, 0.7), 83.3733)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((2256.99, 2529.84, 3160.92), (0.7, 0.7, 0.7), 101.562)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((1925.48, 2363.73, 2784.41), (0.7, 0.7, 0.7), 165.689)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((1650.32, 2359.14, 2932.78), (0.7, 0.7, 0.7), 136.925)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((1613.25, 2346.21, 3031.53), (0.7, 0.7, 0.7), 123.389)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((1908.96, 2603.22, 3269.06), (0.7, 0.7, 0.7), 184.47)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((2296.8, 3153.22, 3700.49), (0.7, 0.7, 0.7), 148.473)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((2685.06, 3866.36, 4267.02), (0.7, 0.7, 0.7), 241.406)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((2868.4, 3307.85, 3972.09), (0.7, 0.7, 0.7), 182.736)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((2804.6, 2881.76, 3817.88), (0.7, 0.7, 0.7), 166.62)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((2521.73, 2919.23, 3723.68), (0.7, 0.7, 0.7), 113.872)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((2308.67, 2716.16, 3581.3), (0.7, 0.7, 0.7), 110.065)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((2004.45, 2486.81, 3622.43), (0.7, 0.7, 0.7), 150.08)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((1649.6, 2232.75, 3802.04), (0.7, 0.7, 0.7), 118.525)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((1214.67, 2110.91, 4092.49), (0.7, 0.7, 0.7), 163.955)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((1120.25, 2292.31, 4401.05), (0.7, 0.7, 0.7), 170.131)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((1678.27, 2798.13, 4478.64), (0.7, 0.7, 0.7), 78.2127)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((2374.63, 3245.57, 4521.19), (0.7, 0.7, 0.7), 251.896)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((3023.57, 3435.26, 4469.53), (0.7, 0.7, 0.7), 167.55)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((3400.33, 3387.03, 4305.9), (0.7, 0.7, 0.7), 167.846)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((3130.36, 3838.64, 4287.69), (0.7, 0.7, 0.7), 259.68)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((2706.58, 3909.72, 4490.95), (0.7, 0.7, 0.7), 80.2854)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((2757.12, 3937.05, 4689.85), (0.7, 0.7, 0.7), 82.4427)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((2909.55, 4257.62, 4737.8), (0.7, 0.7, 0.7), 212.811)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((2900.26, 4472.58, 4035.36), (0.7, 0.7, 0.7), 176.391)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((2754.79, 4067.13, 3439.27), (0.7, 0.7, 0.7), 99.3204)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((2416.05, 3638.28, 3189.19), (0.7, 0.7, 0.7), 166.62)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((2149.46, 3608.5, 3069.36), (0.7, 0.7, 0.7), 102.831)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((2495.87, 4365.74, 3449.04), (0.7, 0.7, 0.7), 65.0997)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((2722.67, 3971.52, 3706.46), (0.7, 0.7, 0.7), 92.1294)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((2793.13, 3420.34, 3736.57), (0.7, 0.7, 0.7), 194.791)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((2972.98, 3059.66, 3731.77), (0.7, 0.7, 0.7), 120.766)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((3364.63, 3441.58, 3929.34), (0.7, 0.7, 0.7), 217.803)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((3005.53, 3570.4, 4071.76), (0.7, 0.7, 0.7), 115.775)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((2668.55, 3343.59, 4195.56), (0.7, 0.7, 0.7), 115.648)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((2636.39, 3121.07, 3946.67), (0.7, 0.7, 0.7), 83.8386)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((2958, 2939.86, 3834.17), (0.7, 0.7, 0.7), 124.32)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((3252.14, 2601.85, 3821.73), (0.7, 0.7, 0.7), 185.993)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((3516.7, 2243.98, 4254.09), (0.7, 0.7, 0.7), 238.826)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((3470.14, 2165.58, 4796.51), (0.7, 0.7, 0.7), 128.465)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((2906.67, 2476.01, 4742.08), (0.7, 0.7, 0.7), 203.209)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((2747.83, 2752.71, 4335.66), (0.7, 0.7, 0.7), 160.486)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((3073.77, 2784.08, 4216.56), (0.7, 0.7, 0.7), 149.277)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((3275.18, 2997.44, 4660.83), (0.7, 0.7, 0.7), 35.7435)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((2466.41, 2956.47, 4059.38), (0.7, 0.7, 0.7), 98.3898)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((1791.01, 2850.58, 3242.97), (0.7, 0.7, 0.7), 188.404)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((1810.11, 2792.74, 2740.45), (0.7, 0.7, 0.7), 110.318)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((2056.1, 3040.33, 2908.78), (0.7, 0.7, 0.7), 127.534)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((2256.69, 3165.63, 3201.35), (0.7, 0.7, 0.7), 91.368)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((2436.76, 3184.46, 3542.55), (0.7, 0.7, 0.7), 131.045)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((2548.03, 3002.36, 3896.64), (0.7, 0.7, 0.7), 143.608)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((2890.34, 2821.94, 3957.51), (0.7, 0.7, 0.7), 135.783)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((3198.24, 2690.75, 3966.27), (0.7, 0.7, 0.7), 92.5947)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((3234.06, 2757.22, 3697.56), (0.7, 0.7, 0.7), 150.123)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((3315.78, 2625.16, 3555.45), (0.7, 0.7, 0.7), 121.57)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((3634.85, 2686.71, 3507.25), (0.7, 0.7, 0.7), 104.777)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((3476.91, 2598.22, 3161.86), (0.7, 0.7, 0.7), 114.844)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((3304.45, 2504.23, 2795.46), (0.7, 0.7, 0.7), 150.588)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((2930.04, 2550.2, 2812.12), (0.7, 0.7, 0.7), 103.55)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((2675.57, 2934.29, 2948.82), (0.7, 0.7, 0.7), 215.392)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((2317.56, 3286.53, 2992.31), (0.7, 0.7, 0.7), 99.9126)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((2445.35, 4019.32, 3194.4), (0.7, 0.7, 0.7), 99.7857)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((2510.25, 4508.58, 3497.28), (0.7, 0.7, 0.7), 109.98)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((2661.27, 4098.94, 3198.37), (0.7, 0.7, 0.7), 102.831)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((2660.72, 3751.52, 3114.04), (0.7, 0.7, 0.7), 103.593)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((2689.85, 3365.12, 3228.34), (0.7, 0.7, 0.7), 173.472)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((2870.43, 3345.94, 3692.88), (0.7, 0.7, 0.7), 113.575)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((3039.31, 3017.56, 3830.07), (0.7, 0.7, 0.7), 128.296)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((3323.08, 2757.2, 3936.5), (0.7, 0.7, 0.7), 145.004)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((3586.26, 2349.6, 3888.03), (0.7, 0.7, 0.7), 148.261)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((3978.78, 2007.58, 4186.48), (0.7, 0.7, 0.7), 127.704)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((4222.08, 1759.72, 4639.3), (0.7, 0.7, 0.7), 129.607)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((3867.8, 2119.35, 4761.11), (0.7, 0.7, 0.7), 139.759)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((3305.41, 2487.2, 4649.09), (0.7, 0.7, 0.7), 118.567)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((3229.29, 2868.5, 4445.64), (0.7, 0.7, 0.7), 136.164)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((3109.43, 3116.1, 4080.46), (0.7, 0.7, 0.7), 121.655)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((3139.24, 3293.09, 3690.33), (0.7, 0.7, 0.7), 127.492)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((3346.45, 3629.17, 3522.3), (0.7, 0.7, 0.7), 138.617)
if "particle_134 geometry" not in marker_sets:
  s=new_marker_set('particle_134 geometry')
  marker_sets["particle_134 geometry"]=s
s= marker_sets["particle_134 geometry"]
mark=s.place_marker((3349.26, 3675.19, 3157.39), (0.7, 0.7, 0.7), 120.766)
if "particle_135 geometry" not in marker_sets:
  s=new_marker_set('particle_135 geometry')
  marker_sets["particle_135 geometry"]=s
s= marker_sets["particle_135 geometry"]
mark=s.place_marker((3102.71, 3712.48, 2954.4), (0.7, 0.7, 0.7), 145.893)
if "particle_136 geometry" not in marker_sets:
  s=new_marker_set('particle_136 geometry')
  marker_sets["particle_136 geometry"]=s
s= marker_sets["particle_136 geometry"]
mark=s.place_marker((2730.38, 3417.21, 3020.1), (0.7, 0.7, 0.7), 185.02)
if "particle_137 geometry" not in marker_sets:
  s=new_marker_set('particle_137 geometry')
  marker_sets["particle_137 geometry"]=s
s= marker_sets["particle_137 geometry"]
mark=s.place_marker((2412.23, 3016.11, 2886.06), (0.7, 0.7, 0.7), 221.314)
if "particle_138 geometry" not in marker_sets:
  s=new_marker_set('particle_138 geometry')
  marker_sets["particle_138 geometry"]=s
s= marker_sets["particle_138 geometry"]
mark=s.place_marker((2334.92, 2587.06, 2654.56), (0.7, 0.7, 0.7), 165.139)
if "particle_139 geometry" not in marker_sets:
  s=new_marker_set('particle_139 geometry')
  marker_sets["particle_139 geometry"]=s
s= marker_sets["particle_139 geometry"]
mark=s.place_marker((2373.11, 2439.03, 2818.38), (0.7, 0.7, 0.7), 179.437)
if "particle_140 geometry" not in marker_sets:
  s=new_marker_set('particle_140 geometry')
  marker_sets["particle_140 geometry"]=s
s= marker_sets["particle_140 geometry"]
mark=s.place_marker((2282.97, 2816.58, 2992.64), (0.7, 0.7, 0.7), 137.898)
if "particle_141 geometry" not in marker_sets:
  s=new_marker_set('particle_141 geometry')
  marker_sets["particle_141 geometry"]=s
s= marker_sets["particle_141 geometry"]
mark=s.place_marker((2278.24, 3128.61, 3165.11), (0.7, 0.7, 0.7), 124.658)
if "particle_142 geometry" not in marker_sets:
  s=new_marker_set('particle_142 geometry')
  marker_sets["particle_142 geometry"]=s
s= marker_sets["particle_142 geometry"]
mark=s.place_marker((2536.56, 3350.66, 3137), (0.7, 0.7, 0.7), 97.7553)
if "particle_143 geometry" not in marker_sets:
  s=new_marker_set('particle_143 geometry')
  marker_sets["particle_143 geometry"]=s
s= marker_sets["particle_143 geometry"]
mark=s.place_marker((2718.37, 3598.32, 3133.59), (0.7, 0.7, 0.7), 92.9331)
if "particle_144 geometry" not in marker_sets:
  s=new_marker_set('particle_144 geometry')
  marker_sets["particle_144 geometry"]=s
s= marker_sets["particle_144 geometry"]
mark=s.place_marker((2834.08, 3910.3, 3226.17), (0.7, 0.7, 0.7), 123.135)
if "particle_145 geometry" not in marker_sets:
  s=new_marker_set('particle_145 geometry')
  marker_sets["particle_145 geometry"]=s
s= marker_sets["particle_145 geometry"]
mark=s.place_marker((2558.41, 3654.44, 3110.14), (0.7, 0.7, 0.7), 125.716)
if "particle_146 geometry" not in marker_sets:
  s=new_marker_set('particle_146 geometry')
  marker_sets["particle_146 geometry"]=s
s= marker_sets["particle_146 geometry"]
mark=s.place_marker((2519.54, 3352.86, 3039.65), (0.7, 0.7, 0.7), 127.534)
if "particle_147 geometry" not in marker_sets:
  s=new_marker_set('particle_147 geometry')
  marker_sets["particle_147 geometry"]=s
s= marker_sets["particle_147 geometry"]
mark=s.place_marker((2653.71, 3168.53, 3225.27), (0.7, 0.7, 0.7), 94.9212)
if "particle_148 geometry" not in marker_sets:
  s=new_marker_set('particle_148 geometry')
  marker_sets["particle_148 geometry"]=s
s= marker_sets["particle_148 geometry"]
mark=s.place_marker((2490.67, 2768.68, 3119.96), (0.7, 0.7, 0.7), 137.644)
if "particle_149 geometry" not in marker_sets:
  s=new_marker_set('particle_149 geometry')
  marker_sets["particle_149 geometry"]=s
s= marker_sets["particle_149 geometry"]
mark=s.place_marker((2469.33, 2422.79, 3056.34), (0.7, 0.7, 0.7), 149.277)
if "particle_150 geometry" not in marker_sets:
  s=new_marker_set('particle_150 geometry')
  marker_sets["particle_150 geometry"]=s
s= marker_sets["particle_150 geometry"]
mark=s.place_marker((2739.41, 2544.53, 2865.33), (0.7, 0.7, 0.7), 103.677)
if "particle_151 geometry" not in marker_sets:
  s=new_marker_set('particle_151 geometry')
  marker_sets["particle_151 geometry"]=s
s= marker_sets["particle_151 geometry"]
mark=s.place_marker((3186.69, 2727.19, 2835.64), (0.7, 0.7, 0.7), 99.6588)
if "particle_152 geometry" not in marker_sets:
  s=new_marker_set('particle_152 geometry')
  marker_sets["particle_152 geometry"]=s
s= marker_sets["particle_152 geometry"]
mark=s.place_marker((3550.67, 2810.72, 2844.83), (0.7, 0.7, 0.7), 134.133)
if "particle_153 geometry" not in marker_sets:
  s=new_marker_set('particle_153 geometry')
  marker_sets["particle_153 geometry"]=s
s= marker_sets["particle_153 geometry"]
mark=s.place_marker((3289.36, 2926.57, 2686.34), (0.7, 0.7, 0.7), 173.007)
if "particle_154 geometry" not in marker_sets:
  s=new_marker_set('particle_154 geometry')
  marker_sets["particle_154 geometry"]=s
s= marker_sets["particle_154 geometry"]
mark=s.place_marker((2785.25, 2670.29, 2626.04), (0.7, 0.7, 0.7), 141.028)
if "particle_155 geometry" not in marker_sets:
  s=new_marker_set('particle_155 geometry')
  marker_sets["particle_155 geometry"]=s
s= marker_sets["particle_155 geometry"]
mark=s.place_marker((2337.15, 2531.18, 2657.9), (0.7, 0.7, 0.7), 161.121)
if "particle_156 geometry" not in marker_sets:
  s=new_marker_set('particle_156 geometry')
  marker_sets["particle_156 geometry"]=s
s= marker_sets["particle_156 geometry"]
mark=s.place_marker((2214.4, 2506.35, 2986.37), (0.7, 0.7, 0.7), 119.582)
if "particle_157 geometry" not in marker_sets:
  s=new_marker_set('particle_157 geometry')
  marker_sets["particle_157 geometry"]=s
s= marker_sets["particle_157 geometry"]
mark=s.place_marker((2413.37, 2775.14, 3209.99), (0.7, 0.7, 0.7), 137.094)
if "particle_158 geometry" not in marker_sets:
  s=new_marker_set('particle_158 geometry')
  marker_sets["particle_158 geometry"]=s
s= marker_sets["particle_158 geometry"]
mark=s.place_marker((2519.97, 3221.93, 3417.98), (0.7, 0.7, 0.7), 149.234)
if "particle_159 geometry" not in marker_sets:
  s=new_marker_set('particle_159 geometry')
  marker_sets["particle_159 geometry"]=s
s= marker_sets["particle_159 geometry"]
mark=s.place_marker((2177.85, 3408.82, 3241.95), (0.7, 0.7, 0.7), 151.011)
if "particle_160 geometry" not in marker_sets:
  s=new_marker_set('particle_160 geometry')
  marker_sets["particle_160 geometry"]=s
s= marker_sets["particle_160 geometry"]
mark=s.place_marker((1834.73, 3329.39, 2882.92), (0.7, 0.7, 0.7), 184.216)
if "particle_161 geometry" not in marker_sets:
  s=new_marker_set('particle_161 geometry')
  marker_sets["particle_161 geometry"]=s
s= marker_sets["particle_161 geometry"]
mark=s.place_marker((2018.16, 3403.55, 2517.63), (0.7, 0.7, 0.7), 170.596)
if "particle_162 geometry" not in marker_sets:
  s=new_marker_set('particle_162 geometry')
  marker_sets["particle_162 geometry"]=s
s= marker_sets["particle_162 geometry"]
mark=s.place_marker((2369.23, 3907.06, 2659.66), (0.7, 0.7, 0.7), 215.603)
if "particle_163 geometry" not in marker_sets:
  s=new_marker_set('particle_163 geometry')
  marker_sets["particle_163 geometry"]=s
s= marker_sets["particle_163 geometry"]
mark=s.place_marker((2801.39, 4613.94, 2947.77), (0.7, 0.7, 0.7), 79.0164)
if "particle_164 geometry" not in marker_sets:
  s=new_marker_set('particle_164 geometry')
  marker_sets["particle_164 geometry"]=s
s= marker_sets["particle_164 geometry"]
mark=s.place_marker((3121.29, 4589.76, 2825.01), (0.7, 0.7, 0.7), 77.2821)
if "particle_165 geometry" not in marker_sets:
  s=new_marker_set('particle_165 geometry')
  marker_sets["particle_165 geometry"]=s
s= marker_sets["particle_165 geometry"]
mark=s.place_marker((3195.91, 4243.61, 2798.03), (0.7, 0.7, 0.7), 188.658)
if "particle_166 geometry" not in marker_sets:
  s=new_marker_set('particle_166 geometry')
  marker_sets["particle_166 geometry"]=s
s= marker_sets["particle_166 geometry"]
mark=s.place_marker((3318.97, 4157.67, 2550.02), (0.7, 0.7, 0.7), 115.437)
if "particle_167 geometry" not in marker_sets:
  s=new_marker_set('particle_167 geometry')
  marker_sets["particle_167 geometry"]=s
s= marker_sets["particle_167 geometry"]
mark=s.place_marker((2937.72, 3689.88, 2618.6), (0.7, 0.7, 0.7), 88.4916)
if "particle_168 geometry" not in marker_sets:
  s=new_marker_set('particle_168 geometry')
  marker_sets["particle_168 geometry"]=s
s= marker_sets["particle_168 geometry"]
mark=s.place_marker((2543.81, 3205.69, 2696.88), (0.7, 0.7, 0.7), 108.88)
if "particle_169 geometry" not in marker_sets:
  s=new_marker_set('particle_169 geometry')
  marker_sets["particle_169 geometry"]=s
s= marker_sets["particle_169 geometry"]
mark=s.place_marker((2274.11, 3049.33, 2871.08), (0.7, 0.7, 0.7), 172.119)
if "particle_170 geometry" not in marker_sets:
  s=new_marker_set('particle_170 geometry')
  marker_sets["particle_170 geometry"]=s
s= marker_sets["particle_170 geometry"]
mark=s.place_marker((2476.03, 3475.89, 2984.19), (0.7, 0.7, 0.7), 139.505)
if "particle_171 geometry" not in marker_sets:
  s=new_marker_set('particle_171 geometry')
  marker_sets["particle_171 geometry"]=s
s= marker_sets["particle_171 geometry"]
mark=s.place_marker((2684.32, 3899.06, 3101.94), (0.7, 0.7, 0.7), 92.7639)
if "particle_172 geometry" not in marker_sets:
  s=new_marker_set('particle_172 geometry')
  marker_sets["particle_172 geometry"]=s
s= marker_sets["particle_172 geometry"]
mark=s.place_marker((2473.88, 3900.58, 3227.48), (0.7, 0.7, 0.7), 89.8452)
if "particle_173 geometry" not in marker_sets:
  s=new_marker_set('particle_173 geometry')
  marker_sets["particle_173 geometry"]=s
s= marker_sets["particle_173 geometry"]
mark=s.place_marker((2567.6, 3833.87, 2980.52), (0.7, 0.7, 0.7), 149.446)
if "particle_174 geometry" not in marker_sets:
  s=new_marker_set('particle_174 geometry')
  marker_sets["particle_174 geometry"]=s
s= marker_sets["particle_174 geometry"]
mark=s.place_marker((2819.31, 3964.63, 2794.88), (0.7, 0.7, 0.7), 126.858)
if "particle_175 geometry" not in marker_sets:
  s=new_marker_set('particle_175 geometry')
  marker_sets["particle_175 geometry"]=s
s= marker_sets["particle_175 geometry"]
mark=s.place_marker((2992.91, 4106.04, 3052.19), (0.7, 0.7, 0.7), 106.046)
if "particle_176 geometry" not in marker_sets:
  s=new_marker_set('particle_176 geometry')
  marker_sets["particle_176 geometry"]=s
s= marker_sets["particle_176 geometry"]
mark=s.place_marker((2859.3, 4028.2, 3542.4), (0.7, 0.7, 0.7), 156.298)
if "particle_177 geometry" not in marker_sets:
  s=new_marker_set('particle_177 geometry')
  marker_sets["particle_177 geometry"]=s
s= marker_sets["particle_177 geometry"]
mark=s.place_marker((2798.04, 3838.48, 4123.47), (0.7, 0.7, 0.7), 231.212)
if "particle_178 geometry" not in marker_sets:
  s=new_marker_set('particle_178 geometry')
  marker_sets["particle_178 geometry"]=s
s= marker_sets["particle_178 geometry"]
mark=s.place_marker((2387.14, 3493.14, 4299.73), (0.7, 0.7, 0.7), 88.4916)
if "particle_179 geometry" not in marker_sets:
  s=new_marker_set('particle_179 geometry')
  marker_sets["particle_179 geometry"]=s
s= marker_sets["particle_179 geometry"]
mark=s.place_marker((2099.68, 3234.47, 4023.68), (0.7, 0.7, 0.7), 111.334)
if "particle_180 geometry" not in marker_sets:
  s=new_marker_set('particle_180 geometry')
  marker_sets["particle_180 geometry"]=s
s= marker_sets["particle_180 geometry"]
mark=s.place_marker((2008.71, 3038.15, 3434.87), (0.7, 0.7, 0.7), 127.619)
if "particle_181 geometry" not in marker_sets:
  s=new_marker_set('particle_181 geometry')
  marker_sets["particle_181 geometry"]=s
s= marker_sets["particle_181 geometry"]
mark=s.place_marker((1933.43, 2916.67, 2988.27), (0.7, 0.7, 0.7), 230.746)
if "particle_182 geometry" not in marker_sets:
  s=new_marker_set('particle_182 geometry')
  marker_sets["particle_182 geometry"]=s
s= marker_sets["particle_182 geometry"]
mark=s.place_marker((2136.77, 3230.56, 3112.84), (0.7, 0.7, 0.7), 124.573)
if "particle_183 geometry" not in marker_sets:
  s=new_marker_set('particle_183 geometry')
  marker_sets["particle_183 geometry"]=s
s= marker_sets["particle_183 geometry"]
mark=s.place_marker((2367.51, 3747.91, 3361.26), (0.7, 0.7, 0.7), 124.489)
if "particle_184 geometry" not in marker_sets:
  s=new_marker_set('particle_184 geometry')
  marker_sets["particle_184 geometry"]=s
s= marker_sets["particle_184 geometry"]
mark=s.place_marker((2693.23, 3898.29, 3229.76), (0.7, 0.7, 0.7), 196.61)
if "particle_185 geometry" not in marker_sets:
  s=new_marker_set('particle_185 geometry')
  marker_sets["particle_185 geometry"]=s
s= marker_sets["particle_185 geometry"]
mark=s.place_marker((2664.84, 3631.86, 3320.11), (0.7, 0.7, 0.7), 134.049)
if "particle_186 geometry" not in marker_sets:
  s=new_marker_set('particle_186 geometry')
  marker_sets["particle_186 geometry"]=s
s= marker_sets["particle_186 geometry"]
mark=s.place_marker((2442.61, 3827.53, 3396.73), (0.7, 0.7, 0.7), 141.493)
if "particle_187 geometry" not in marker_sets:
  s=new_marker_set('particle_187 geometry')
  marker_sets["particle_187 geometry"]=s
s= marker_sets["particle_187 geometry"]
mark=s.place_marker((2375.17, 4183.92, 3595.34), (0.7, 0.7, 0.7), 172.203)
if "particle_188 geometry" not in marker_sets:
  s=new_marker_set('particle_188 geometry')
  marker_sets["particle_188 geometry"]=s
s= marker_sets["particle_188 geometry"]
mark=s.place_marker((2762.75, 3869.53, 3177.13), (0.7, 0.7, 0.7), 271.354)
if "particle_189 geometry" not in marker_sets:
  s=new_marker_set('particle_189 geometry')
  marker_sets["particle_189 geometry"]=s
s= marker_sets["particle_189 geometry"]
mark=s.place_marker((3092.96, 3498.15, 3093.59), (0.7, 0.7, 0.7), 97.0785)
if "particle_190 geometry" not in marker_sets:
  s=new_marker_set('particle_190 geometry')
  marker_sets["particle_190 geometry"]=s
s= marker_sets["particle_190 geometry"]
mark=s.place_marker((3345.92, 3257.63, 3290.63), (0.7, 0.7, 0.7), 151.857)
if "particle_191 geometry" not in marker_sets:
  s=new_marker_set('particle_191 geometry')
  marker_sets["particle_191 geometry"]=s
s= marker_sets["particle_191 geometry"]
mark=s.place_marker((3743.54, 2869.35, 3238.95), (0.7, 0.7, 0.7), 199.233)
if "particle_192 geometry" not in marker_sets:
  s=new_marker_set('particle_192 geometry')
  marker_sets["particle_192 geometry"]=s
s= marker_sets["particle_192 geometry"]
mark=s.place_marker((3604.38, 2405.2, 2968.97), (0.7, 0.7, 0.7), 118.863)
if "particle_193 geometry" not in marker_sets:
  s=new_marker_set('particle_193 geometry')
  marker_sets["particle_193 geometry"]=s
s= marker_sets["particle_193 geometry"]
mark=s.place_marker((3724.73, 2022.28, 3043.94), (0.7, 0.7, 0.7), 172.415)
if "particle_194 geometry" not in marker_sets:
  s=new_marker_set('particle_194 geometry')
  marker_sets["particle_194 geometry"]=s
s= marker_sets["particle_194 geometry"]
mark=s.place_marker((4090.07, 1866.48, 3306.34), (0.7, 0.7, 0.7), 134.26)
if "particle_195 geometry" not in marker_sets:
  s=new_marker_set('particle_195 geometry')
  marker_sets["particle_195 geometry"]=s
s= marker_sets["particle_195 geometry"]
mark=s.place_marker((4879.94, 1790.91, 3772), (0.7, 0.7, 0.7), 139.548)
if "particle_196 geometry" not in marker_sets:
  s=new_marker_set('particle_196 geometry')
  marker_sets["particle_196 geometry"]=s
s= marker_sets["particle_196 geometry"]
mark=s.place_marker((4629.86, 2132.8, 4148.85), (0.7, 0.7, 0.7), 196.526)
if "particle_197 geometry" not in marker_sets:
  s=new_marker_set('particle_197 geometry')
  marker_sets["particle_197 geometry"]=s
s= marker_sets["particle_197 geometry"]
mark=s.place_marker((3937.79, 2538.16, 4108.61), (0.7, 0.7, 0.7), 136.206)
if "particle_198 geometry" not in marker_sets:
  s=new_marker_set('particle_198 geometry')
  marker_sets["particle_198 geometry"]=s
s= marker_sets["particle_198 geometry"]
mark=s.place_marker((3009.77, 2546.36, 3756.97), (0.7, 0.7, 0.7), 152.322)
if "particle_199 geometry" not in marker_sets:
  s=new_marker_set('particle_199 geometry')
  marker_sets["particle_199 geometry"]=s
s= marker_sets["particle_199 geometry"]
mark=s.place_marker((2472.94, 2596.65, 3362.42), (0.7, 0.7, 0.7), 126.054)
if "particle_200 geometry" not in marker_sets:
  s=new_marker_set('particle_200 geometry')
  marker_sets["particle_200 geometry"]=s
s= marker_sets["particle_200 geometry"]
mark=s.place_marker((2461.18, 3022.91, 3349.43), (0.7, 0.7, 0.7), 164.378)
if "particle_201 geometry" not in marker_sets:
  s=new_marker_set('particle_201 geometry')
  marker_sets["particle_201 geometry"]=s
s= marker_sets["particle_201 geometry"]
mark=s.place_marker((2691.56, 3393.1, 3257.24), (0.7, 0.7, 0.7), 122.205)
if "particle_202 geometry" not in marker_sets:
  s=new_marker_set('particle_202 geometry')
  marker_sets["particle_202 geometry"]=s
s= marker_sets["particle_202 geometry"]
mark=s.place_marker((2974.66, 3633.05, 3021.83), (0.7, 0.7, 0.7), 134.979)
if "particle_203 geometry" not in marker_sets:
  s=new_marker_set('particle_203 geometry')
  marker_sets["particle_203 geometry"]=s
s= marker_sets["particle_203 geometry"]
mark=s.place_marker((3028.76, 3393.48, 2748.89), (0.7, 0.7, 0.7), 136.375)
if "particle_204 geometry" not in marker_sets:
  s=new_marker_set('particle_204 geometry')
  marker_sets["particle_204 geometry"]=s
s= marker_sets["particle_204 geometry"]
mark=s.place_marker((3040.25, 3442.71, 2974.75), (0.7, 0.7, 0.7), 151.688)
if "particle_205 geometry" not in marker_sets:
  s=new_marker_set('particle_205 geometry')
  marker_sets["particle_205 geometry"]=s
s= marker_sets["particle_205 geometry"]
mark=s.place_marker((2933.43, 3690.09, 2884.55), (0.7, 0.7, 0.7), 116.156)
if "particle_206 geometry" not in marker_sets:
  s=new_marker_set('particle_206 geometry')
  marker_sets["particle_206 geometry"]=s
s= marker_sets["particle_206 geometry"]
mark=s.place_marker((2516.02, 3149.53, 2749.28), (0.7, 0.7, 0.7), 122.839)
if "particle_207 geometry" not in marker_sets:
  s=new_marker_set('particle_207 geometry')
  marker_sets["particle_207 geometry"]=s
s= marker_sets["particle_207 geometry"]
mark=s.place_marker((2255.43, 2726.29, 2918.36), (0.7, 0.7, 0.7), 164.716)
if "particle_208 geometry" not in marker_sets:
  s=new_marker_set('particle_208 geometry')
  marker_sets["particle_208 geometry"]=s
s= marker_sets["particle_208 geometry"]
mark=s.place_marker((2743.29, 2988.77, 3583.99), (0.7, 0.7, 0.7), 303.672)
if "particle_209 geometry" not in marker_sets:
  s=new_marker_set('particle_209 geometry')
  marker_sets["particle_209 geometry"]=s
s= marker_sets["particle_209 geometry"]
mark=s.place_marker((3598.08, 3487.86, 3986.01), (0.7, 0.7, 0.7), 220.298)
if "particle_210 geometry" not in marker_sets:
  s=new_marker_set('particle_210 geometry')
  marker_sets["particle_210 geometry"]=s
s= marker_sets["particle_210 geometry"]
mark=s.place_marker((3439.09, 3928.97, 3545.31), (0.7, 0.7, 0.7), 175.883)
if "particle_211 geometry" not in marker_sets:
  s=new_marker_set('particle_211 geometry')
  marker_sets["particle_211 geometry"]=s
s= marker_sets["particle_211 geometry"]
mark=s.place_marker((2930.63, 4345.45, 3305.58), (0.7, 0.7, 0.7), 233.581)
if "particle_212 geometry" not in marker_sets:
  s=new_marker_set('particle_212 geometry')
  marker_sets["particle_212 geometry"]=s
s= marker_sets["particle_212 geometry"]
mark=s.place_marker((2143.43, 4351.48, 3395.09), (0.7, 0.7, 0.7), 231.127)
if "particle_213 geometry" not in marker_sets:
  s=new_marker_set('particle_213 geometry')
  marker_sets["particle_213 geometry"]=s
s= marker_sets["particle_213 geometry"]
mark=s.place_marker((1649.92, 4568.88, 3057.09), (0.7, 0.7, 0.7), 247.413)
if "particle_214 geometry" not in marker_sets:
  s=new_marker_set('particle_214 geometry')
  marker_sets["particle_214 geometry"]=s
s= marker_sets["particle_214 geometry"]
mark=s.place_marker((1514.7, 4874.1, 2495.85), (0.7, 0.7, 0.7), 200.206)
if "particle_215 geometry" not in marker_sets:
  s=new_marker_set('particle_215 geometry')
  marker_sets["particle_215 geometry"]=s
s= marker_sets["particle_215 geometry"]
mark=s.place_marker((1803.16, 4944.04, 2192.39), (0.7, 0.7, 0.7), 150.419)
if "particle_216 geometry" not in marker_sets:
  s=new_marker_set('particle_216 geometry')
  marker_sets["particle_216 geometry"]=s
s= marker_sets["particle_216 geometry"]
mark=s.place_marker((1627.38, 4360.18, 2238.85), (0.7, 0.7, 0.7), 140.14)
if "particle_217 geometry" not in marker_sets:
  s=new_marker_set('particle_217 geometry')
  marker_sets["particle_217 geometry"]=s
s= marker_sets["particle_217 geometry"]
mark=s.place_marker((1312.19, 4102.39, 2392.31), (0.7, 0.7, 0.7), 132.949)
if "particle_218 geometry" not in marker_sets:
  s=new_marker_set('particle_218 geometry')
  marker_sets["particle_218 geometry"]=s
s= marker_sets["particle_218 geometry"]
mark=s.place_marker((1195.81, 3772.72, 2504.05), (0.7, 0.7, 0.7), 141.113)
if "particle_219 geometry" not in marker_sets:
  s=new_marker_set('particle_219 geometry')
  marker_sets["particle_219 geometry"]=s
s= marker_sets["particle_219 geometry"]
mark=s.place_marker((1295.73, 3797.59, 2858.69), (0.7, 0.7, 0.7), 171.526)
if "particle_220 geometry" not in marker_sets:
  s=new_marker_set('particle_220 geometry')
  marker_sets["particle_220 geometry"]=s
s= marker_sets["particle_220 geometry"]
mark=s.place_marker((1632.96, 4080.86, 3295.85), (0.7, 0.7, 0.7), 326.937)
if "particle_221 geometry" not in marker_sets:
  s=new_marker_set('particle_221 geometry')
  marker_sets["particle_221 geometry"]=s
s= marker_sets["particle_221 geometry"]
mark=s.place_marker((2206.29, 4114.73, 3484.49), (0.7, 0.7, 0.7), 92.0871)
if "particle_222 geometry" not in marker_sets:
  s=new_marker_set('particle_222 geometry')
  marker_sets["particle_222 geometry"]=s
s= marker_sets["particle_222 geometry"]
mark=s.place_marker((2345.09, 3641.19, 3602.16), (0.7, 0.7, 0.7), 210.273)
if "particle_223 geometry" not in marker_sets:
  s=new_marker_set('particle_223 geometry')
  marker_sets["particle_223 geometry"]=s
s= marker_sets["particle_223 geometry"]
mark=s.place_marker((2028.78, 3028.89, 3292.82), (0.7, 0.7, 0.7), 122.628)
if "particle_224 geometry" not in marker_sets:
  s=new_marker_set('particle_224 geometry')
  marker_sets["particle_224 geometry"]=s
s= marker_sets["particle_224 geometry"]
mark=s.place_marker((1838.43, 2906.97, 3195.99), (0.7, 0.7, 0.7), 109.176)
if "particle_225 geometry" not in marker_sets:
  s=new_marker_set('particle_225 geometry')
  marker_sets["particle_225 geometry"]=s
s= marker_sets["particle_225 geometry"]
mark=s.place_marker((1950.17, 3195.9, 3093.16), (0.7, 0.7, 0.7), 142.213)
if "particle_226 geometry" not in marker_sets:
  s=new_marker_set('particle_226 geometry')
  marker_sets["particle_226 geometry"]=s
s= marker_sets["particle_226 geometry"]
mark=s.place_marker((2132.41, 3312.43, 3332.04), (0.7, 0.7, 0.7), 250.078)
if "particle_227 geometry" not in marker_sets:
  s=new_marker_set('particle_227 geometry')
  marker_sets["particle_227 geometry"]=s
s= marker_sets["particle_227 geometry"]
mark=s.place_marker((2415.47, 3307.47, 2972.72), (0.7, 0.7, 0.7), 123.558)
if "particle_228 geometry" not in marker_sets:
  s=new_marker_set('particle_228 geometry')
  marker_sets["particle_228 geometry"]=s
s= marker_sets["particle_228 geometry"]
mark=s.place_marker((2446.35, 3067.63, 2565.37), (0.7, 0.7, 0.7), 235.992)
if "particle_229 geometry" not in marker_sets:
  s=new_marker_set('particle_229 geometry')
  marker_sets["particle_229 geometry"]=s
s= marker_sets["particle_229 geometry"]
mark=s.place_marker((2651.22, 2858.8, 2162.2), (0.7, 0.7, 0.7), 172.373)
if "particle_230 geometry" not in marker_sets:
  s=new_marker_set('particle_230 geometry')
  marker_sets["particle_230 geometry"]=s
s= marker_sets["particle_230 geometry"]
mark=s.place_marker((3054.35, 3033.46, 2036.24), (0.7, 0.7, 0.7), 152.322)
if "particle_231 geometry" not in marker_sets:
  s=new_marker_set('particle_231 geometry')
  marker_sets["particle_231 geometry"]=s
s= marker_sets["particle_231 geometry"]
mark=s.place_marker((3249.03, 3253.68, 2005.73), (0.7, 0.7, 0.7), 196.653)
if "particle_232 geometry" not in marker_sets:
  s=new_marker_set('particle_232 geometry')
  marker_sets["particle_232 geometry"]=s
s= marker_sets["particle_232 geometry"]
mark=s.place_marker((2922.56, 3361.6, 1861.31), (0.7, 0.7, 0.7), 134.091)
if "particle_233 geometry" not in marker_sets:
  s=new_marker_set('particle_233 geometry')
  marker_sets["particle_233 geometry"]=s
s= marker_sets["particle_233 geometry"]
mark=s.place_marker((2675.27, 3273.9, 1663.18), (0.7, 0.7, 0.7), 180.325)
if "particle_234 geometry" not in marker_sets:
  s=new_marker_set('particle_234 geometry')
  marker_sets["particle_234 geometry"]=s
s= marker_sets["particle_234 geometry"]
mark=s.place_marker((2699.14, 3063.57, 2077.47), (0.7, 0.7, 0.7), 218.437)
if "particle_235 geometry" not in marker_sets:
  s=new_marker_set('particle_235 geometry')
  marker_sets["particle_235 geometry"]=s
s= marker_sets["particle_235 geometry"]
mark=s.place_marker((2692.77, 3298.66, 2478.55), (0.7, 0.7, 0.7), 148.008)
if "particle_236 geometry" not in marker_sets:
  s=new_marker_set('particle_236 geometry')
  marker_sets["particle_236 geometry"]=s
s= marker_sets["particle_236 geometry"]
mark=s.place_marker((2815.91, 3879.98, 2710.34), (0.7, 0.7, 0.7), 191.873)
if "particle_237 geometry" not in marker_sets:
  s=new_marker_set('particle_237 geometry')
  marker_sets["particle_237 geometry"]=s
s= marker_sets["particle_237 geometry"]
mark=s.place_marker((2670.78, 4399.5, 2812.97), (0.7, 0.7, 0.7), 138.575)
if "particle_238 geometry" not in marker_sets:
  s=new_marker_set('particle_238 geometry')
  marker_sets["particle_238 geometry"]=s
s= marker_sets["particle_238 geometry"]
mark=s.place_marker((2745.21, 4738.89, 2545.22), (0.7, 0.7, 0.7), 161.205)
if "particle_239 geometry" not in marker_sets:
  s=new_marker_set('particle_239 geometry')
  marker_sets["particle_239 geometry"]=s
s= marker_sets["particle_239 geometry"]
mark=s.place_marker((2966.37, 4379.84, 2685.19), (0.7, 0.7, 0.7), 288.021)
if "particle_240 geometry" not in marker_sets:
  s=new_marker_set('particle_240 geometry')
  marker_sets["particle_240 geometry"]=s
s= marker_sets["particle_240 geometry"]
mark=s.place_marker((2908.75, 3930.32, 2154.51), (0.7, 0.7, 0.7), 227.405)
if "particle_241 geometry" not in marker_sets:
  s=new_marker_set('particle_241 geometry')
  marker_sets["particle_241 geometry"]=s
s= marker_sets["particle_241 geometry"]
mark=s.place_marker((2838.21, 3433.36, 2022.84), (0.7, 0.7, 0.7), 126.519)
if "particle_242 geometry" not in marker_sets:
  s=new_marker_set('particle_242 geometry')
  marker_sets["particle_242 geometry"]=s
s= marker_sets["particle_242 geometry"]
mark=s.place_marker((3122.69, 3490.12, 2108.69), (0.7, 0.7, 0.7), 117.975)
if "particle_243 geometry" not in marker_sets:
  s=new_marker_set('particle_243 geometry')
  marker_sets["particle_243 geometry"]=s
s= marker_sets["particle_243 geometry"]
mark=s.place_marker((2916.86, 3212.71, 2334.27), (0.7, 0.7, 0.7), 200.883)
if "particle_244 geometry" not in marker_sets:
  s=new_marker_set('particle_244 geometry')
  marker_sets["particle_244 geometry"]=s
s= marker_sets["particle_244 geometry"]
mark=s.place_marker((2657.53, 3105.96, 2181.91), (0.7, 0.7, 0.7), 158.794)
if "particle_245 geometry" not in marker_sets:
  s=new_marker_set('particle_245 geometry')
  marker_sets["particle_245 geometry"]=s
s= marker_sets["particle_245 geometry"]
mark=s.place_marker((2393.96, 3228.27, 2016.67), (0.7, 0.7, 0.7), 115.86)
if "particle_246 geometry" not in marker_sets:
  s=new_marker_set('particle_246 geometry')
  marker_sets["particle_246 geometry"]=s
s= marker_sets["particle_246 geometry"]
mark=s.place_marker((2299.28, 3009.32, 2060.57), (0.7, 0.7, 0.7), 133.034)
if "particle_247 geometry" not in marker_sets:
  s=new_marker_set('particle_247 geometry')
  marker_sets["particle_247 geometry"]=s
s= marker_sets["particle_247 geometry"]
mark=s.place_marker((2517.84, 2585.6, 2042.87), (0.7, 0.7, 0.7), 314.627)
if "particle_248 geometry" not in marker_sets:
  s=new_marker_set('particle_248 geometry')
  marker_sets["particle_248 geometry"]=s
s= marker_sets["particle_248 geometry"]
mark=s.place_marker((2753.92, 2857.61, 2117.45), (0.7, 0.7, 0.7), 115.352)
if "particle_249 geometry" not in marker_sets:
  s=new_marker_set('particle_249 geometry')
  marker_sets["particle_249 geometry"]=s
s= marker_sets["particle_249 geometry"]
mark=s.place_marker((2815.83, 3287.56, 2082.41), (0.7, 0.7, 0.7), 180.621)
if "particle_250 geometry" not in marker_sets:
  s=new_marker_set('particle_250 geometry')
  marker_sets["particle_250 geometry"]=s
s= marker_sets["particle_250 geometry"]
mark=s.place_marker((2519.44, 3465.55, 1919.13), (0.7, 0.7, 0.7), 126.265)
if "particle_251 geometry" not in marker_sets:
  s=new_marker_set('particle_251 geometry')
  marker_sets["particle_251 geometry"]=s
s= marker_sets["particle_251 geometry"]
mark=s.place_marker((2161.85, 3396.25, 2075.26), (0.7, 0.7, 0.7), 133.541)
if "particle_252 geometry" not in marker_sets:
  s=new_marker_set('particle_252 geometry')
  marker_sets["particle_252 geometry"]=s
s= marker_sets["particle_252 geometry"]
mark=s.place_marker((1771.28, 3516.92, 2235.9), (0.7, 0.7, 0.7), 171.019)
if "particle_253 geometry" not in marker_sets:
  s=new_marker_set('particle_253 geometry')
  marker_sets["particle_253 geometry"]=s
s= marker_sets["particle_253 geometry"]
mark=s.place_marker((1516.94, 3760.6, 2409.17), (0.7, 0.7, 0.7), 115.437)
if "particle_254 geometry" not in marker_sets:
  s=new_marker_set('particle_254 geometry')
  marker_sets["particle_254 geometry"]=s
s= marker_sets["particle_254 geometry"]
mark=s.place_marker((1798.42, 3697.75, 2254.62), (0.7, 0.7, 0.7), 158.583)
if "particle_255 geometry" not in marker_sets:
  s=new_marker_set('particle_255 geometry')
  marker_sets["particle_255 geometry"]=s
s= marker_sets["particle_255 geometry"]
mark=s.place_marker((1947.99, 3258.84, 2377.24), (0.7, 0.7, 0.7), 192)
if "particle_256 geometry" not in marker_sets:
  s=new_marker_set('particle_256 geometry')
  marker_sets["particle_256 geometry"]=s
s= marker_sets["particle_256 geometry"]
mark=s.place_marker((2156.83, 2886.49, 2285.85), (0.7, 0.7, 0.7), 150.165)
if "particle_257 geometry" not in marker_sets:
  s=new_marker_set('particle_257 geometry')
  marker_sets["particle_257 geometry"]=s
s= marker_sets["particle_257 geometry"]
mark=s.place_marker((1870.37, 2882.66, 2327.93), (0.7, 0.7, 0.7), 157.567)
if "particle_258 geometry" not in marker_sets:
  s=new_marker_set('particle_258 geometry')
  marker_sets["particle_258 geometry"]=s
s= marker_sets["particle_258 geometry"]
mark=s.place_marker((1938.85, 2817.33, 2402.25), (0.7, 0.7, 0.7), 199.36)
if "particle_259 geometry" not in marker_sets:
  s=new_marker_set('particle_259 geometry')
  marker_sets["particle_259 geometry"]=s
s= marker_sets["particle_259 geometry"]
mark=s.place_marker((2095.82, 3195.55, 2617.75), (0.7, 0.7, 0.7), 105.369)
if "particle_260 geometry" not in marker_sets:
  s=new_marker_set('particle_260 geometry')
  marker_sets["particle_260 geometry"]=s
s= marker_sets["particle_260 geometry"]
mark=s.place_marker((2188.58, 3349.41, 2783.01), (0.7, 0.7, 0.7), 118.651)
if "particle_261 geometry" not in marker_sets:
  s=new_marker_set('particle_261 geometry')
  marker_sets["particle_261 geometry"]=s
s= marker_sets["particle_261 geometry"]
mark=s.place_marker((2341.11, 2928.23, 2581.61), (0.7, 0.7, 0.7), 219.664)
if "particle_262 geometry" not in marker_sets:
  s=new_marker_set('particle_262 geometry')
  marker_sets["particle_262 geometry"]=s
s= marker_sets["particle_262 geometry"]
mark=s.place_marker((2218.13, 2431.66, 2265.18), (0.7, 0.7, 0.7), 196.018)
if "particle_263 geometry" not in marker_sets:
  s=new_marker_set('particle_263 geometry')
  marker_sets["particle_263 geometry"]=s
s= marker_sets["particle_263 geometry"]
mark=s.place_marker((2133.08, 1993.66, 2060.5), (0.7, 0.7, 0.7), 218.141)
if "particle_264 geometry" not in marker_sets:
  s=new_marker_set('particle_264 geometry')
  marker_sets["particle_264 geometry"]=s
s= marker_sets["particle_264 geometry"]
mark=s.place_marker((1879.55, 1910.2, 2296.51), (0.7, 0.7, 0.7), 181.636)
if "particle_265 geometry" not in marker_sets:
  s=new_marker_set('particle_265 geometry')
  marker_sets["particle_265 geometry"]=s
s= marker_sets["particle_265 geometry"]
mark=s.place_marker((1836.86, 2126.76, 2496.67), (0.7, 0.7, 0.7), 195.003)
if "particle_266 geometry" not in marker_sets:
  s=new_marker_set('particle_266 geometry')
  marker_sets["particle_266 geometry"]=s
s= marker_sets["particle_266 geometry"]
mark=s.place_marker((1813.05, 1982.77, 2284), (0.7, 0.7, 0.7), 139.209)
if "particle_267 geometry" not in marker_sets:
  s=new_marker_set('particle_267 geometry')
  marker_sets["particle_267 geometry"]=s
s= marker_sets["particle_267 geometry"]
mark=s.place_marker((1736.66, 1987.92, 2244.43), (0.7, 0.7, 0.7), 189.885)
if "particle_268 geometry" not in marker_sets:
  s=new_marker_set('particle_268 geometry')
  marker_sets["particle_268 geometry"]=s
s= marker_sets["particle_268 geometry"]
mark=s.place_marker((1776.07, 2186.49, 2056.09), (0.7, 0.7, 0.7), 267.674)
if "particle_269 geometry" not in marker_sets:
  s=new_marker_set('particle_269 geometry')
  marker_sets["particle_269 geometry"]=s
s= marker_sets["particle_269 geometry"]
mark=s.place_marker((1968.79, 2624.85, 1744.38), (0.7, 0.7, 0.7), 196.568)
if "particle_270 geometry" not in marker_sets:
  s=new_marker_set('particle_270 geometry')
  marker_sets["particle_270 geometry"]=s
s= marker_sets["particle_270 geometry"]
mark=s.place_marker((1647.69, 2673.23, 1729.54), (0.7, 0.7, 0.7), 192.423)
if "particle_271 geometry" not in marker_sets:
  s=new_marker_set('particle_271 geometry')
  marker_sets["particle_271 geometry"]=s
s= marker_sets["particle_271 geometry"]
mark=s.place_marker((1448.79, 2359.73, 1787.52), (1, 0.7, 0), 202.405)
if "particle_272 geometry" not in marker_sets:
  s=new_marker_set('particle_272 geometry')
  marker_sets["particle_272 geometry"]=s
s= marker_sets["particle_272 geometry"]
mark=s.place_marker((1800.19, 3076.7, 1535.87), (0.7, 0.7, 0.7), 135.529)
if "particle_273 geometry" not in marker_sets:
  s=new_marker_set('particle_273 geometry')
  marker_sets["particle_273 geometry"]=s
s= marker_sets["particle_273 geometry"]
mark=s.place_marker((2016.71, 3965.5, 1292.17), (0.7, 0.7, 0.7), 114.21)
if "particle_274 geometry" not in marker_sets:
  s=new_marker_set('particle_274 geometry')
  marker_sets["particle_274 geometry"]=s
s= marker_sets["particle_274 geometry"]
mark=s.place_marker((2120.74, 4036.97, 1592.92), (0.7, 0.7, 0.7), 159.133)
if "particle_275 geometry" not in marker_sets:
  s=new_marker_set('particle_275 geometry')
  marker_sets["particle_275 geometry"]=s
s= marker_sets["particle_275 geometry"]
mark=s.place_marker((2337.07, 3775.48, 1830.23), (0.7, 0.7, 0.7), 144.412)
if "particle_276 geometry" not in marker_sets:
  s=new_marker_set('particle_276 geometry')
  marker_sets["particle_276 geometry"]=s
s= marker_sets["particle_276 geometry"]
mark=s.place_marker((2553.24, 3544.68, 1934.05), (0.7, 0.7, 0.7), 70.8525)
if "particle_277 geometry" not in marker_sets:
  s=new_marker_set('particle_277 geometry')
  marker_sets["particle_277 geometry"]=s
s= marker_sets["particle_277 geometry"]
mark=s.place_marker((2314.04, 2991.3, 2149.49), (0.7, 0.7, 0.7), 141.874)
if "particle_278 geometry" not in marker_sets:
  s=new_marker_set('particle_278 geometry')
  marker_sets["particle_278 geometry"]=s
s= marker_sets["particle_278 geometry"]
mark=s.place_marker((2018.11, 2453.33, 2225.04), (0.7, 0.7, 0.7), 217.337)
if "particle_279 geometry" not in marker_sets:
  s=new_marker_set('particle_279 geometry')
  marker_sets["particle_279 geometry"]=s
s= marker_sets["particle_279 geometry"]
mark=s.place_marker((2049.82, 2398.92, 2181.74), (0.7, 0.7, 0.7), 237.641)
if "particle_280 geometry" not in marker_sets:
  s=new_marker_set('particle_280 geometry')
  marker_sets["particle_280 geometry"]=s
s= marker_sets["particle_280 geometry"]
mark=s.place_marker((2476.41, 2578.19, 2110.37), (0.7, 0.7, 0.7), 229.393)
if "particle_281 geometry" not in marker_sets:
  s=new_marker_set('particle_281 geometry')
  marker_sets["particle_281 geometry"]=s
s= marker_sets["particle_281 geometry"]
mark=s.place_marker((2556.09, 2041.77, 1851.74), (0.7, 0.7, 0.7), 349.906)
if "particle_282 geometry" not in marker_sets:
  s=new_marker_set('particle_282 geometry')
  marker_sets["particle_282 geometry"]=s
s= marker_sets["particle_282 geometry"]
mark=s.place_marker((2321.72, 1686.81, 1473.19), (0.7, 0.7, 0.7), 162.347)
if "particle_283 geometry" not in marker_sets:
  s=new_marker_set('particle_283 geometry')
  marker_sets["particle_283 geometry"]=s
s= marker_sets["particle_283 geometry"]
mark=s.place_marker((2324.73, 1603.93, 1326.63), (0.7, 0.7, 0.7), 194.072)
if "particle_284 geometry" not in marker_sets:
  s=new_marker_set('particle_284 geometry')
  marker_sets["particle_284 geometry"]=s
s= marker_sets["particle_284 geometry"]
mark=s.place_marker((2497.36, 1610.21, 1266.8), (0.7, 0.7, 0.7), 242.21)
if "particle_285 geometry" not in marker_sets:
  s=new_marker_set('particle_285 geometry')
  marker_sets["particle_285 geometry"]=s
s= marker_sets["particle_285 geometry"]
mark=s.place_marker((2742.18, 1934.92, 948.777), (0.7, 0.7, 0.7), 320.93)
if "particle_286 geometry" not in marker_sets:
  s=new_marker_set('particle_286 geometry')
  marker_sets["particle_286 geometry"]=s
s= marker_sets["particle_286 geometry"]
mark=s.place_marker((3006.4, 1920.64, 443.736), (0.7, 0.7, 0.7), 226.432)
if "particle_287 geometry" not in marker_sets:
  s=new_marker_set('particle_287 geometry')
  marker_sets["particle_287 geometry"]=s
s= marker_sets["particle_287 geometry"]
mark=s.place_marker((3086.12, 1715.24, 720.379), (0.7, 0.7, 0.7), 125.208)
if "particle_288 geometry" not in marker_sets:
  s=new_marker_set('particle_288 geometry')
  marker_sets["particle_288 geometry"]=s
s= marker_sets["particle_288 geometry"]
mark=s.place_marker((3116, 1355.67, 1226.49), (0.7, 0.7, 0.7), 197.837)
if "particle_289 geometry" not in marker_sets:
  s=new_marker_set('particle_289 geometry')
  marker_sets["particle_289 geometry"]=s
s= marker_sets["particle_289 geometry"]
mark=s.place_marker((3644.74, 989.654, 1304.88), (0.7, 0.7, 0.7), 167.804)
if "particle_290 geometry" not in marker_sets:
  s=new_marker_set('particle_290 geometry')
  marker_sets["particle_290 geometry"]=s
s= marker_sets["particle_290 geometry"]
mark=s.place_marker((4395.13, 674.536, 1138.77), (0.7, 0.7, 0.7), 136.84)
if "particle_291 geometry" not in marker_sets:
  s=new_marker_set('particle_291 geometry')
  marker_sets["particle_291 geometry"]=s
s= marker_sets["particle_291 geometry"]
mark=s.place_marker((4515.71, 990.712, 872.555), (0.7, 0.7, 0.7), 85.7421)
if "particle_292 geometry" not in marker_sets:
  s=new_marker_set('particle_292 geometry')
  marker_sets["particle_292 geometry"]=s
s= marker_sets["particle_292 geometry"]
mark=s.place_marker((3164.38, 1396.95, 784.68), (1, 0.7, 0), 256)
if "particle_293 geometry" not in marker_sets:
  s=new_marker_set('particle_293 geometry')
  marker_sets["particle_293 geometry"]=s
s= marker_sets["particle_293 geometry"]
mark=s.place_marker((3885.47, 773.584, 1382.48), (0.7, 0.7, 0.7), 138.702)
if "particle_294 geometry" not in marker_sets:
  s=new_marker_set('particle_294 geometry')
  marker_sets["particle_294 geometry"]=s
s= marker_sets["particle_294 geometry"]
mark=s.place_marker((4039.49, 387.377, 1609.46), (0.7, 0.7, 0.7), 140.732)
if "particle_295 geometry" not in marker_sets:
  s=new_marker_set('particle_295 geometry')
  marker_sets["particle_295 geometry"]=s
s= marker_sets["particle_295 geometry"]
mark=s.place_marker((3901.08, 417.91, 1320.14), (0.7, 0.7, 0.7), 81.3006)
if "particle_296 geometry" not in marker_sets:
  s=new_marker_set('particle_296 geometry')
  marker_sets["particle_296 geometry"]=s
s= marker_sets["particle_296 geometry"]
mark=s.place_marker((4058.75, 349.429, 901.764), (0.7, 0.7, 0.7), 133.837)
if "particle_297 geometry" not in marker_sets:
  s=new_marker_set('particle_297 geometry')
  marker_sets["particle_297 geometry"]=s
s= marker_sets["particle_297 geometry"]
mark=s.place_marker((3598.73, 755.606, 871.413), (0.7, 0.7, 0.7), 98.3475)
if "particle_298 geometry" not in marker_sets:
  s=new_marker_set('particle_298 geometry')
  marker_sets["particle_298 geometry"]=s
s= marker_sets["particle_298 geometry"]
mark=s.place_marker((2907.65, 1126.95, 1148.82), (0.7, 0.7, 0.7), 297.623)
if "particle_299 geometry" not in marker_sets:
  s=new_marker_set('particle_299 geometry')
  marker_sets["particle_299 geometry"]=s
s= marker_sets["particle_299 geometry"]
mark=s.place_marker((2630.84, 1450.06, 1103.52), (0.7, 0.7, 0.7), 212.938)
if "particle_300 geometry" not in marker_sets:
  s=new_marker_set('particle_300 geometry')
  marker_sets["particle_300 geometry"]=s
s= marker_sets["particle_300 geometry"]
mark=s.place_marker((2499.83, 1303.69, 987.371), (0.7, 0.7, 0.7), 154.183)
if "particle_301 geometry" not in marker_sets:
  s=new_marker_set('particle_301 geometry')
  marker_sets["particle_301 geometry"]=s
s= marker_sets["particle_301 geometry"]
mark=s.place_marker((2511.25, 1490.07, 607.832), (0.7, 0.7, 0.7), 180.832)
if "particle_302 geometry" not in marker_sets:
  s=new_marker_set('particle_302 geometry')
  marker_sets["particle_302 geometry"]=s
s= marker_sets["particle_302 geometry"]
mark=s.place_marker((2669.55, 1779.76, 425.357), (0.7, 0.7, 0.7), 122.332)
if "particle_303 geometry" not in marker_sets:
  s=new_marker_set('particle_303 geometry')
  marker_sets["particle_303 geometry"]=s
s= marker_sets["particle_303 geometry"]
mark=s.place_marker((2907.25, 2066.07, 374.24), (0.7, 0.7, 0.7), 209.047)
if "particle_304 geometry" not in marker_sets:
  s=new_marker_set('particle_304 geometry')
  marker_sets["particle_304 geometry"]=s
s= marker_sets["particle_304 geometry"]
mark=s.place_marker((2650.43, 2052.31, 56.0027), (0.7, 0.7, 0.7), 126.985)
if "particle_305 geometry" not in marker_sets:
  s=new_marker_set('particle_305 geometry')
  marker_sets["particle_305 geometry"]=s
s= marker_sets["particle_305 geometry"]
mark=s.place_marker((2699.27, 1971.34, -346.704), (0.7, 0.7, 0.7), 122.205)
if "particle_306 geometry" not in marker_sets:
  s=new_marker_set('particle_306 geometry')
  marker_sets["particle_306 geometry"]=s
s= marker_sets["particle_306 geometry"]
mark=s.place_marker((2781.69, 1743.29, -451.043), (0.7, 0.7, 0.7), 107.95)
if "particle_307 geometry" not in marker_sets:
  s=new_marker_set('particle_307 geometry')
  marker_sets["particle_307 geometry"]=s
s= marker_sets["particle_307 geometry"]
mark=s.place_marker((2543.6, 1695.55, 104.69), (0.7, 0.7, 0.7), 182.567)
if "particle_308 geometry" not in marker_sets:
  s=new_marker_set('particle_308 geometry')
  marker_sets["particle_308 geometry"]=s
s= marker_sets["particle_308 geometry"]
mark=s.place_marker((2487.85, 1639.74, 736.467), (0.7, 0.7, 0.7), 185.274)
if "particle_309 geometry" not in marker_sets:
  s=new_marker_set('particle_309 geometry')
  marker_sets["particle_309 geometry"]=s
s= marker_sets["particle_309 geometry"]
mark=s.place_marker((2652.8, 1782.2, 1137.09), (0.7, 0.7, 0.7), 413.567)
if "particle_310 geometry" not in marker_sets:
  s=new_marker_set('particle_310 geometry')
  marker_sets["particle_310 geometry"]=s
s= marker_sets["particle_310 geometry"]
mark=s.place_marker((2495.68, 1687.76, 1297.22), (0.7, 0.7, 0.7), 240.01)
if "particle_311 geometry" not in marker_sets:
  s=new_marker_set('particle_311 geometry')
  marker_sets["particle_311 geometry"]=s
s= marker_sets["particle_311 geometry"]
mark=s.place_marker((2519.2, 1726.26, 1272.51), (0.7, 0.7, 0.7), 238.995)
if "particle_312 geometry" not in marker_sets:
  s=new_marker_set('particle_312 geometry')
  marker_sets["particle_312 geometry"]=s
s= marker_sets["particle_312 geometry"]
mark=s.place_marker((2405.35, 1598.14, 1054.6), (0.7, 0.7, 0.7), 203.674)
if "particle_313 geometry" not in marker_sets:
  s=new_marker_set('particle_313 geometry')
  marker_sets["particle_313 geometry"]=s
s= marker_sets["particle_313 geometry"]
mark=s.place_marker((2029.68, 1723.26, 596.537), (0.7, 0.7, 0.7), 266.744)
if "particle_314 geometry" not in marker_sets:
  s=new_marker_set('particle_314 geometry')
  marker_sets["particle_314 geometry"]=s
s= marker_sets["particle_314 geometry"]
mark=s.place_marker((1994.6, 1268.29, 575.048), (0.7, 0.7, 0.7), 147.585)
if "particle_315 geometry" not in marker_sets:
  s=new_marker_set('particle_315 geometry')
  marker_sets["particle_315 geometry"]=s
s= marker_sets["particle_315 geometry"]
mark=s.place_marker((2108.98, 1388.65, 815.795), (0.7, 0.7, 0.7), 249.485)
if "particle_316 geometry" not in marker_sets:
  s=new_marker_set('particle_316 geometry')
  marker_sets["particle_316 geometry"]=s
s= marker_sets["particle_316 geometry"]
mark=s.place_marker((2204.52, 1786.42, 928.205), (0.7, 0.7, 0.7), 119.371)
if "particle_317 geometry" not in marker_sets:
  s=new_marker_set('particle_317 geometry')
  marker_sets["particle_317 geometry"]=s
s= marker_sets["particle_317 geometry"]
mark=s.place_marker((2640.42, 2317.98, 739.01), (0.7, 0.7, 0.7), 155.875)
if "particle_318 geometry" not in marker_sets:
  s=new_marker_set('particle_318 geometry')
  marker_sets["particle_318 geometry"]=s
s= marker_sets["particle_318 geometry"]
mark=s.place_marker((3375.21, 2485.35, 648.193), (0.7, 0.7, 0.7), 189.419)
if "particle_319 geometry" not in marker_sets:
  s=new_marker_set('particle_319 geometry')
  marker_sets["particle_319 geometry"]=s
s= marker_sets["particle_319 geometry"]
mark=s.place_marker((3706.11, 2275.12, 1026.69), (0.7, 0.7, 0.7), 137.475)
if "particle_320 geometry" not in marker_sets:
  s=new_marker_set('particle_320 geometry')
  marker_sets["particle_320 geometry"]=s
s= marker_sets["particle_320 geometry"]
mark=s.place_marker((3754.68, 2058.89, 1478.97), (0.7, 0.7, 0.7), 176.179)
if "particle_321 geometry" not in marker_sets:
  s=new_marker_set('particle_321 geometry')
  marker_sets["particle_321 geometry"]=s
s= marker_sets["particle_321 geometry"]
mark=s.place_marker((3930.56, 1804.12, 1829.11), (0.7, 0.7, 0.7), 138.829)
if "particle_322 geometry" not in marker_sets:
  s=new_marker_set('particle_322 geometry')
  marker_sets["particle_322 geometry"]=s
s= marker_sets["particle_322 geometry"]
mark=s.place_marker((4164.41, 1510.15, 2019.42), (0.7, 0.7, 0.7), 148.727)
if "particle_323 geometry" not in marker_sets:
  s=new_marker_set('particle_323 geometry')
  marker_sets["particle_323 geometry"]=s
s= marker_sets["particle_323 geometry"]
mark=s.place_marker((4575.51, 1187.54, 2072.87), (0.7, 0.7, 0.7), 230.323)
if "particle_324 geometry" not in marker_sets:
  s=new_marker_set('particle_324 geometry')
  marker_sets["particle_324 geometry"]=s
s= marker_sets["particle_324 geometry"]
mark=s.place_marker((4202.23, 1486.7, 1655.54), (0.7, 0.7, 0.7), 175.376)
if "particle_325 geometry" not in marker_sets:
  s=new_marker_set('particle_325 geometry')
  marker_sets["particle_325 geometry"]=s
s= marker_sets["particle_325 geometry"]
mark=s.place_marker((3801.47, 1742.54, 1488.39), (0.7, 0.7, 0.7), 161.163)
if "particle_326 geometry" not in marker_sets:
  s=new_marker_set('particle_326 geometry')
  marker_sets["particle_326 geometry"]=s
s= marker_sets["particle_326 geometry"]
mark=s.place_marker((4031.8, 2144.2, 1621.99), (0.7, 0.7, 0.7), 125.885)
if "particle_327 geometry" not in marker_sets:
  s=new_marker_set('particle_327 geometry')
  marker_sets["particle_327 geometry"]=s
s= marker_sets["particle_327 geometry"]
mark=s.place_marker((4309.39, 2506.29, 1573.82), (0.7, 0.7, 0.7), 206.635)
if "particle_328 geometry" not in marker_sets:
  s=new_marker_set('particle_328 geometry')
  marker_sets["particle_328 geometry"]=s
s= marker_sets["particle_328 geometry"]
mark=s.place_marker((4024.58, 2413, 1913.96), (0.7, 0.7, 0.7), 151.392)
if "particle_329 geometry" not in marker_sets:
  s=new_marker_set('particle_329 geometry')
  marker_sets["particle_329 geometry"]=s
s= marker_sets["particle_329 geometry"]
mark=s.place_marker((3854.72, 2232.7, 2174.85), (0.7, 0.7, 0.7), 173.388)
if "particle_330 geometry" not in marker_sets:
  s=new_marker_set('particle_330 geometry')
  marker_sets["particle_330 geometry"]=s
s= marker_sets["particle_330 geometry"]
mark=s.place_marker((4065.63, 1980.99, 2198.88), (0.7, 0.7, 0.7), 135.825)
if "particle_331 geometry" not in marker_sets:
  s=new_marker_set('particle_331 geometry')
  marker_sets["particle_331 geometry"]=s
s= marker_sets["particle_331 geometry"]
mark=s.place_marker((4411.02, 1732.55, 2124.73), (0.7, 0.7, 0.7), 186.839)
if "particle_332 geometry" not in marker_sets:
  s=new_marker_set('particle_332 geometry')
  marker_sets["particle_332 geometry"]=s
s= marker_sets["particle_332 geometry"]
mark=s.place_marker((4794.92, 1478.83, 2012.02), (0.7, 0.7, 0.7), 121.189)
if "particle_333 geometry" not in marker_sets:
  s=new_marker_set('particle_333 geometry')
  marker_sets["particle_333 geometry"]=s
s= marker_sets["particle_333 geometry"]
mark=s.place_marker((4468.47, 1689.05, 1833.67), (0.7, 0.7, 0.7), 102.916)
if "particle_334 geometry" not in marker_sets:
  s=new_marker_set('particle_334 geometry')
  marker_sets["particle_334 geometry"]=s
s= marker_sets["particle_334 geometry"]
mark=s.place_marker((3930.46, 1864.79, 1565.28), (0.7, 0.7, 0.7), 212.769)
if "particle_335 geometry" not in marker_sets:
  s=new_marker_set('particle_335 geometry')
  marker_sets["particle_335 geometry"]=s
s= marker_sets["particle_335 geometry"]
mark=s.place_marker((3296.36, 2083.02, 1529.78), (0.7, 0.7, 0.7), 173.092)
if "particle_336 geometry" not in marker_sets:
  s=new_marker_set('particle_336 geometry')
  marker_sets["particle_336 geometry"]=s
s= marker_sets["particle_336 geometry"]
mark=s.place_marker((2915.91, 2281.92, 1264.99), (0.7, 0.7, 0.7), 264.502)
if "particle_337 geometry" not in marker_sets:
  s=new_marker_set('particle_337 geometry')
  marker_sets["particle_337 geometry"]=s
s= marker_sets["particle_337 geometry"]
mark=s.place_marker((2841.56, 2468.86, 746.689), (0.7, 0.7, 0.7), 208.666)
if "particle_338 geometry" not in marker_sets:
  s=new_marker_set('particle_338 geometry')
  marker_sets["particle_338 geometry"]=s
s= marker_sets["particle_338 geometry"]
mark=s.place_marker((2804.13, 2380.2, 266.308), (0.7, 0.7, 0.7), 186.797)
if "particle_339 geometry" not in marker_sets:
  s=new_marker_set('particle_339 geometry')
  marker_sets["particle_339 geometry"]=s
s= marker_sets["particle_339 geometry"]
mark=s.place_marker((2384.59, 2129.58, 155.659), (0.7, 0.7, 0.7), 255.534)
if "particle_340 geometry" not in marker_sets:
  s=new_marker_set('particle_340 geometry')
  marker_sets["particle_340 geometry"]=s
s= marker_sets["particle_340 geometry"]
mark=s.place_marker((2408.74, 1740.8, -9.51556), (0.7, 0.7, 0.7), 153.126)
if "particle_341 geometry" not in marker_sets:
  s=new_marker_set('particle_341 geometry')
  marker_sets["particle_341 geometry"]=s
s= marker_sets["particle_341 geometry"]
mark=s.place_marker((2536.39, 1990.47, -296.525), (0.7, 0.7, 0.7), 165.816)
if "particle_342 geometry" not in marker_sets:
  s=new_marker_set('particle_342 geometry')
  marker_sets["particle_342 geometry"]=s
s= marker_sets["particle_342 geometry"]
mark=s.place_marker((2349.54, 2257.81, -74.0649), (0.7, 0.7, 0.7), 134.429)
if "particle_343 geometry" not in marker_sets:
  s=new_marker_set('particle_343 geometry')
  marker_sets["particle_343 geometry"]=s
s= marker_sets["particle_343 geometry"]
mark=s.place_marker((2507.32, 2422.51, 254.519), (0.7, 0.7, 0.7), 178.971)
if "particle_344 geometry" not in marker_sets:
  s=new_marker_set('particle_344 geometry')
  marker_sets["particle_344 geometry"]=s
s= marker_sets["particle_344 geometry"]
mark=s.place_marker((3006.51, 2415.34, 428.029), (0.7, 0.7, 0.7), 189.969)
if "particle_345 geometry" not in marker_sets:
  s=new_marker_set('particle_345 geometry')
  marker_sets["particle_345 geometry"]=s
s= marker_sets["particle_345 geometry"]
mark=s.place_marker((3562.04, 2614.29, 196.017), (0.7, 0.7, 0.7), 121.359)
if "particle_346 geometry" not in marker_sets:
  s=new_marker_set('particle_346 geometry')
  marker_sets["particle_346 geometry"]=s
s= marker_sets["particle_346 geometry"]
mark=s.place_marker((3997.68, 2543.8, 523.648), (0.7, 0.7, 0.7), 187.262)
if "particle_347 geometry" not in marker_sets:
  s=new_marker_set('particle_347 geometry')
  marker_sets["particle_347 geometry"]=s
s= marker_sets["particle_347 geometry"]
mark=s.place_marker((4075.76, 2399.8, 1161.56), (0.7, 0.7, 0.7), 164.335)
if "particle_348 geometry" not in marker_sets:
  s=new_marker_set('particle_348 geometry')
  marker_sets["particle_348 geometry"]=s
s= marker_sets["particle_348 geometry"]
mark=s.place_marker((4118.73, 1948.77, 1396.98), (0.7, 0.7, 0.7), 138.363)
if "particle_349 geometry" not in marker_sets:
  s=new_marker_set('particle_349 geometry')
  marker_sets["particle_349 geometry"]=s
s= marker_sets["particle_349 geometry"]
mark=s.place_marker((4314.61, 1697.52, 1589.38), (0.7, 0.7, 0.7), 138.49)
if "particle_350 geometry" not in marker_sets:
  s=new_marker_set('particle_350 geometry')
  marker_sets["particle_350 geometry"]=s
s= marker_sets["particle_350 geometry"]
mark=s.place_marker((4339.19, 1954.95, 1829.74), (0.7, 0.7, 0.7), 116.325)
if "particle_351 geometry" not in marker_sets:
  s=new_marker_set('particle_351 geometry')
  marker_sets["particle_351 geometry"]=s
s= marker_sets["particle_351 geometry"]
mark=s.place_marker((4065.15, 2284.36, 1632.73), (0.7, 0.7, 0.7), 106.511)
if "particle_352 geometry" not in marker_sets:
  s=new_marker_set('particle_352 geometry')
  marker_sets["particle_352 geometry"]=s
s= marker_sets["particle_352 geometry"]
mark=s.place_marker((3681.44, 2394.42, 1245.08), (0.7, 0.7, 0.7), 151.096)
if "particle_353 geometry" not in marker_sets:
  s=new_marker_set('particle_353 geometry')
  marker_sets["particle_353 geometry"]=s
s= marker_sets["particle_353 geometry"]
mark=s.place_marker((3374.53, 2445.54, 640.403), (0.7, 0.7, 0.7), 240.856)
if "particle_354 geometry" not in marker_sets:
  s=new_marker_set('particle_354 geometry')
  marker_sets["particle_354 geometry"]=s
s= marker_sets["particle_354 geometry"]
mark=s.place_marker((3166.38, 2387.77, 160.982), (0.7, 0.7, 0.7), 149.7)
if "particle_355 geometry" not in marker_sets:
  s=new_marker_set('particle_355 geometry')
  marker_sets["particle_355 geometry"]=s
s= marker_sets["particle_355 geometry"]
mark=s.place_marker((2839.25, 2406.33, 29.2283), (0.7, 0.7, 0.7), 165.943)
if "particle_356 geometry" not in marker_sets:
  s=new_marker_set('particle_356 geometry')
  marker_sets["particle_356 geometry"]=s
s= marker_sets["particle_356 geometry"]
mark=s.place_marker((2435.32, 2194.07, 445.167), (0.7, 0.7, 0.7), 178.971)
if "particle_357 geometry" not in marker_sets:
  s=new_marker_set('particle_357 geometry')
  marker_sets["particle_357 geometry"]=s
s= marker_sets["particle_357 geometry"]
mark=s.place_marker((1788.09, 2101.5, 831.05), (0.7, 0.7, 0.7), 154.945)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
