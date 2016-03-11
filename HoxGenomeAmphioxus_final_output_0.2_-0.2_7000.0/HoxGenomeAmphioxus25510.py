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
mark=s.place_marker((-981.943, -2566.43, -4439.46), (0, 0, 1), 201.612)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((-893.176, -2478.96, -3924.39), (0.00947867, 0.00947867, 1), 254.309)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((-1128.91, -2225.37, -3580.11), (0.0189573, 0.0189573, 1), 183.366)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((-1281.66, -1896.82, -3272.57), (0.028436, 0.028436, 1), 225.888)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((-1418.17, -1426.44, -2988.29), (0.0379147, 0.0379147, 1), 222.634)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((-1880.94, -1237.97, -2987.25), (0.0473934, 0.0473934, 1), 191.111)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((-2182.86, -1372.55, -3433.93), (0.056872, 0.056872, 1), 109.473)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((-2479.1, -1245.89, -3863.45), (0.0663507, 0.0663507, 1), 208.923)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((-2612.12, -899.542, -4057.28), (0.0758294, 0.0758294, 1), 122.729)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((-2353.2, -623.515, -4096.4), (0.0853081, 0.0853081, 1), 153.948)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((-1996.71, -355.598, -4137.42), (0.0947867, 0.0947867, 1), 178.073)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((-1666.35, -260.153, -3668.35), (0.104265, 0.104265, 1), 202.935)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((-1424.4, -18.4382, -3401.86), (0.113744, 0.113744, 1), 120.017)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((-1474.69, 211.447, -3242.37), (0.123223, 0.123223, 1), 131.233)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((-1810.17, 31.8336, -3747.63), (0.132701, 0.132701, 1), 193.91)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((-2002.69, 61.3825, -4255.21), (0.14218, 0.14218, 1), 103.745)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((-1992.04, 415.855, -4478.56), (0.151659, 0.151659, 1), 145.986)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((-1473.83, 555.668, -3613.58), (0.161137, 0.161137, 1), 229.143)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((-902.25, 776.05, -2558.81), (1, 0.8, 0), 171.629)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((-1130.1, 657.092, -3122.75), (0.180095, 0.180095, 1), 138.566)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((-1079.42, 275.026, -3233.34), (0.189573, 0.189573, 1), 144.337)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((-994.969, 47.04, -2875.01), (0.199052, 0.199052, 1), 253.072)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((-1401.15, -101.407, -2743.37), (0.208531, 0.208531, 1), 195.906)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((-1769.11, -158.886, -2981.18), (0.218009, 0.218009, 1), 169.416)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((-2146.58, 73.949, -3281.2), (0.227488, 0.227488, 1), 310.152)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((-2258.9, 591.412, -2988.16), (0.236967, 0.236967, 1), 191.892)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((-2667.27, 777.708, -3127.83), (0.246445, 0.246445, 1), 112.163)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((-2821.75, 588.664, -3185.7), (0.255924, 0.255924, 1), 197.728)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((-3172.39, 617.057, -2909.61), (0.265403, 0.265403, 1), 221.007)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((-3240.48, 316.481, -2541.02), (0.274882, 0.274882, 1), 209.118)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((-2969.08, 27.7909, -2064.34), (0.28436, 0.28436, 1), 226.517)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((-3218.32, -409.83, -1904.54), (0.293839, 0.293839, 1), 140.171)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((-3677.12, -827.925, -1997.31), (0.303318, 0.303318, 1), 241.509)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((-3791.17, -1405.06, -2097.4), (0.312796, 0.312796, 1), 194.582)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((-3471.96, -1532.45, -2283.43), (0.322275, 0.322275, 1), 149.934)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((-3216.54, -1247.87, -1910.63), (0.331754, 0.331754, 1), 197.967)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((-3354.84, -1400.85, -1577.76), (0.341232, 0.341232, 1), 120.277)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((-3130.26, -1479.75, -1174.24), (0.350711, 0.350711, 1), 149.522)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((-2923.09, -1754.99, -1163.38), (0.36019, 0.36019, 1), 160.803)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((-3114.45, -1920.54, -1731.9), (0.369668, 0.369668, 1), 149.869)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((-3073.4, -1745.65, -2143.99), (0.379147, 0.379147, 1), 181.37)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((-3037.28, -1645.8, -1669.96), (0.388626, 0.388626, 1), 229.511)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((-3230.03, -1911.69, -1076.26), (0.398104, 0.398104, 1), 264.093)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((-3408.59, -2077.79, -684.003), (0.407583, 0.407583, 1), 177.617)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((-3199.3, -1632.14, -692.35), (0.417062, 0.417062, 1), 167.16)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((-3525.77, -1253.42, -561.851), (0.42654, 0.42654, 1), 142.536)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((-3922.39, -960.302, -340.177), (0.436019, 0.436019, 1), 189.571)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((-3887.7, -707.009, 243.154), (0.445498, 0.445498, 1), 222.244)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((-4067.29, -303.491, 348.307), (0.454976, 0.454976, 1), 137.438)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((-3934.24, 145.315, 156.963), (0.464455, 0.464455, 1), 225.953)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((-4207.84, 491.003, -156.62), (0.473934, 0.473934, 1), 202.545)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((-3947.18, 580.134, -454.074), (0.483412, 0.483412, 1), 160.955)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((-3509.9, 681.032, -290.04), (0.492891, 0.492891, 1), 146.767)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((-2867.53, 861.729, -80.3462), (0.50237, 0.50237, 1), 169.351)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((-2434.31, 1060.39, -209.586), (0.511848, 0.511848, 1), 186.968)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((-1951.17, 1340.67, -117.151), (0.521327, 0.521327, 1), 217.883)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((-1437.61, 1636.39, 72.724), (0.530806, 0.530806, 1), 238.667)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((-1179.32, 2039.17, 95.839), (0.540284, 0.540284, 1), 157.94)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((-1372.42, 2387.53, -102.834), (0.549763, 0.549763, 1), 182.477)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((-999.631, 2041.81, 64.1427), (0.559242, 0.559242, 1), 341.892)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((-1180.3, 2729.78, 145.74), (0.56872, 0.56872, 1), 245.002)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((-1488.31, 3077.28, 371.92), (0.578199, 0.578199, 1), 147.786)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((-1583.48, 2689.37, 555.303), (0.587678, 0.587678, 1), 157.354)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((-1547.54, 2235.3, 859.909), (0.597156, 0.597156, 1), 278.238)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((-1525.84, 2231.59, 1390.99), (0.606635, 0.606635, 1), 211.136)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((-1962.15, 2556.82, 1642.56), (1, 0.8, 0), 195.667)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((-1294.35, 2360.31, 1291.55), (0.625592, 0.625592, 1), 206.797)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((-720.695, 2253.08, 1111.38), (0.635071, 0.635071, 1), 192.153)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((-193.299, 2317.05, 1150.6), (0.64455, 0.64455, 1), 211.505)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((70.9405, 2686.15, 1426.33), (0.654028, 0.654028, 1), 199.29)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((243.461, 3279.01, 1823.34), (0.663507, 0.663507, 1), 201.937)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((234.628, 3654.71, 2265.8), (0.672986, 0.672986, 1), 115.895)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((133.131, 3149.15, 2242.87), (0.682464, 0.682464, 1), 162.756)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((-54.5222, 2818.03, 2333.34), (0.691943, 0.691943, 1), 172.996)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((-119.42, 2424.42, 2533.92), (0.701422, 0.701422, 1), 270.103)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((-533.499, 2133.91, 2622.26), (0.7109, 0.7109, 1), 231.551)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((-889.352, 1806.1, 2098.92), (1, 0.8, 0), 193.867)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((-542.45, 1852.46, 1602.47), (0.729858, 0.729858, 1), 148.047)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((-346.851, 1755.54, 1304.44), (0.739336, 0.739336, 1), 219.553)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((-315.5, 2122.93, 1626.69), (0.748815, 0.748815, 1), 263.79)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((-511.059, 1767.35, 1021), (0.758294, 0.758294, 1), 165.967)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((-715.355, 1324.9, 785.134), (0.767773, 0.767773, 1), 208.706)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((-1058.35, 1164.69, 1010.12), (0.777251, 0.777251, 1), 120.928)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((-1197.1, 1035.44, 1336.66), (0.78673, 0.78673, 1), 243.765)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((-1150.13, 730.374, 1570.78), (0.796209, 0.796209, 1), 206.558)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((-1206.67, 974.181, 2050.85), (1, 0.3, 0), 187.488)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((-908.203, 885.761, 1381.12), (0.815166, 0.815166, 1), 227.45)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((-321.682, 939.573, 1441.48), (0.824645, 0.824645, 1), 288.522)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((67.6113, 1307.68, 1285.4), (0.834123, 0.834123, 1), 208.554)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((127.172, 1246.5, 1748.18), (0.843602, 0.843602, 1), 212.524)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((373.448, 1465.03, 2131.23), (0.853081, 0.853081, 1), 251.51)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((425.517, 1551.68, 1921.89), (0.862559, 0.862559, 1), 216.364)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((111.885, 998.479, 1951.82), (0.872038, 0.872038, 1), 241.661)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((127.92, 890.4, 2245.98), (0.881517, 0.881517, 1), 243.613)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((242.146, 769.147, 2730.31), (0.890995, 0.890995, 1), 259.581)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((-43.0575, 778.758, 2907.16), (0.900474, 0.900474, 1), 174.081)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((-384.181, 568.924, 2653.11), (1, 0.3, 0), 132.665)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((-391.961, 643.299, 3206.48), (1, 0.3, 0), 201.612)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((89.2732, 588.634, 3102.82), (0.92891, 0.92891, 1), 160.109)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((96.1228, 435.082, 2748.3), (0.938389, 0.938389, 1), 155.119)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((304.474, 344.204, 2574.41), (0.947867, 0.947867, 1), 239.187)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((130.626, 117.705, 2799.62), (0.957346, 0.957346, 1), 121.145)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((-422.874, 50.2946, 2574.49), (1, 0.3, 0), 228.513)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((-75.1087, 143.124, 2023.77), (0.976303, 0.976303, 1), 147.7)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((341.071, 134.142, 2273.51), (0.985782, 0.985782, 1), 217.948)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((159.537, 245.086, 1874.43), (1, 0.3, 0), 190.374)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((228.983, 725.24, 1522.27), (1, 0.995261, 0.995261), 245.088)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((648.37, 968.379, 1733.43), (1, 0.985782, 0.985782), 175.534)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((1040.92, 991.131, 2003.94), (1, 0.976303, 0.976303), 215.41)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((1248.49, 601.195, 2300.54), (1, 0.966825, 0.966825), 253.463)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((1327.83, 277.119, 2746.4), (1, 0.957346, 0.957346), 256.739)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((1036.72, 40.8732, 2773.31), (1, 0.947867, 0.947867), 151.236)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((981.938, 137.251, 2328.81), (1, 0.938389, 0.938389), 197.75)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((792.866, 172.444, 1700.18), (1, 0.92891, 0.92891), 280.994)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((1156.71, 65.6367, 1872.96), (1, 0.919431, 0.919431), 265.026)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((1076.42, -136.282, 2416.64), (1, 0.909953, 0.909953), 210.984)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((1076.15, -210.797, 1966.54), (1, 0.900474, 0.900474), 193.91)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((822.469, -256.685, 1554.99), (1, 0.890995, 0.890995), 250.664)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((400.717, -350.823, 1331.68), (1, 0.881517, 0.881517), 203.716)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((674.68, -777.691, 1700.18), (1, 0.3, 0), 277.501)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((343.372, -942.559, 1982.45), (1, 0.862559, 0.862559), 198.791)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((104.818, -1023.57, 1550.93), (1, 0.3, 0), 162.647)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((254.688, -785.453, 2226.36), (1, 0.843602, 0.843602), 291.624)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((611.67, -629.14, 2712.38), (1, 0.834123, 0.834123), 174.471)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((987.849, -325.569, 2755.93), (1, 0.824645, 0.824645), 218.1)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((1324.94, -105.159, 2376.58), (1, 0.815166, 0.815166), 260.101)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((1835.44, -25.5638, 2372.52), (1, 0.805687, 0.805687), 184.69)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((2185.62, -15.6691, 2364.2), (1, 0.796209, 0.796209), 134.791)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((1721.03, 111.35, 2357.3), (1, 0.78673, 0.78673), 256.348)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((1431.34, -273.545, 2470.51), (1, 0.777251, 0.777251), 165.229)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((1349.78, -703.681, 2403.44), (1, 0.767773, 0.767773), 223.111)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((1413.7, -1154.56, 2291.92), (1, 0.758294, 0.758294), 163.428)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((1579.49, -1587.44, 2434.96), (1, 0.748815, 0.748815), 182.346)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((1314, -1651.88, 2331.79), (1, 0.739336, 0.739336), 148.784)
if "particle_134 geometry" not in marker_sets:
  s=new_marker_set('particle_134 geometry')
  marker_sets["particle_134 geometry"]=s
