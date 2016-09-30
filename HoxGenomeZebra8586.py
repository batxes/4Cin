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
mark=s.place_marker((771.311, 5491.35, 1323.34), (0, 0, 1), 162.734)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((711.165, 5442.81, 918.953), (0.00917431, 0.00917431, 1), 247.128)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((385.209, 5224.07, 565.547), (0.0183486, 0.0183486, 1), 275.526)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((-14.5221, 5175.53, 350.258), (0.0275229, 0.0275229, 1), 174.384)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((-249.364, 5188.47, 267.667), (0.0366972, 0.0366972, 1), 66.1914)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((-473.812, 5139.05, 233.007), (0.0458716, 0.0458716, 1), 156.074)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((-750.033, 5067.82, 220.726), (0.0550459, 0.0550459, 1), 117.392)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((-1008.91, 4993.81, 229.101), (0.0642202, 0.0642202, 1), 137.503)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((-1246, 4766.04, 326.341), (0.0733945, 0.0733945, 1), 179.418)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((-1368.14, 4371.11, 450.825), (0.0825688, 0.0825688, 1), 155.575)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((-1492.1, 3946.06, 529.731), (0.0917431, 0.0917431, 1), 192.066)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((-1672.44, 4243.35, 417.421), (0.100917, 0.100917, 1), 110.428)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((-1849.96, 4014.95, 417.768), (0.110092, 0.110092, 1), 168.83)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((-1825.79, 3491.81, 567.501), (0.119266, 0.119266, 1), 242.246)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((-1978.28, 3267.92, 904.536), (0.12844, 0.12844, 1), 131.211)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((-2082.15, 3246.75, 1253.16), (0.137615, 0.137615, 1), 197.056)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((-1914.24, 3670.54, 1232.25), (0.146789, 0.146789, 1), 146.615)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((-1771.52, 4111.03, 1097.76), (0.155963, 0.155963, 1), 238.58)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((-1597.37, 4579.28, 935.38), (0.165138, 0.165138, 1), 130.777)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((-1320.58, 4441.11, 803.256), (0.174312, 0.174312, 1), 95.7617)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((-974.511, 4150.28, 641.889), (0.183486, 0.183486, 1), 242.116)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((-536.882, 3964.03, 496.051), (0.192661, 0.192661, 1), 142.254)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((-66.2791, 4020.18, 354.854), (0.201835, 0.201835, 1), 250.794)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((419.942, 4022.62, 356.407), (0.211009, 0.211009, 1), 148.025)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((798.599, 4054.54, 463.766), (0.220183, 0.220183, 1), 154.881)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((1121.2, 4388.77, 548.402), (0.229358, 0.229358, 1), 103.333)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((1302.4, 4621.67, 730.259), (0.238532, 0.238532, 1), 115.765)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((1307.76, 4912.95, 961.381), (0.247706, 0.247706, 1), 213.999)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((1019.17, 4985.57, 724.993), (0.256881, 0.256881, 1), 137.915)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((755.343, 4732.97, 399.129), (0.266055, 0.266055, 1), 253.333)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((462.056, 4274.99, 26.279), (0.275229, 0.275229, 1), 232.093)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((198.659, 3883.29, -297.985), (0.284404, 0.284404, 1), 165.771)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((-47.763, 3969.84, -775.126), (0.293578, 0.293578, 1), 230.488)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((-229.574, 3926.15, -1306.54), (0.302752, 0.302752, 1), 260.926)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((-255.633, 3305.53, -1200.99), (0.311927, 0.311927, 1), 177.66)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((-125.517, 3105.25, -1386.55), (0.321101, 0.321101, 1), 94.6119)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((151.315, 2858.35, -1363.78), (0.330275, 0.330275, 1), 269.365)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((-85.3121, 2369.82, -1189.91), (0.33945, 0.33945, 1), 221.506)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((-474.773, 2314.44, -1526.53), (0.348624, 0.348624, 1), 264.853)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((-899.995, 2517.85, -1632.76), (0.357798, 0.357798, 1), 164.557)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((-1075.69, 2815.81, -1483.25), (0.366972, 0.366972, 1), 167.616)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((-1328.43, 2838.42, -1354.64), (0.376147, 0.376147, 1), 90.1861)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((-1293.41, 2770.48, -1140.27), (0.385321, 0.385321, 1), 118.607)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((-1478.93, 2891.92, -1284.84), (0.394495, 0.394495, 1), 145.443)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((-1565.7, 2591.71, -1130.77), (0.40367, 0.40367, 1), 142.796)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((-1536.85, 2278.39, -937.561), (0.412844, 0.412844, 1), 81.0525)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((-1526.9, 2022.09, -748.749), (0.422018, 0.422018, 1), 149.283)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((-1747.47, 2269.84, -816.435), (0.431193, 0.431193, 1), 175.274)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((-1994.32, 2510.85, -652.828), (0.440367, 0.440367, 1), 252.682)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((-1942.72, 2835.74, -952.815), (0.449541, 0.449541, 1), 126.742)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((-2249.05, 2848.43, -762.598), (0.458716, 0.458716, 1), 227.797)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((-2051.48, 2651.73, -1141.9), (0.46789, 0.46789, 1), 199.833)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((-1621.11, 2400.16, -1335.21), (0.477064, 0.477064, 1), 187.25)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((-1309.79, 2131.36, -1430.58), (0.486239, 0.486239, 1), 134.162)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((-1038.46, 2021.61, -1688.11), (0.495413, 0.495413, 1), 180.242)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((-1122.24, 1685.76, -1928.26), (0.504587, 0.504587, 1), 203.759)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((-1347.62, 1362.26, -1821.73), (0.513761, 0.513761, 1), 116.893)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((-1360.34, 963.106, -1495.23), (0.522936, 0.522936, 1), 179.287)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((-1436.05, 561.693, -1071.54), (0.53211, 0.53211, 1), 228.188)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((-1885.71, 321.792, -1193.91), (0.541284, 0.541284, 1), 260.405)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((-2117.72, 459.822, -1668.07), (0.550459, 0.550459, 1), 195.212)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((-2323, 632.359, -2175.24), (0.559633, 0.559633, 1), 217.948)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((-2278.14, 377.642, -1818.84), (0.568807, 0.568807, 1), 154.425)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((-2245.54, 167.496, -1383.06), (0.577982, 0.577982, 1), 207.014)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((-2420.84, 85.4708, -852.019), (0.587156, 0.587156, 1), 314.035)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((-2588.04, 350.082, -1359.71), (0.59633, 0.59633, 1), 229.316)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((-2759.09, 538.481, -1829.28), (0.605505, 0.605505, 1), 226.626)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((-3146.8, 555.396, -1913.03), (0.614679, 0.614679, 1), 132.339)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((-3343.36, 453.379, -1626.17), (0.623853, 0.623853, 1), 123.358)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((-3413.05, 286.501, -1265.33), (0.633028, 0.633028, 1), 98.6038)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((-3613.25, 127.34, -939.3), (0.642202, 0.642202, 1), 161.649)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((-3466.89, -63.1311, -491.19), (0.651376, 0.651376, 1), 162.322)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((-3174.63, -135.325, -261.234), (0.66055, 0.66055, 1), 101.077)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((-2809.92, -186.219, -62.3921), (0.669725, 0.669725, 1), 217.471)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((-2454.7, -86.8643, 84.542), (0.678899, 0.678899, 1), 125.18)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((-2100.47, 110.013, -45.4151), (0.688073, 0.688073, 1), 232.505)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((-1612.06, -313.121, 270.296), (0.697248, 0.697248, 1), 365.539)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((-1273.28, -758.778, -121.739), (1, 0.8, 0), 215.583)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((-1764.97, -333.432, -168.443), (0.715596, 0.715596, 1), 189.896)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((-2129.22, -19.493, -283.555), (0.724771, 0.724771, 1), 138.891)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((-2262.46, -218.591, -64.2684), (0.733945, 0.733945, 1), 162.279)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((-1888.87, -560.794, 182.44), (0.743119, 0.743119, 1), 228.47)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((-1445.67, -763.959, 219.991), (0.752294, 0.752294, 1), 163.081)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((-1971.94, -942.405, 266.499), (1, 0.8, 0), 314.404)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((-1855.84, -528.492, 760.347), (0.770642, 0.770642, 1), 226.561)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((-1881.69, -44.0696, 716.954), (0.779817, 0.779817, 1), 170.978)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((-2036.11, 360.539, 538.992), (0.788991, 0.788991, 1), 191.176)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((-2455.15, 611.92, 449.61), (0.798165, 0.798165, 1), 162.43)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((-2915.59, 759.812, 474.259), (0.807339, 0.807339, 1), 191.48)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((-3224.95, 1106.53, 406.833), (0.816514, 0.816514, 1), 114.419)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((-2822.52, 1009.72, 588.436), (0.825688, 0.825688, 1), 129.953)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((-2284.46, 861.789, 757.227), (0.834862, 0.834862, 1), 246.694)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((-1665, 1000.06, 818.624), (0.844037, 0.844037, 1), 235.955)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((-1205.84, 924.256, 891.561), (0.853211, 0.853211, 1), 102.856)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((-857.321, 633.313, 939.204), (0.862385, 0.862385, 1), 205.755)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((-420.344, 644.727, 990.305), (0.87156, 0.87156, 1), 146.289)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((-466.274, 588.597, 1355.31), (0.880734, 0.880734, 1), 223.155)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((-813.031, 452.009, 1534.71), (0.889908, 0.889908, 1), 162.626)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((-1175.74, 489.082, 1677.38), (0.899083, 0.899083, 1), 207.881)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((-1419.63, 217.26, 1791.8), (0.908257, 0.908257, 1), 259.841)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((-1531.29, 471.277, 1483.88), (0.917431, 0.917431, 1), 169.481)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((-1809.75, 444.179, 1697.43), (0.926606, 0.926606, 1), 170.284)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((-2002.5, 847.085, 1758.38), (0.93578, 0.93578, 1), 147.504)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((-2149.64, 1316.32, 1803.89), (0.944954, 0.944954, 1), 162.365)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((-1677.96, 1026.75, 1799.48), (0.954128, 0.954128, 1), 263.247)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((-1203.85, 740.025, 1734.41), (0.963303, 0.963303, 1), 141.083)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((-885.574, 540.834, 1752.47), (0.972477, 0.972477, 1), 191.046)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((-774.605, 324.336, 2052.78), (0.981651, 0.981651, 1), 197.858)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((-919.878, -226.306, 2054.56), (0.990826, 0.990826, 1), 179.092)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((-1151.52, -806.098, 2102.69), (1, 1, 1), 193.997)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((-1501.53, -1300.51, 2470.84), (1, 0.3, 0), 150.281)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((-1803.88, -1425.53, 2583.85), (1, 0.3, 0), 201.265)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((-1385.99, -1582.06, 1944.71), (1, 0.972477, 0.972477), 120.668)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((-1044.57, -1680.42, 1581.24), (1, 0.963303, 0.963303), 279.323)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((-1184.38, -1987.45, 1976.87), (1, 0.3, 0), 255.61)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((-460.791, -2385.54, 1631.91), (1, 0.3, 0), 168.874)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((-147.635, -2209.04, 1343.8), (1, 0.93578, 0.93578), 153.579)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((-75.5409, -2162.14, 862.319), (1, 0.8, 0), 152.169)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((310.749, -1986.52, 674.468), (1, 0.917431, 0.917431), 222.309)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((72.6604, -1622.36, 606.798), (1, 0.8, 0), 220.92)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((430.605, -1646.96, -5.90247), (1, 0.899083, 0.899083), 203.629)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((678.057, -1852.79, -403), (1, 0.889908, 0.889908), 232.701)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((1008.18, -2127.52, -259.157), (1, 0.880734, 0.880734), 177.704)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((1418.01, -2404.81, -12.2032), (1, 0.87156, 0.87156), 321.997)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((1802.07, -2644.27, 250.149), (1, 0.862385, 0.862385), 93.5705)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((1662.83, -2381.38, 63.0459), (1, 0.853211, 0.853211), 186.751)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((1740.81, -2112.67, -336.802), (1, 0.844037, 0.844037), 246.52)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((1794, -2028.33, -769.48), (1, 0.834862, 0.834862), 136.527)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((2026.12, -2025.84, -987.287), (1, 0.825688, 0.825688), 57.5134)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((2115.7, -2211.82, -867.228), (1, 0.816514, 0.816514), 214.173)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((1754.21, -2188.8, -581.502), (1, 0.807339, 0.807339), 182.368)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((1314.15, -1997.71, -384.541), (1, 0.798165, 0.798165), 298.436)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((1678.81, -1729.04, -398.052), (1, 0.788991, 0.788991), 149.565)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((1535.32, -1501, -144.743), (1, 0.779817, 0.779817), 199.269)
if "particle_134 geometry" not in marker_sets:
  s=new_marker_set('particle_134 geometry')
  marker_sets["particle_134 geometry"]=s