s= marker_sets["particle_134 geometry"]
mark=s.place_marker((1111.45, -1315.8, 2235.02), (1, 0.729858, 0.729858), 239.318)
if "particle_135 geometry" not in marker_sets:
  s=new_marker_set('particle_135 geometry')
  marker_sets["particle_135 geometry"]=s
s= marker_sets["particle_135 geometry"]
mark=s.place_marker((1016.39, -1722.57, 2068.15), (1, 0.3, 0), 146.268)
if "particle_136 geometry" not in marker_sets:
  s=new_marker_set('particle_136 geometry')
  marker_sets["particle_136 geometry"]=s
s= marker_sets["particle_136 geometry"]
mark=s.place_marker((1439.72, -1712.26, 2284.08), (1, 0.7109, 0.7109), 187.163)
if "particle_137 geometry" not in marker_sets:
  s=new_marker_set('particle_137 geometry')
  marker_sets["particle_137 geometry"]=s
s= marker_sets["particle_137 geometry"]
mark=s.place_marker((1909.39, -2106.82, 2336.15), (1, 0.701422, 0.701422), 174.059)
if "particle_138 geometry" not in marker_sets:
  s=new_marker_set('particle_138 geometry')
  marker_sets["particle_138 geometry"]=s
s= marker_sets["particle_138 geometry"]
mark=s.place_marker((2350.18, -2600.32, 2316.47), (1, 0.691943, 0.691943), 155.032)
if "particle_139 geometry" not in marker_sets:
  s=new_marker_set('particle_139 geometry')
  marker_sets["particle_139 geometry"]=s