s= marker_sets["particle_134 geometry"]
mark=s.place_marker((1411.07, -1369.06, 197.168), (1, 0.770642, 0.770642), 179.114)
if "particle_135 geometry" not in marker_sets:
  s=new_marker_set('particle_135 geometry')
  marker_sets["particle_135 geometry"]=s
s= marker_sets["particle_135 geometry"]
mark=s.place_marker((1765.31, -1610.31, 83.7584), (1, 0.761468, 0.761468), 190.851)
if "particle_136 geometry" not in marker_sets:
  s=new_marker_set('particle_136 geometry')
  marker_sets["particle_136 geometry"]=s
s= marker_sets["particle_136 geometry"]
mark=s.place_marker((2252.19, -1870.69, 40.8552), (1, 0.752294, 0.752294), 218.555)
if "particle_137 geometry" not in marker_sets:
  s=new_marker_set('particle_137 geometry')
  marker_sets["particle_137 geometry"]=s
s= marker_sets["particle_137 geometry"]
mark=s.place_marker((2411.01, -2250, 357.089), (1, 0.743119, 0.743119), 233.612)
if "particle_138 geometry" not in marker_sets:
  s=new_marker_set('particle_138 geometry')
  marker_sets["particle_138 geometry"]=s
s= marker_sets["particle_138 geometry"]
mark=s.place_marker((2438.3, -2763.09, 648.361), (1, 0.733945, 0.733945), 315.467)
if "particle_139 geometry" not in marker_sets:
  s=new_marker_set('particle_139 geometry')
  marker_sets["particle_139 geometry"]=s