s= marker_sets["particle_139 geometry"]
mark=s.place_marker((2626.69, -2821.46, 2199.71), (1, 0.682464, 0.682464), 71.4199)
if "particle_140 geometry" not in marker_sets:
  s=new_marker_set('particle_140 geometry')
  marker_sets["particle_140 geometry"]=s
s= marker_sets["particle_140 geometry"]
mark=s.place_marker((2530.23, -2428.68, 1846.31), (1, 0.672986, 0.672986), 364.085)
if "particle_141 geometry" not in marker_sets:
  s=new_marker_set('particle_141 geometry')
  marker_sets["particle_141 geometry"]=s
s= marker_sets["particle_141 geometry"]
mark=s.place_marker((2260.07, -1842.31, 1380.49), (1, 0.663507, 0.663507), 155.9)
if "particle_142 geometry" not in marker_sets:
  s=new_marker_set('particle_142 geometry')
  marker_sets["particle_142 geometry"]=s
s= marker_sets["particle_142 geometry"]
mark=s.place_marker((2345.37, -1608.84, 850.488), (1, 0.654028, 0.654028), 206.992)
if "particle_143 geometry" not in marker_sets:
  s=new_marker_set('particle_143 geometry')
  marker_sets["particle_143 geometry"]=s
s= marker_sets["particle_143 geometry"]
mark=s.place_marker((2349.07, -1535.72, 316.549), (1, 0.64455, 0.64455), 148.459)
if "particle_144 geometry" not in marker_sets:
  s=new_marker_set('particle_144 geometry')
  marker_sets["particle_144 geometry"]=s
s= marker_sets["particle_144 geometry"]
mark=s.place_marker((2066.72, -1126.76, 243.1), (1, 0.635071, 0.635071), 221.224)
if "particle_145 geometry" not in marker_sets:
  s=new_marker_set('particle_145 geometry')
  marker_sets["particle_145 geometry"]=s
s= marker_sets["particle_145 geometry"]
mark=s.place_marker((1866.49, -689.789, 73.1328), (1, 0.625592, 0.625592), 206.124)
if "particle_146 geometry" not in marker_sets:
  s=new_marker_set('particle_146 geometry')
  marker_sets["particle_146 geometry"]=s
s= marker_sets["particle_146 geometry"]
mark=s.place_marker((1443.33, -514.658, 49.032), (1, 0.616114, 0.616114), 151.388)
if "particle_147 geometry" not in marker_sets:
  s=new_marker_set('particle_147 geometry')
  marker_sets["particle_147 geometry"]=s
s= marker_sets["particle_147 geometry"]
mark=s.place_marker((1599.26, -1040.97, 317.719), (1, 0.8, 0), 177.378)
if "particle_148 geometry" not in marker_sets:
  s=new_marker_set('particle_148 geometry')
  marker_sets["particle_148 geometry"]=s
s= marker_sets["particle_148 geometry"]
mark=s.place_marker((2386.23, -1072.53, 271.598), (1, 0.597156, 0.597156), 191.458)
if "particle_149 geometry" not in marker_sets:
  s=new_marker_set('particle_149 geometry')
  marker_sets["particle_149 geometry"]=s
s= marker_sets["particle_149 geometry"]
mark=s.place_marker((3237.67, -1401.05, 233.668), (1, 0.587678, 0.587678), 249.579)
if "particle_150 geometry" not in marker_sets:
  s=new_marker_set('particle_150 geometry')
  marker_sets["particle_150 geometry"]=s
s= marker_sets["particle_150 geometry"]
mark=s.place_marker((4131.24, -1794.32, 143.166), (1, 0.578199, 0.578199), 151.735)
if "particle_151 geometry" not in marker_sets:
  s=new_marker_set('particle_151 geometry')
  marker_sets["particle_151 geometry"]=s