s= marker_sets["particle_139 geometry"]
mark=s.place_marker((2237.16, -3128.06, 405.933), (1, 0.724771, 0.724771), 150.455)
if "particle_140 geometry" not in marker_sets:
  s=new_marker_set('particle_140 geometry')
  marker_sets["particle_140 geometry"]=s
s= marker_sets["particle_140 geometry"]
mark=s.place_marker((2107.87, -3255.95, 708.433), (1, 0.715596, 0.715596), 135.963)
if "particle_141 geometry" not in marker_sets:
  s=new_marker_set('particle_141 geometry')
  marker_sets["particle_141 geometry"]=s
s= marker_sets["particle_141 geometry"]
mark=s.place_marker((1623.39, -2987.37, 733.76), (1, 0.706422, 0.706422), 302.45)
if "particle_142 geometry" not in marker_sets:
  s=new_marker_set('particle_142 geometry')
  marker_sets["particle_142 geometry"]=s
s= marker_sets["particle_142 geometry"]
mark=s.place_marker((1927.34, -3053.79, 1048.08), (1, 0.697248, 0.697248), 231.421)
if "particle_143 geometry" not in marker_sets:
  s=new_marker_set('particle_143 geometry')
  marker_sets["particle_143 geometry"]=s
s= marker_sets["particle_143 geometry"]
mark=s.place_marker((2181.09, -3403.29, 1291.05), (1, 0.688073, 0.688073), 226.648)
if "particle_144 geometry" not in marker_sets:
  s=new_marker_set('particle_144 geometry')
  marker_sets["particle_144 geometry"]=s
s= marker_sets["particle_144 geometry"]
mark=s.place_marker((1518.53, -2974.27, 1182.12), (1, 0.678899, 0.678899), 245.826)
if "particle_145 geometry" not in marker_sets:
  s=new_marker_set('particle_145 geometry')
  marker_sets["particle_145 geometry"]=s
s= marker_sets["particle_145 geometry"]
mark=s.place_marker((927.346, -2538.52, 1153.86), (1, 0.669725, 0.669725), 213.088)
if "particle_146 geometry" not in marker_sets:
  s=new_marker_set('particle_146 geometry')
  marker_sets["particle_146 geometry"]=s
s= marker_sets["particle_146 geometry"]
mark=s.place_marker((983.379, -2382.92, 1464.51), (1, 0.66055, 0.66055), 330.046)
if "particle_147 geometry" not in marker_sets:
  s=new_marker_set('particle_147 geometry')
  marker_sets["particle_147 geometry"]=s
s= marker_sets["particle_147 geometry"]
mark=s.place_marker((1619.25, -2700.85, 1398.68), (1, 0.651376, 0.651376), 244.351)
if "particle_148 geometry" not in marker_sets:
  s=new_marker_set('particle_148 geometry')
  marker_sets["particle_148 geometry"]=s
s= marker_sets["particle_148 geometry"]
mark=s.place_marker((1582.47, -2584.48, 1821.86), (1, 0.642202, 0.642202), 195.472)
if "particle_149 geometry" not in marker_sets:
  s=new_marker_set('particle_149 geometry')
  marker_sets["particle_149 geometry"]=s
s= marker_sets["particle_149 geometry"]
mark=s.place_marker((1961.68, -2553.1, 1777.75), (1, 0.633028, 0.633028), 124.052)
if "particle_150 geometry" not in marker_sets:
  s=new_marker_set('particle_150 geometry')
  marker_sets["particle_150 geometry"]=s
s= marker_sets["particle_150 geometry"]
mark=s.place_marker((1975.38, -2200.03, 1739.45), (1, 0.623853, 0.623853), 189.202)
if "particle_151 geometry" not in marker_sets:
  s=new_marker_set('particle_151 geometry')
  marker_sets["particle_151 geometry"]=s
s= marker_sets["particle_151 geometry"]
mark=s.place_marker((1492.58, -1919.41, 1700.75), (1, 0.614679, 0.614679), 225.368)
if "particle_152 geometry" not in marker_sets:
  s=new_marker_set('particle_152 geometry')
  marker_sets["particle_152 geometry"]=s
s= marker_sets["particle_152 geometry"]
mark=s.place_marker((1128.27, -1473.81, 1846.25), (1, 0.8, 0), 173.452)
if "particle_153 geometry" not in marker_sets:
  s=new_marker_set('particle_153 geometry')
  marker_sets["particle_153 geometry"]=s
s= marker_sets["particle_153 geometry"]
mark=s.place_marker((1711.07, -1811.9, 2131.52), (1, 0.59633, 0.59633), 396.476)
if "particle_154 geometry" not in marker_sets:
  s=new_marker_set('particle_154 geometry')
  marker_sets["particle_154 geometry"]=s
s= marker_sets["particle_154 geometry"]
mark=s.place_marker((2298.99, -2249.2, 2448.47), (1, 0.587156, 0.587156), 212.806)
if "particle_155 geometry" not in marker_sets:
  s=new_marker_set('particle_155 geometry')
  marker_sets["particle_155 geometry"]=s