s= marker_sets["particle_151 geometry"]
mark=s.place_marker((3775.44, -1777.45, 541.235), (1, 0.56872, 0.56872), 124.573)
if "particle_152 geometry" not in marker_sets:
  s=new_marker_set('particle_152 geometry')
  marker_sets["particle_152 geometry"]=s
s= marker_sets["particle_152 geometry"]
mark=s.place_marker((3157.08, -1358.62, 745.793), (1, 0.559242, 0.559242), 184.342)
if "particle_153 geometry" not in marker_sets:
  s=new_marker_set('particle_153 geometry')
  marker_sets["particle_153 geometry"]=s
s= marker_sets["particle_153 geometry"]
mark=s.place_marker((2809.6, -1028.99, 951.405), (1, 0.549763, 0.549763), 202.588)
if "particle_154 geometry" not in marker_sets:
  s=new_marker_set('particle_154 geometry')
  marker_sets["particle_154 geometry"]=s
s= marker_sets["particle_154 geometry"]
mark=s.place_marker((2984.19, -787.418, 1307.86), (1, 0.540284, 0.540284), 221.463)
if "particle_155 geometry" not in marker_sets:
  s=new_marker_set('particle_155 geometry')
  marker_sets["particle_155 geometry"]=s
s= marker_sets["particle_155 geometry"]
mark=s.place_marker((2727.54, -523.615, 1471.59), (1, 0.8, 0), 134.639)
if "particle_156 geometry" not in marker_sets:
  s=new_marker_set('particle_156 geometry')
  marker_sets["particle_156 geometry"]=s
s= marker_sets["particle_156 geometry"]
mark=s.place_marker((3276.38, -131.897, 1559.35), (1, 0.521327, 0.521327), 219.727)
if "particle_157 geometry" not in marker_sets:
  s=new_marker_set('particle_157 geometry')
  marker_sets["particle_157 geometry"]=s
s= marker_sets["particle_157 geometry"]
mark=s.place_marker((3700.49, 244.218, 1654.79), (1, 0.511848, 0.511848), 185.536)
if "particle_158 geometry" not in marker_sets:
  s=new_marker_set('particle_158 geometry')
  marker_sets["particle_158 geometry"]=s
s= marker_sets["particle_158 geometry"]
mark=s.place_marker((3511.31, 630.383, 1930.33), (1, 0.50237, 0.50237), 191.263)
if "particle_159 geometry" not in marker_sets:
  s=new_marker_set('particle_159 geometry')
  marker_sets["particle_159 geometry"]=s
s= marker_sets["particle_159 geometry"]
mark=s.place_marker((3079.91, 876.091, 2032.06), (1, 0.492891, 0.492891), 162.496)
if "particle_160 geometry" not in marker_sets:
  s=new_marker_set('particle_160 geometry')
  marker_sets["particle_160 geometry"]=s
s= marker_sets["particle_160 geometry"]
mark=s.place_marker((2664.77, 909.361, 1881.29), (1, 0.483412, 0.483412), 202.935)
if "particle_161 geometry" not in marker_sets:
  s=new_marker_set('particle_161 geometry')
  marker_sets["particle_161 geometry"]=s
s= marker_sets["particle_161 geometry"]
mark=s.place_marker((2792.7, 1175.13, 1600.23), (1, 0.473934, 0.473934), 186.295)
if "particle_162 geometry" not in marker_sets:
  s=new_marker_set('particle_162 geometry')
  marker_sets["particle_162 geometry"]=s
s= marker_sets["particle_162 geometry"]
mark=s.place_marker((2953.17, 1544.11, 1705.29), (1, 0.464455, 0.464455), 153.297)
if "particle_163 geometry" not in marker_sets:
  s=new_marker_set('particle_163 geometry')
  marker_sets["particle_163 geometry"]=s
s= marker_sets["particle_163 geometry"]
mark=s.place_marker((3264.93, 1598.86, 1501.2), (1, 0.454976, 0.454976), 144.944)
if "particle_164 geometry" not in marker_sets:
  s=new_marker_set('particle_164 geometry')
  marker_sets["particle_164 geometry"]=s
s= marker_sets["particle_164 geometry"]
mark=s.place_marker((3643.36, 1795.71, 1499.35), (1, 0.445498, 0.445498), 165.489)
if "particle_165 geometry" not in marker_sets:
  s=new_marker_set('particle_165 geometry')
  marker_sets["particle_165 geometry"]=s
s= marker_sets["particle_165 geometry"]
mark=s.place_marker((3972.14, 1961.25, 1298), (1, 0.436019, 0.436019), 160.326)
if "particle_166 geometry" not in marker_sets:
  s=new_marker_set('particle_166 geometry')
  marker_sets["particle_166 geometry"]=s