s= marker_sets["particle_155 geometry"]
mark=s.place_marker((1927.76, -2413.68, 2199.79), (1, 0.577982, 0.577982), 159.024)
if "particle_156 geometry" not in marker_sets:
  s=new_marker_set('particle_156 geometry')
  marker_sets["particle_156 geometry"]=s
s= marker_sets["particle_156 geometry"]
mark=s.place_marker((1543.12, -2340.6, 1974.29), (1, 0.568807, 0.568807), 173.951)
if "particle_157 geometry" not in marker_sets:
  s=new_marker_set('particle_157 geometry')
  marker_sets["particle_157 geometry"]=s
s= marker_sets["particle_157 geometry"]
mark=s.place_marker((1372.35, -2226.37, 1597.43), (1, 0.559633, 0.559633), 205.495)
if "particle_158 geometry" not in marker_sets:
  s=new_marker_set('particle_158 geometry')
  marker_sets["particle_158 geometry"]=s
s= marker_sets["particle_158 geometry"]
mark=s.place_marker((1673.27, -2219.56, 1203.83), (1, 0.550459, 0.550459), 250.664)
if "particle_159 geometry" not in marker_sets:
  s=new_marker_set('particle_159 geometry')
  marker_sets["particle_159 geometry"]=s
s= marker_sets["particle_159 geometry"]
mark=s.place_marker((2060.52, -2087.51, 737.543), (1, 0.541284, 0.541284), 321.693)
if "particle_160 geometry" not in marker_sets:
  s=new_marker_set('particle_160 geometry')
  marker_sets["particle_160 geometry"]=s
s= marker_sets["particle_160 geometry"]
mark=s.place_marker((1879.37, -1751.61, 400.99), (1, 0.53211, 0.53211), 190.829)
if "particle_161 geometry" not in marker_sets:
  s=new_marker_set('particle_161 geometry')
  marker_sets["particle_161 geometry"]=s
s= marker_sets["particle_161 geometry"]
mark=s.place_marker((2149, -1570.66, 200.796), (1, 0.522936, 0.522936), 201.655)
if "particle_162 geometry" not in marker_sets:
  s=new_marker_set('particle_162 geometry')
  marker_sets["particle_162 geometry"]=s
s= marker_sets["particle_162 geometry"]
mark=s.place_marker((2606.67, -1647.38, -8.00795), (1, 0.513761, 0.513761), 261.642)
if "particle_163 geometry" not in marker_sets:
  s=new_marker_set('particle_163 geometry')
  marker_sets["particle_163 geometry"]=s
s= marker_sets["particle_163 geometry"]
mark=s.place_marker((2838.99, -2020.95, 10.1547), (1, 0.504587, 0.504587), 163.754)
if "particle_164 geometry" not in marker_sets:
  s=new_marker_set('particle_164 geometry')
  marker_sets["particle_164 geometry"]=s
s= marker_sets["particle_164 geometry"]
mark=s.place_marker((2485.62, -2230.74, -25.785), (1, 0.495413, 0.495413), 235.998)
if "particle_165 geometry" not in marker_sets:
  s=new_marker_set('particle_165 geometry')
  marker_sets["particle_165 geometry"]=s
s= marker_sets["particle_165 geometry"]
mark=s.place_marker((2006.55, -2455.26, -195.19), (1, 0.486239, 0.486239), 301.018)
if "particle_166 geometry" not in marker_sets:
  s=new_marker_set('particle_166 geometry')
  marker_sets["particle_166 geometry"]=s
s= marker_sets["particle_166 geometry"]
mark=s.place_marker((2067.24, -2666.05, -594.175), (1, 0.477064, 0.477064), 153.449)
if "particle_167 geometry" not in marker_sets:
  s=new_marker_set('particle_167 geometry')
  marker_sets["particle_167 geometry"]=s
s= marker_sets["particle_167 geometry"]
mark=s.place_marker((2404.94, -2683.45, -402.36), (1, 0.46789, 0.46789), 197.012)
if "particle_168 geometry" not in marker_sets:
  s=new_marker_set('particle_168 geometry')
  marker_sets["particle_168 geometry"]=s
s= marker_sets["particle_168 geometry"]
mark=s.place_marker((2429.25, -2606.56, 103.191), (1, 0.458716, 0.458716), 235.89)
if "particle_169 geometry" not in marker_sets:
  s=new_marker_set('particle_169 geometry')
  marker_sets["particle_169 geometry"]=s
s= marker_sets["particle_169 geometry"]
mark=s.place_marker((2056.92, -2416.83, 578.847), (1, 0.449541, 0.449541), 223.979)
if "particle_170 geometry" not in marker_sets:
  s=new_marker_set('particle_170 geometry')
  marker_sets["particle_170 geometry"]=s
s= marker_sets["particle_170 geometry"]
mark=s.place_marker((1973.45, -2194.97, 992.366), (1, 0.440367, 0.440367), 169.85)
if "particle_171 geometry" not in marker_sets:
  s=new_marker_set('particle_171 geometry')
  marker_sets["particle_171 geometry"]=s
s= marker_sets["particle_171 geometry"]
mark=s.place_marker((2357.23, -1895.84, 1086.89), (1, 0.431193, 0.431193), 275.657)
if "particle_172 geometry" not in marker_sets:
  s=new_marker_set('particle_172 geometry')
  marker_sets["particle_172 geometry"]=s
s= marker_sets["particle_172 geometry"]
mark=s.place_marker((2311.89, -1458.12, 1145.6), (1, 0.422018, 0.422018), 138.327)
if "particle_173 geometry" not in marker_sets:
  s=new_marker_set('particle_173 geometry')
  marker_sets["particle_173 geometry"]=s
s= marker_sets["particle_173 geometry"]
mark=s.place_marker((2488.45, -1313.59, 1428.42), (1, 0.412844, 0.412844), 194.192)
if "particle_174 geometry" not in marker_sets:
  s=new_marker_set('particle_174 geometry')
  marker_sets["particle_174 geometry"]=s
s= marker_sets["particle_174 geometry"]
mark=s.place_marker((2875.39, -1336.85, 1808.88), (1, 0.40367, 0.40367), 252.899)
if "particle_175 geometry" not in marker_sets:
  s=new_marker_set('particle_175 geometry')
  marker_sets["particle_175 geometry"]=s
s= marker_sets["particle_175 geometry"]
mark=s.place_marker((2741.35, -1361.1, 2367.59), (1, 0.394495, 0.394495), 216.147)
if "particle_176 geometry" not in marker_sets:
  s=new_marker_set('particle_176 geometry')
  marker_sets["particle_176 geometry"]=s
s= marker_sets["particle_176 geometry"]
mark=s.place_marker((2158.07, -1284.75, 2642.61), (1, 0.385321, 0.385321), 300.389)
if "particle_177 geometry" not in marker_sets:
  s=new_marker_set('particle_177 geometry')
  marker_sets["particle_177 geometry"]=s
s= marker_sets["particle_177 geometry"]
mark=s.place_marker((2352.34, -725.155, 2863.75), (1, 0.376147, 0.376147), 251.206)
if "particle_178 geometry" not in marker_sets:
  s=new_marker_set('particle_178 geometry')
  marker_sets["particle_178 geometry"]=s
s= marker_sets["particle_178 geometry"]
mark=s.place_marker((3001, -273.986, 3115.29), (1, 0.366972, 0.366972), 324.08)
if "particle_179 geometry" not in marker_sets:
  s=new_marker_set('particle_179 geometry')
  marker_sets["particle_179 geometry"]=s
s= marker_sets["particle_179 geometry"]
mark=s.place_marker((3698.8, 136.556, 3301.51), (1, 0.357798, 0.357798), 220.703)
if "particle_180 geometry" not in marker_sets:
  s=new_marker_set('particle_180 geometry')
  marker_sets["particle_180 geometry"]=s
s= marker_sets["particle_180 geometry"]
mark=s.place_marker((4185.43, 640.228, 3231.39), (1, 0.348624, 0.348624), 301.908)
if "particle_181 geometry" not in marker_sets:
  s=new_marker_set('particle_181 geometry')
  marker_sets["particle_181 geometry"]=s
s= marker_sets["particle_181 geometry"]
mark=s.place_marker((4404.69, 1060.13, 3207.48), (1, 0.33945, 0.33945), 11.4116)
if "particle_182 geometry" not in marker_sets:
  s=new_marker_set('particle_182 geometry')
  marker_sets["particle_182 geometry"]=s
s= marker_sets["particle_182 geometry"]
mark=s.place_marker((3983.2, 891.248, 2976.68), (1, 0.330275, 0.330275), 151.626)
if "particle_183 geometry" not in marker_sets:
  s=new_marker_set('particle_183 geometry')
  marker_sets["particle_183 geometry"]=s
s= marker_sets["particle_183 geometry"]
mark=s.place_marker((3580.2, 857.478, 2482.42), (1, 0.321101, 0.321101), 363.608)
if "particle_184 geometry" not in marker_sets:
  s=new_marker_set('particle_184 geometry')
  marker_sets["particle_184 geometry"]=s
s= marker_sets["particle_184 geometry"]
mark=s.place_marker((3435.36, 1258.93, 1962.8), (1, 0.311927, 0.311927), 215.974)
if "particle_185 geometry" not in marker_sets:
  s=new_marker_set('particle_185 geometry')
  marker_sets["particle_185 geometry"]=s
s= marker_sets["particle_185 geometry"]
mark=s.place_marker((2874.79, 1028.95, 1749.35), (1, 0.302752, 0.302752), 247.106)
if "particle_186 geometry" not in marker_sets:
  s=new_marker_set('particle_186 geometry')
  marker_sets["particle_186 geometry"]=s