s= marker_sets["particle_166 geometry"]
mark=s.place_marker((3476.83, 1798.48, 1407.87), (1, 0.42654, 0.42654), 168.006)
if "particle_167 geometry" not in marker_sets:
  s=new_marker_set('particle_167 geometry')
  marker_sets["particle_167 geometry"]=s
s= marker_sets["particle_167 geometry"]
mark=s.place_marker((3447.1, 1853.7, 1819.11), (1, 0.417062, 0.417062), 262.423)
if "particle_168 geometry" not in marker_sets:
  s=new_marker_set('particle_168 geometry')
  marker_sets["particle_168 geometry"]=s
s= marker_sets["particle_168 geometry"]
mark=s.place_marker((4008.31, 2043.63, 1728.44), (1, 0.407583, 0.407583), 32.2822)
if "particle_169 geometry" not in marker_sets:
  s=new_marker_set('particle_169 geometry')
  marker_sets["particle_169 geometry"]=s
s= marker_sets["particle_169 geometry"]
mark=s.place_marker((4165.25, 1800.39, 1439.49), (1, 0.398104, 0.398104), 230.943)
if "particle_170 geometry" not in marker_sets:
  s=new_marker_set('particle_170 geometry')
  marker_sets["particle_170 geometry"]=s
s= marker_sets["particle_170 geometry"]
mark=s.place_marker((3613.67, 1577.85, 1176.33), (1, 0.388626, 0.388626), 158.612)
if "particle_171 geometry" not in marker_sets:
  s=new_marker_set('particle_171 geometry')
  marker_sets["particle_171 geometry"]=s
s= marker_sets["particle_171 geometry"]
mark=s.place_marker((2984.36, 1487.36, 994.035), (1, 0.379147, 0.379147), 172.454)
if "particle_172 geometry" not in marker_sets:
  s=new_marker_set('particle_172 geometry')
  marker_sets["particle_172 geometry"]=s
s= marker_sets["particle_172 geometry"]
mark=s.place_marker((2455.49, 1464.95, 890.525), (1, 0.369668, 0.369668), 192.153)
if "particle_173 geometry" not in marker_sets:
  s=new_marker_set('particle_173 geometry')
  marker_sets["particle_173 geometry"]=s
s= marker_sets["particle_173 geometry"]
mark=s.place_marker((1938.12, 1484.51, 627.064), (1, 0.8, 0), 153.123)
if "particle_174 geometry" not in marker_sets:
  s=new_marker_set('particle_174 geometry')
  marker_sets["particle_174 geometry"]=s
s= marker_sets["particle_174 geometry"]
mark=s.place_marker((2604.92, 1862.5, 94.1542), (1, 0.350711, 0.350711), 164.079)
if "particle_175 geometry" not in marker_sets:
  s=new_marker_set('particle_175 geometry')
  marker_sets["particle_175 geometry"]=s
s= marker_sets["particle_175 geometry"]
mark=s.place_marker((3242.15, 2180.9, -12.2992), (1, 0.341232, 0.341232), 130.669)
if "particle_176 geometry" not in marker_sets:
  s=new_marker_set('particle_176 geometry')
  marker_sets["particle_176 geometry"]=s
s= marker_sets["particle_176 geometry"]
mark=s.place_marker((2810.43, 2104.1, 578.006), (1, 0.331754, 0.331754), 260.579)
if "particle_177 geometry" not in marker_sets:
  s=new_marker_set('particle_177 geometry')
  marker_sets["particle_177 geometry"]=s
s= marker_sets["particle_177 geometry"]
mark=s.place_marker((2276.24, 2163.68, 918.881), (1, 0.322275, 0.322275), 214.737)
if "particle_178 geometry" not in marker_sets:
  s=new_marker_set('particle_178 geometry')
  marker_sets["particle_178 geometry"]=s
s= marker_sets["particle_178 geometry"]
mark=s.place_marker((2467.67, 2325.19, 1394.84), (1, 0.312796, 0.312796), 284.617)
if "particle_179 geometry" not in marker_sets:
  s=new_marker_set('particle_179 geometry')
  marker_sets["particle_179 geometry"]=s
s= marker_sets["particle_179 geometry"]
mark=s.place_marker((3102.84, 2349.44, 1541.93), (1, 0.303318, 0.303318), 277.891)
if "particle_180 geometry" not in marker_sets:
  s=new_marker_set('particle_180 geometry')
  marker_sets["particle_180 geometry"]=s
s= marker_sets["particle_180 geometry"]
mark=s.place_marker((3482.23, 2663.66, 1376.85), (1, 0.293839, 0.293839), 132.318)
if "particle_181 geometry" not in marker_sets:
  s=new_marker_set('particle_181 geometry')
  marker_sets["particle_181 geometry"]=s