s= marker_sets["particle_186 geometry"]
mark=s.place_marker((2405.55, 1046.94, 1818.6), (1, 0.293578, 0.293578), 172.128)
if "particle_187 geometry" not in marker_sets:
  s=new_marker_set('particle_187 geometry')
  marker_sets["particle_187 geometry"]=s
s= marker_sets["particle_187 geometry"]
mark=s.place_marker((2604.29, 1452.75, 1837.44), (1, 0.284404, 0.284404), 190.591)
if "particle_188 geometry" not in marker_sets:
  s=new_marker_set('particle_188 geometry')
  marker_sets["particle_188 geometry"]=s
s= marker_sets["particle_188 geometry"]
mark=s.place_marker((2957.45, 1665.9, 1971.92), (1, 0.275229, 0.275229), 229.967)
if "particle_189 geometry" not in marker_sets:
  s=new_marker_set('particle_189 geometry')
  marker_sets["particle_189 geometry"]=s
s= marker_sets["particle_189 geometry"]
mark=s.place_marker((3317.7, 2010.91, 1997.72), (1, 0.266055, 0.266055), 176.185)
if "particle_190 geometry" not in marker_sets:
  s=new_marker_set('particle_190 geometry')
  marker_sets["particle_190 geometry"]=s
s= marker_sets["particle_190 geometry"]
mark=s.place_marker((2970.44, 2355.53, 2111.22), (1, 0.256881, 0.256881), 313.341)
if "particle_191 geometry" not in marker_sets:
  s=new_marker_set('particle_191 geometry')
  marker_sets["particle_191 geometry"]=s
s= marker_sets["particle_191 geometry"]
mark=s.place_marker((2836.64, 1901.23, 1616.95), (1, 0.247706, 0.247706), 321.889)
if "particle_192 geometry" not in marker_sets:
  s=new_marker_set('particle_192 geometry')
  marker_sets["particle_192 geometry"]=s
s= marker_sets["particle_192 geometry"]
mark=s.place_marker((3264.1, 1974.05, 1226.79), (1, 0.238532, 0.238532), 178.962)
if "particle_193 geometry" not in marker_sets:
  s=new_marker_set('particle_193 geometry')
  marker_sets["particle_193 geometry"]=s
s= marker_sets["particle_193 geometry"]
mark=s.place_marker((3388.44, 1768.33, 853.074), (1, 0.229358, 0.229358), 205.929)
if "particle_194 geometry" not in marker_sets:
  s=new_marker_set('particle_194 geometry')
  marker_sets["particle_194 geometry"]=s
s= marker_sets["particle_194 geometry"]
mark=s.place_marker((3430.49, 1451.06, 416.092), (1, 0.220183, 0.220183), 295.725)
if "particle_195 geometry" not in marker_sets:
  s=new_marker_set('particle_195 geometry')
  marker_sets["particle_195 geometry"]=s
s= marker_sets["particle_195 geometry"]
mark=s.place_marker((3402.38, 879.341, 34.4937), (1, 0.211009, 0.211009), 373.328)
if "particle_196 geometry" not in marker_sets:
  s=new_marker_set('particle_196 geometry')
  marker_sets["particle_196 geometry"]=s
s= marker_sets["particle_196 geometry"]
mark=s.place_marker((3920.29, 875.073, 100.334), (1, 0.201835, 0.201835), 139.39)
if "particle_197 geometry" not in marker_sets:
  s=new_marker_set('particle_197 geometry')
  marker_sets["particle_197 geometry"]=s
s= marker_sets["particle_197 geometry"]
mark=s.place_marker((4312.7, 878.415, 215.573), (1, 0.192661, 0.192661), 221.267)
if "particle_198 geometry" not in marker_sets:
  s=new_marker_set('particle_198 geometry')
  marker_sets["particle_198 geometry"]=s
s= marker_sets["particle_198 geometry"]
mark=s.place_marker((4232.62, 481.817, 491.557), (1, 0.183486, 0.183486), 172.041)
if "particle_199 geometry" not in marker_sets:
  s=new_marker_set('particle_199 geometry')
  marker_sets["particle_199 geometry"]=s
s= marker_sets["particle_199 geometry"]
mark=s.place_marker((4318.34, 210.281, 765.45), (1, 0.174312, 0.174312), 179.808)
if "particle_200 geometry" not in marker_sets:
  s=new_marker_set('particle_200 geometry')
  marker_sets["particle_200 geometry"]=s
s= marker_sets["particle_200 geometry"]
mark=s.place_marker((4368.02, -73.634, 1139.73), (1, 0.165138, 0.165138), 267.586)
if "particle_201 geometry" not in marker_sets:
  s=new_marker_set('particle_201 geometry')
  marker_sets["particle_201 geometry"]=s
s= marker_sets["particle_201 geometry"]
mark=s.place_marker((3979.57, -318.133, 1155.36), (1, 0.155963, 0.155963), 98.4736)
if "particle_202 geometry" not in marker_sets:
  s=new_marker_set('particle_202 geometry')
  marker_sets["particle_202 geometry"]=s
s= marker_sets["particle_202 geometry"]
mark=s.place_marker((3875.4, -715.987, 983.017), (1, 0.146789, 0.146789), 318.765)
if "particle_203 geometry" not in marker_sets:
  s=new_marker_set('particle_203 geometry')
  marker_sets["particle_203 geometry"]=s
s= marker_sets["particle_203 geometry"]
mark=s.place_marker((4113.8, -309.954, 967.95), (1, 0.137615, 0.137615), 206.493)
if "particle_204 geometry" not in marker_sets:
  s=new_marker_set('particle_204 geometry')
  marker_sets["particle_204 geometry"]=s
s= marker_sets["particle_204 geometry"]
mark=s.place_marker((3387.67, -460.32, 1020.16), (1, 0.12844, 0.12844), 290.344)
if "particle_205 geometry" not in marker_sets:
  s=new_marker_set('particle_205 geometry')
  marker_sets["particle_205 geometry"]=s
s= marker_sets["particle_205 geometry"]
mark=s.place_marker((3652.64, -159.143, 728.973), (1, 0.119266, 0.119266), 136.809)
if "particle_206 geometry" not in marker_sets:
  s=new_marker_set('particle_206 geometry')
  marker_sets["particle_206 geometry"]=s
s= marker_sets["particle_206 geometry"]
mark=s.place_marker((4115.96, 74.2345, 516.866), (1, 0.110092, 0.110092), 205.842)
if "particle_207 geometry" not in marker_sets:
  s=new_marker_set('particle_207 geometry')
  marker_sets["particle_207 geometry"]=s
s= marker_sets["particle_207 geometry"]
mark=s.place_marker((3966.33, 170.44, 160.398), (1, 0.100917, 0.100917), 157.679)
if "particle_208 geometry" not in marker_sets:
  s=new_marker_set('particle_208 geometry')
  marker_sets["particle_208 geometry"]=s
s= marker_sets["particle_208 geometry"]
mark=s.place_marker((3994.17, 287.644, -221.81), (1, 0.0917431, 0.0917431), 226.713)
if "particle_209 geometry" not in marker_sets:
  s=new_marker_set('particle_209 geometry')
  marker_sets["particle_209 geometry"]=s
s= marker_sets["particle_209 geometry"]
mark=s.place_marker((3907.03, 568.593, 48.6477), (1, 0.0825688, 0.0825688), 181.999)
if "particle_210 geometry" not in marker_sets:
  s=new_marker_set('particle_210 geometry')
  marker_sets["particle_210 geometry"]=s
s= marker_sets["particle_210 geometry"]
mark=s.place_marker((4105.7, 525.137, 347.513), (1, 0.0733945, 0.0733945), 136.114)
if "particle_211 geometry" not in marker_sets:
  s=new_marker_set('particle_211 geometry')
  marker_sets["particle_211 geometry"]=s
s= marker_sets["particle_211 geometry"]
mark=s.place_marker((4072.28, 392.815, 696.366), (1, 0.0642202, 0.0642202), 175.252)
if "particle_212 geometry" not in marker_sets:
  s=new_marker_set('particle_212 geometry')
  marker_sets["particle_212 geometry"]=s
s= marker_sets["particle_212 geometry"]
mark=s.place_marker((4343.48, 451.304, 986.362), (1, 0.0550459, 0.0550459), 165.251)
if "particle_213 geometry" not in marker_sets:
  s=new_marker_set('particle_213 geometry')
  marker_sets["particle_213 geometry"]=s
s= marker_sets["particle_213 geometry"]
mark=s.place_marker((4746.92, 654.01, 1111.64), (1, 0.0458716, 0.0458716), 160.521)
if "particle_214 geometry" not in marker_sets:
  s=new_marker_set('particle_214 geometry')
  marker_sets["particle_214 geometry"]=s
s= marker_sets["particle_214 geometry"]
mark=s.place_marker((5257.93, 918.299, 1182.12), (1, 0.0366972, 0.0366972), 165.793)
if "particle_215 geometry" not in marker_sets:
  s=new_marker_set('particle_215 geometry')
  marker_sets["particle_215 geometry"]=s
s= marker_sets["particle_215 geometry"]
mark=s.place_marker((5131.29, 1067.68, 1490.38), (1, 0.0275229, 0.0275229), 194.235)
if "particle_216 geometry" not in marker_sets:
  s=new_marker_set('particle_216 geometry')
  marker_sets["particle_216 geometry"]=s
s= marker_sets["particle_216 geometry"]
mark=s.place_marker((4805.1, 856.691, 1551.82), (1, 0.0183486, 0.0183486), 150.607)
if "particle_217 geometry" not in marker_sets:
  s=new_marker_set('particle_217 geometry')
  marker_sets["particle_217 geometry"]=s
s= marker_sets["particle_217 geometry"]
mark=s.place_marker((5100.64, 799.609, 1774.53), (1, 0.00917431, 0.00917431), 222.938)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