s= marker_sets["particle_181 geometry"]
mark=s.place_marker((3742.96, 2936.77, 1156.37), (1, 0.28436, 0.28436), 179.917)
if "particle_182 geometry" not in marker_sets:
  s=new_marker_set('particle_182 geometry')
  marker_sets["particle_182 geometry"]=s
s= marker_sets["particle_182 geometry"]
mark=s.place_marker((3899.1, 2757.32, 865.544), (1, 0.274882, 0.274882), 120.125)
if "particle_183 geometry" not in marker_sets:
  s=new_marker_set('particle_183 geometry')
  marker_sets["particle_183 geometry"]=s
s= marker_sets["particle_183 geometry"]
mark=s.place_marker((3407.26, 2578.63, 838.515), (1, 0.265403, 0.265403), 220.204)
if "particle_184 geometry" not in marker_sets:
  s=new_marker_set('particle_184 geometry')
  marker_sets["particle_184 geometry"]=s
s= marker_sets["particle_184 geometry"]
mark=s.place_marker((3033.93, 2659.44, 1172.79), (1, 0.255924, 0.255924), 218.035)
if "particle_185 geometry" not in marker_sets:
  s=new_marker_set('particle_185 geometry')
  marker_sets["particle_185 geometry"]=s
s= marker_sets["particle_185 geometry"]
mark=s.place_marker((2693.19, 2199.12, 1367.6), (1, 0.246445, 0.246445), 236.063)
if "particle_186 geometry" not in marker_sets:
  s=new_marker_set('particle_186 geometry')
  marker_sets["particle_186 geometry"]=s
s= marker_sets["particle_186 geometry"]
mark=s.place_marker((2961.46, 2051.53, 1718.45), (1, 0.236967, 0.236967), 157.853)
if "particle_187 geometry" not in marker_sets:
  s=new_marker_set('particle_187 geometry')
  marker_sets["particle_187 geometry"]=s
s= marker_sets["particle_187 geometry"]
mark=s.place_marker((3248.01, 2374.71, 2049.3), (1, 0.227488, 0.227488), 151.735)
if "particle_188 geometry" not in marker_sets:
  s=new_marker_set('particle_188 geometry')
  marker_sets["particle_188 geometry"]=s
s= marker_sets["particle_188 geometry"]
mark=s.place_marker((3399.85, 2166.21, 2065.09), (1, 0.218009, 0.218009), 132.101)
if "particle_189 geometry" not in marker_sets:
  s=new_marker_set('particle_189 geometry')
  marker_sets["particle_189 geometry"]=s
s= marker_sets["particle_189 geometry"]
mark=s.place_marker((3361.63, 2115.41, 1649.71), (1, 0.208531, 0.208531), 180.567)
if "particle_190 geometry" not in marker_sets:
  s=new_marker_set('particle_190 geometry')
  marker_sets["particle_190 geometry"]=s
s= marker_sets["particle_190 geometry"]
mark=s.place_marker((3449.18, 1891.19, 1064.67), (1, 0.199052, 0.199052), 231.073)
if "particle_191 geometry" not in marker_sets:
  s=new_marker_set('particle_191 geometry')
  marker_sets["particle_191 geometry"]=s
s= marker_sets["particle_191 geometry"]
mark=s.place_marker((3890.92, 1631.84, 749.908), (1, 0.189573, 0.189573), 173.473)
if "particle_192 geometry" not in marker_sets:
  s=new_marker_set('particle_192 geometry')
  marker_sets["particle_192 geometry"]=s
s= marker_sets["particle_192 geometry"]
mark=s.place_marker((3930.76, 1412.69, 1146.95), (1, 0.180095, 0.180095), 184.993)
if "particle_193 geometry" not in marker_sets:
  s=new_marker_set('particle_193 geometry')
  marker_sets["particle_193 geometry"]=s
s= marker_sets["particle_193 geometry"]
mark=s.place_marker((4234.1, 1490.88, 1064.2), (1, 0.170616, 0.170616), 147.396)
if "particle_194 geometry" not in marker_sets:
  s=new_marker_set('particle_194 geometry')
  marker_sets["particle_194 geometry"]=s
s= marker_sets["particle_194 geometry"]
mark=s.place_marker((4559.57, 1579.84, 699.549), (1, 0.161137, 0.161137), 236.172)
if "particle_195 geometry" not in marker_sets:
  s=new_marker_set('particle_195 geometry')
  marker_sets["particle_195 geometry"]=s
s= marker_sets["particle_195 geometry"]
mark=s.place_marker((4366.43, 1778.43, 334.217), (1, 0.151659, 0.151659), 146.788)
if "particle_196 geometry" not in marker_sets:
  s=new_marker_set('particle_196 geometry')
  marker_sets["particle_196 geometry"]=s
s= marker_sets["particle_196 geometry"]
mark=s.place_marker((3870.61, 1752.19, 328.305), (1, 0.14218, 0.14218), 257.758)
if "particle_197 geometry" not in marker_sets:
  s=new_marker_set('particle_197 geometry')
  marker_sets["particle_197 geometry"]=s
s= marker_sets["particle_197 geometry"]
mark=s.place_marker((3852.36, 2086.24, 901.176), (1, 0.132701, 0.132701), 215.822)
if "particle_198 geometry" not in marker_sets:
  s=new_marker_set('particle_198 geometry')
  marker_sets["particle_198 geometry"]=s
s= marker_sets["particle_198 geometry"]
mark=s.place_marker((3811.89, 2560.11, 1392.3), (1, 0.123223, 0.123223), 215.583)
if "particle_199 geometry" not in marker_sets:
  s=new_marker_set('particle_199 geometry')
  marker_sets["particle_199 geometry"]=s
s= marker_sets["particle_199 geometry"]
mark=s.place_marker((3647.35, 2935.87, 1467.8), (1, 0.113744, 0.113744), 136.961)
if "particle_200 geometry" not in marker_sets:
  s=new_marker_set('particle_200 geometry')
  marker_sets["particle_200 geometry"]=s
s= marker_sets["particle_200 geometry"]
mark=s.place_marker((3680.83, 2595.22, 1132.41), (1, 0.104265, 0.104265), 180.134)
if "particle_201 geometry" not in marker_sets:
  s=new_marker_set('particle_201 geometry')
  marker_sets["particle_201 geometry"]=s
s= marker_sets["particle_201 geometry"]
mark=s.place_marker((3776.21, 2188.49, 652.811), (1, 0.0947867, 0.0947867), 256.869)
if "particle_202 geometry" not in marker_sets:
  s=new_marker_set('particle_202 geometry')
  marker_sets["particle_202 geometry"]=s
s= marker_sets["particle_202 geometry"]
mark=s.place_marker((3721.68, 1747.05, 127.59), (1, 0.0853081, 0.0853081), 255.155)
if "particle_203 geometry" not in marker_sets:
  s=new_marker_set('particle_203 geometry')
  marker_sets["particle_203 geometry"]=s
s= marker_sets["particle_203 geometry"]
mark=s.place_marker((4083.3, 1436.45, 437.675), (1, 0.0758294, 0.0758294), 245.869)
if "particle_204 geometry" not in marker_sets:
  s=new_marker_set('particle_204 geometry')
  marker_sets["particle_204 geometry"]=s
s= marker_sets["particle_204 geometry"]
mark=s.place_marker((4332.16, 1472.37, 906.719), (1, 0.0663507, 0.0663507), 188.248)
if "particle_205 geometry" not in marker_sets:
  s=new_marker_set('particle_205 geometry')
  marker_sets["particle_205 geometry"]=s
s= marker_sets["particle_205 geometry"]
mark=s.place_marker((4476.46, 1770.2, 1036.44), (1, 0.056872, 0.056872), 140.258)
if "particle_206 geometry" not in marker_sets:
  s=new_marker_set('particle_206 geometry')
  marker_sets["particle_206 geometry"]=s
s= marker_sets["particle_206 geometry"]
mark=s.place_marker((4143.73, 1853.16, 714.261), (1, 0.0473934, 0.0473934), 254.092)
if "particle_207 geometry" not in marker_sets:
  s=new_marker_set('particle_207 geometry')
  marker_sets["particle_207 geometry"]=s
s= marker_sets["particle_207 geometry"]
mark=s.place_marker((3797.47, 2093.72, 487.282), (1, 0.0379147, 0.0379147), 135.203)
if "particle_208 geometry" not in marker_sets:
  s=new_marker_set('particle_208 geometry')
  marker_sets["particle_208 geometry"]=s
s= marker_sets["particle_208 geometry"]
mark=s.place_marker((4042.15, 2435.47, 653.626), (1, 0.028436, 0.028436), 198.835)
if "particle_209 geometry" not in marker_sets:
  s=new_marker_set('particle_209 geometry')
  marker_sets["particle_209 geometry"]=s
s= marker_sets["particle_209 geometry"]
mark=s.place_marker((4066.78, 2310.65, 1131.43), (1, 0.0189573, 0.0189573), 231.095)
if "particle_210 geometry" not in marker_sets:
  s=new_marker_set('particle_210 geometry')
  marker_sets["particle_210 geometry"]=s
s= marker_sets["particle_210 geometry"]
mark=s.place_marker((4424.81, 2037.85, 1385.07), (1, 0.00947867, 0.00947867), 251.206)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
