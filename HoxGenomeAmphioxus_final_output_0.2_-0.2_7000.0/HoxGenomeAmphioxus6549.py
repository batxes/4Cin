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
mark=s.place_marker((6458.26, 469.212, -106.472), (0, 0, 1), 201.612)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((5960.5, 350.102, 23.8251), (0.00947867, 0.00947867, 1), 254.309)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((5585.6, 222.774, -242.366), (0.0189573, 0.0189573, 1), 183.366)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((5170.25, 161.592, -458.653), (0.028436, 0.028436, 1), 225.888)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((4700.07, 178.929, -764.743), (0.0379147, 0.0379147, 1), 222.634)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((4676.59, -13.7439, -1227.27), (0.0473934, 0.0473934, 1), 191.111)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((5156.72, -27.7049, -1506.68), (0.056872, 0.056872, 1), 109.473)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((5473.4, 113.136, -1924.99), (0.0663507, 0.0663507, 1), 208.923)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((5436.88, 350.251, -2272.09), (0.0758294, 0.0758294, 1), 122.729)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((5258.99, 682.889, -2240.58), (0.0853081, 0.0853081, 1), 153.948)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((5077.59, 1067.85, -2126.05), (0.0947867, 0.0947867, 1), 178.073)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((4597.66, 1051.46, -1803.7), (0.104265, 0.104265, 1), 202.935)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((4205.87, 1177.55, -1695.28), (0.113744, 0.113744, 1), 120.017)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((3959.75, 1185.4, -1845.37), (0.123223, 0.123223, 1), 131.233)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((4511.69, 1169.15, -2127.67), (0.132701, 0.132701, 1), 193.91)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((4926.83, 1363.03, -2451.85), (0.14218, 0.14218, 1), 103.745)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((4869.42, 1673.9, -2670.28), (0.151659, 0.151659, 1), 145.986)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((4044.46, 1580.89, -2138.65), (0.161137, 0.161137, 1), 229.143)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((2989.88, 1454.51, -1557.87), (1, 0.8, 0), 171.629)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((3551.06, 1573.15, -1795.08), (0.180095, 0.180095, 1), 138.566)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((3844.9, 1453.85, -1550.43), (0.189573, 0.189573, 1), 144.337)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((3676.01, 1154.38, -1286.04), (0.199052, 0.199052, 1), 253.072)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((3722.59, 745.891, -1481.25), (0.208531, 0.208531, 1), 195.906)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((4006.25, 621.513, -1800.07), (0.218009, 0.218009, 1), 169.416)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((4185.14, 688.797, -2306.61), (0.227488, 0.227488, 1), 310.152)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((3665.93, 770.647, -2605.42), (0.236967, 0.236967, 1), 191.892)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((3739.76, 712.505, -3064.36), (0.246445, 0.246445, 1), 112.163)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((3868.04, 433.835, -3119.34), (0.255924, 0.255924, 1), 197.728)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((3688.22, 49.7987, -3279.27), (0.265403, 0.265403, 1), 221.007)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((3611.67, -361.434, -3055.77), (0.274882, 0.274882, 1), 209.118)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((3408.41, -580.102, -2563.56), (0.28436, 0.28436, 1), 226.517)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((3554.99, -1068.16, -2461.39), (0.293839, 0.293839, 1), 140.171)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((3943.23, -1537.7, -2607.71), (0.303318, 0.303318, 1), 241.509)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((4339.24, -1903.78, -2376.87), (0.312796, 0.312796, 1), 194.582)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((4456.56, -1657.93, -2100.65), (0.322275, 0.322275, 1), 149.934)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((3992.25, -1470.73, -2024.66), (0.331754, 0.331754, 1), 197.967)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((3915.64, -1825.08, -2042.63), (0.341232, 0.341232, 1), 120.277)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((3587.84, -1948.42, -1729.44), (0.350711, 0.350711, 1), 149.522)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((3485.12, -2070.68, -1405.84), (0.36019, 0.36019, 1), 160.803)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((4073.57, -2016.7, -1575.72), (0.369668, 0.369668, 1), 149.869)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((4334.65, -1678.33, -1717.77), (0.379147, 0.379147, 1), 181.37)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((3906.31, -1840.38, -1593.88), (0.388626, 0.388626, 1), 229.511)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((3603.69, -2428.71, -1426.32), (0.398104, 0.398104, 1), 264.093)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((3408.74, -2846.06, -1350.17), (0.407583, 0.407583, 1), 177.617)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((3185.68, -2426.71, -1455.78), (0.417062, 0.417062, 1), 167.16)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((2954.99, -2465.75, -1906.51), (0.42654, 0.42654, 1), 142.536)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((2724.91, -2649.54, -2349.46), (0.436019, 0.436019, 1), 189.571)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((2141.42, -2801.42, -2386.78), (0.445498, 0.445498, 1), 222.244)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((1808.37, -2704.17, -2667.77), (0.454976, 0.454976, 1), 137.438)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((1649.31, -2252.32, -2828.3), (0.464455, 0.464455, 1), 225.953)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((1759.35, -2048.04, -3319.61), (0.473934, 0.473934, 1), 202.545)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((1951.23, -1685.19, -3275.1), (0.483412, 0.483412, 1), 160.955)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((1674.11, -1460.89, -2930.7), (0.492891, 0.492891, 1), 146.767)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((1295.64, -1073.16, -2489), (0.50237, 0.50237, 1), 169.351)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((1218.21, -619.494, -2313.26), (0.511848, 0.511848, 1), 186.968)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((898.091, -221.813, -2071.59), (0.521327, 0.521327, 1), 217.883)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((507.594, 154.27, -1792.24), (0.530806, 0.530806, 1), 238.667)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((232.202, 531.083, -1824.51), (0.540284, 0.540284, 1), 157.94)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((248.726, 701.032, -2235.84), (0.549763, 0.549763, 1), 182.477)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((235.852, 676.402, -1696.81), (0.559242, 0.559242, 1), 341.892)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((-170.552, 913.419, -2226.55), (0.56872, 0.56872, 1), 245.002)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((-521.522, 840.634, -2603.79), (0.578199, 0.578199, 1), 147.786)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((-463.478, 467.472, -2400.88), (0.587678, 0.587678, 1), 157.354)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((-476.328, 72.4919, -2028.73), (0.597156, 0.597156, 1), 278.238)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((-913.275, -188.771, -1870.03), (0.606635, 0.606635, 1), 211.136)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((-1253.22, -373.442, -2335.07), (1, 0.8, 0), 195.667)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((-1022.72, 106.226, -1783.6), (0.625592, 0.625592, 1), 206.797)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((-890.337, 457.745, -1313.52), (0.635071, 0.635071, 1), 192.153)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((-1007.48, 752.059, -903.623), (0.64455, 0.64455, 1), 211.505)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((-1489.87, 954.275, -840.299), (0.654028, 0.654028, 1), 199.29)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((-2185.67, 1174.25, -942.342), (0.663507, 0.663507, 1), 201.937)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((-2756.79, 1130.49, -1051.7), (0.672986, 0.672986, 1), 115.895)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((-2430.18, 771.95, -845.842), (0.682464, 0.682464, 1), 162.756)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((-2275.47, 399.648, -769.301), (0.691943, 0.691943, 1), 172.996)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((-2188.55, 6.32448, -550.105), (0.701422, 0.701422, 1), 270.103)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((-1985.72, -447.557, -664.634), (0.7109, 0.7109, 1), 231.551)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((-1316.65, -491.947, -894.049), (1, 0.8, 0), 193.867)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((-928.26, -15.4197, -805.182), (0.729858, 0.729858, 1), 148.047)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((-613.72, 179.504, -740.793), (0.739336, 0.739336, 1), 219.553)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((-1095.2, 253.429, -836.702), (0.748815, 0.748815, 1), 263.79)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((-364.037, 233.931, -945.426), (0.758294, 0.758294, 1), 165.967)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((104.835, -36.0145, -917.689), (0.767773, 0.767773, 1), 208.706)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((46.4771, -446.012, -1051.81), (0.777251, 0.777251, 1), 120.928)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((-193.188, -724.102, -997.353), (0.78673, 0.78673, 1), 243.765)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((-416.919, -717.009, -680.348), (0.796209, 0.796209, 1), 206.558)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((-819.826, -1082.78, -801.022), (1, 0.3, 0), 187.488)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((-183.515, -673.061, -692.712), (0.815166, 0.815166, 1), 227.45)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((-276.33, -405.264, -210.966), (0.824645, 0.824645, 1), 288.522)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((77.5338, -60.7155, -325.632), (0.834123, 0.834123, 1), 208.554)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((-42.0474, -480.384, -201.408), (0.843602, 0.843602, 1), 212.524)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((272.323, -827.065, -384.808), (0.853081, 0.853081, 1), 251.51)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((482.634, -1320.1, -446.773), (0.862559, 0.862559, 1), 216.364)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((59.0699, -1194.86, -109.884), (0.872038, 0.872038, 1), 241.661)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((-153.005, -1236.1, 22.3925), (0.881517, 0.881517, 1), 243.613)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((-324.912, -1672.71, 245.125), (0.890995, 0.890995, 1), 259.581)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((-674.933, -1752.06, 230.18), (0.900474, 0.900474, 1), 174.081)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((-681.016, -1365.3, 320.369), (1, 0.3, 0), 132.665)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((-912.265, -1884.74, 313.999), (1, 0.3, 0), 201.612)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((-1031.02, -1764.1, 730.063), (0.92891, 0.92891, 1), 160.109)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((-1038.29, -1357.15, 735.94), (0.938389, 0.938389, 1), 155.119)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((-1158.77, -1000.29, 903.205), (0.947867, 0.947867, 1), 239.187)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((-1510.41, -932.55, 869.973), (0.957346, 0.957346, 1), 121.145)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((-1265.27, -1231.51, 468.096), (1, 0.3, 0), 228.513)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((-1008.45, -616.288, 670.515), (0.976303, 0.976303, 1), 147.7)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((-1020.17, -669.995, 1078.28), (0.985782, 0.985782, 1), 217.948)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((-690.189, -598.438, 711.009), (1, 0.3, 0), 190.374)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((-609.071, -94.1988, 423.344), (1, 0.995261, 0.995261), 245.088)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((-992.038, 128.816, 694.913), (1, 0.985782, 0.985782), 175.534)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((-1277.5, 186.375, 1061.46), (1, 0.976303, 0.976303), 215.41)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((-1248.27, -104.584, 1492.55), (1, 0.966825, 0.966825), 253.463)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((-1443.17, -487.283, 1829.45), (1, 0.957346, 0.957346), 256.739)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((-1300.72, -654.768, 1668.03), (1, 0.947867, 0.947867), 151.236)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((-958.513, -405.122, 1497.56), (1, 0.938389, 0.938389), 197.75)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((-410.121, -178.319, 1186.36), (1, 0.92891, 0.92891), 280.994)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((-493.154, -96.5107, 1564.34), (1, 0.919431, 0.919431), 265.026)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((-788.143, -560.484, 1765.34), (1, 0.909953, 0.909953), 210.984)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((-381.472, -358.199, 1682.65), (1, 0.900474, 0.900474), 193.91)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((12.1798, -302.913, 1392.8), (1, 0.890995, 0.890995), 250.664)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((317.624, -494.099, 1081.29), (1, 0.881517, 0.881517), 203.716)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((186.949, -723.735, 1664.04), (1, 0.3, 0), 277.501)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((102.298, -1114.78, 1557.49), (1, 0.862559, 0.862559), 198.791)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((576.14, -1116.56, 1380.58), (1, 0.3, 0), 162.647)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((-173.907, -1208.85, 1520.24), (1, 0.843602, 0.843602), 291.624)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((-753.593, -1107, 1795.45), (1, 0.834123, 0.834123), 174.471)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((-1064.42, -767.012, 1884.75), (1, 0.824645, 0.824645), 218.1)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((-815.821, -305.858, 1917.45), (1, 0.815166, 0.815166), 260.101)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((-965.083, 43.2678, 2259.9), (1, 0.805687, 0.805687), 184.69)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((-1055.04, 146.809, 2589.95), (1, 0.796209, 0.796209), 134.791)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((-1067.19, -127.415, 2199.29), (1, 0.78673, 0.78673), 256.348)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((-853.324, -570.923, 2170.5), (1, 0.777251, 0.777251), 165.229)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((-527.928, -839.482, 2324.06), (1, 0.767773, 0.767773), 223.111)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((-197.516, -1006.38, 2593.66), (1, 0.758294, 0.758294), 163.428)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((-90.1351, -1242.74, 2997.67), (1, 0.748815, 0.748815), 182.346)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((104.833, -1366.72, 2805.49), (1, 0.739336, 0.739336), 148.784)
if "particle_134 geometry" not in marker_sets:
  s=new_marker_set('particle_134 geometry')
  marker_sets["particle_134 geometry"]=s
s= marker_sets["particle_134 geometry"]
mark=s.place_marker((4.89402, -1214.32, 2432.12), (1, 0.729858, 0.729858), 239.318)
if "particle_135 geometry" not in marker_sets:
  s=new_marker_set('particle_135 geometry')
  marker_sets["particle_135 geometry"]=s
s= marker_sets["particle_135 geometry"]
mark=s.place_marker((367.418, -1397.53, 2547.13), (1, 0.3, 0), 146.268)
if "particle_136 geometry" not in marker_sets:
  s=new_marker_set('particle_136 geometry')
  marker_sets["particle_136 geometry"]=s
s= marker_sets["particle_136 geometry"]
mark=s.place_marker((142.696, -1249.88, 2927.86), (1, 0.7109, 0.7109), 187.163)
if "particle_137 geometry" not in marker_sets:
  s=new_marker_set('particle_137 geometry')
  marker_sets["particle_137 geometry"]=s
s= marker_sets["particle_137 geometry"]
mark=s.place_marker((304.944, -1240.06, 3526.17), (1, 0.701422, 0.701422), 174.059)
if "particle_138 geometry" not in marker_sets:
  s=new_marker_set('particle_138 geometry')
  marker_sets["particle_138 geometry"]=s
s= marker_sets["particle_138 geometry"]
mark=s.place_marker((574.578, -1265.46, 4141.62), (1, 0.691943, 0.691943), 155.032)
if "particle_139 geometry" not in marker_sets:
  s=new_marker_set('particle_139 geometry')
  marker_sets["particle_139 geometry"]=s
s= marker_sets["particle_139 geometry"]
mark=s.place_marker((780.918, -1188.86, 4442.64), (1, 0.682464, 0.682464), 71.4199)
if "particle_140 geometry" not in marker_sets:
  s=new_marker_set('particle_140 geometry')
  marker_sets["particle_140 geometry"]=s
s= marker_sets["particle_140 geometry"]
mark=s.place_marker((877.508, -829.542, 4062.08), (1, 0.672986, 0.672986), 364.085)
if "particle_141 geometry" not in marker_sets:
  s=new_marker_set('particle_141 geometry')
  marker_sets["particle_141 geometry"]=s
s= marker_sets["particle_141 geometry"]
mark=s.place_marker((937.722, -403.704, 3398.6), (1, 0.663507, 0.663507), 155.9)
if "particle_142 geometry" not in marker_sets:
  s=new_marker_set('particle_142 geometry')
  marker_sets["particle_142 geometry"]=s
s= marker_sets["particle_142 geometry"]
mark=s.place_marker((1192.37, 65.8165, 3189.61), (1, 0.654028, 0.654028), 206.992)
if "particle_143 geometry" not in marker_sets:
  s=new_marker_set('particle_143 geometry')
  marker_sets["particle_143 geometry"]=s
s= marker_sets["particle_143 geometry"]
mark=s.place_marker((1572.44, 401.552, 3016.04), (1, 0.64455, 0.64455), 148.459)
if "particle_144 geometry" not in marker_sets:
  s=new_marker_set('particle_144 geometry')
  marker_sets["particle_144 geometry"]=s
s= marker_sets["particle_144 geometry"]
mark=s.place_marker((1438.48, 543.981, 2554.54), (1, 0.635071, 0.635071), 221.224)
if "particle_145 geometry" not in marker_sets:
  s=new_marker_set('particle_145 geometry')
  marker_sets["particle_145 geometry"]=s
s= marker_sets["particle_145 geometry"]
mark=s.place_marker((1358.58, 774.117, 2101.61), (1, 0.625592, 0.625592), 206.124)
if "particle_146 geometry" not in marker_sets:
  s=new_marker_set('particle_146 geometry')
  marker_sets["particle_146 geometry"]=s
s= marker_sets["particle_146 geometry"]
mark=s.place_marker((1288.44, 633.163, 1667.16), (1, 0.616114, 0.616114), 151.388)
if "particle_147 geometry" not in marker_sets:
  s=new_marker_set('particle_147 geometry')
  marker_sets["particle_147 geometry"]=s
s= marker_sets["particle_147 geometry"]
mark=s.place_marker((1323.96, 278.528, 2170.68), (1, 0.8, 0), 177.378)
if "particle_148 geometry" not in marker_sets:
  s=new_marker_set('particle_148 geometry')
  marker_sets["particle_148 geometry"]=s
s= marker_sets["particle_148 geometry"]
mark=s.place_marker((1299.78, 732.528, 2806.45), (1, 0.597156, 0.597156), 191.458)
if "particle_149 geometry" not in marker_sets:
  s=new_marker_set('particle_149 geometry')
  marker_sets["particle_149 geometry"]=s
s= marker_sets["particle_149 geometry"]
mark=s.place_marker((1418.78, 1029.89, 3650.21), (1, 0.587678, 0.587678), 249.579)
if "particle_150 geometry" not in marker_sets:
  s=new_marker_set('particle_150 geometry')
  marker_sets["particle_150 geometry"]=s
s= marker_sets["particle_150 geometry"]
mark=s.place_marker((1615.3, 1355.92, 4551.03), (1, 0.578199, 0.578199), 151.735)
if "particle_151 geometry" not in marker_sets:
  s=new_marker_set('particle_151 geometry')
  marker_sets["particle_151 geometry"]=s
s= marker_sets["particle_151 geometry"]
mark=s.place_marker((1319.03, 956.85, 4344.53), (1, 0.56872, 0.56872), 124.573)
if "particle_152 geometry" not in marker_sets:
  s=new_marker_set('particle_152 geometry')
  marker_sets["particle_152 geometry"]=s
s= marker_sets["particle_152 geometry"]
mark=s.place_marker((973.587, 758.292, 3674.21), (1, 0.559242, 0.559242), 184.342)
if "particle_153 geometry" not in marker_sets:
  s=new_marker_set('particle_153 geometry')
  marker_sets["particle_153 geometry"]=s
s= marker_sets["particle_153 geometry"]
mark=s.place_marker((643.863, 677.054, 3272.64), (1, 0.549763, 0.549763), 202.588)
if "particle_154 geometry" not in marker_sets:
  s=new_marker_set('particle_154 geometry')
  marker_sets["particle_154 geometry"]=s
s= marker_sets["particle_154 geometry"]
mark=s.place_marker((185.67, 765.086, 3333.28), (1, 0.540284, 0.540284), 221.463)
if "particle_155 geometry" not in marker_sets:
  s=new_marker_set('particle_155 geometry')
  marker_sets["particle_155 geometry"]=s
s= marker_sets["particle_155 geometry"]
mark=s.place_marker((-42.7926, 689.553, 2994.89), (1, 0.8, 0), 134.639)
if "particle_156 geometry" not in marker_sets:
  s=new_marker_set('particle_156 geometry')
  marker_sets["particle_156 geometry"]=s
s= marker_sets["particle_156 geometry"]
mark=s.place_marker((-396.547, 1210.61, 3267.96), (1, 0.521327, 0.521327), 219.727)
if "particle_157 geometry" not in marker_sets:
  s=new_marker_set('particle_157 geometry')
  marker_sets["particle_157 geometry"]=s
s= marker_sets["particle_157 geometry"]
mark=s.place_marker((-755.184, 1642.58, 3434.55), (1, 0.511848, 0.511848), 185.536)
if "particle_158 geometry" not in marker_sets:
  s=new_marker_set('particle_158 geometry')
  marker_sets["particle_158 geometry"]=s
s= marker_sets["particle_158 geometry"]
mark=s.place_marker((-1183.44, 1617.39, 3146.77), (1, 0.50237, 0.50237), 191.263)
if "particle_159 geometry" not in marker_sets:
  s=new_marker_set('particle_159 geometry')
  marker_sets["particle_159 geometry"]=s
s= marker_sets["particle_159 geometry"]
mark=s.place_marker((-1358.63, 1453.12, 2695.17), (1, 0.492891, 0.492891), 162.496)
if "particle_160 geometry" not in marker_sets:
  s=new_marker_set('particle_160 geometry')
  marker_sets["particle_160 geometry"]=s
s= marker_sets["particle_160 geometry"]
mark=s.place_marker((-1209.55, 1296.91, 2309.57), (1, 0.483412, 0.483412), 202.935)
if "particle_161 geometry" not in marker_sets:
  s=new_marker_set('particle_161 geometry')
  marker_sets["particle_161 geometry"]=s
s= marker_sets["particle_161 geometry"]
mark=s.place_marker((-1182.83, 1675.84, 2163.86), (1, 0.473934, 0.473934), 186.295)
if "particle_162 geometry" not in marker_sets:
  s=new_marker_set('particle_162 geometry')
  marker_sets["particle_162 geometry"]=s
s= marker_sets["particle_162 geometry"]
mark=s.place_marker((-1512.47, 1920.19, 2090.13), (1, 0.464455, 0.464455), 153.297)
if "particle_163 geometry" not in marker_sets:
  s=new_marker_set('particle_163 geometry')
  marker_sets["particle_163 geometry"]=s
s= marker_sets["particle_163 geometry"]
mark=s.place_marker((-1456.86, 2254.27, 2231.85), (1, 0.454976, 0.454976), 144.944)
if "particle_164 geometry" not in marker_sets:
  s=new_marker_set('particle_164 geometry')
  marker_sets["particle_164 geometry"]=s
s= marker_sets["particle_164 geometry"]
mark=s.place_marker((-1713.38, 2570.78, 2359.4), (1, 0.445498, 0.445498), 165.489)
if "particle_165 geometry" not in marker_sets:
  s=new_marker_set('particle_165 geometry')
  marker_sets["particle_165 geometry"]=s
s= marker_sets["particle_165 geometry"]
mark=s.place_marker((-1896.26, 2946.01, 2401), (1, 0.436019, 0.436019), 160.326)
if "particle_166 geometry" not in marker_sets:
  s=new_marker_set('particle_166 geometry')
  marker_sets["particle_166 geometry"]=s
s= marker_sets["particle_166 geometry"]
mark=s.place_marker((-1755.58, 2504.34, 2150.32), (1, 0.42654, 0.42654), 168.006)
if "particle_167 geometry" not in marker_sets:
  s=new_marker_set('particle_167 geometry')
  marker_sets["particle_167 geometry"]=s
s= marker_sets["particle_167 geometry"]
mark=s.place_marker((-1901.51, 2320.73, 2310.39), (1, 0.417062, 0.417062), 262.423)
if "particle_168 geometry" not in marker_sets:
  s=new_marker_set('particle_168 geometry')
  marker_sets["particle_168 geometry"]=s
s= marker_sets["particle_168 geometry"]
mark=s.place_marker((-1998.14, 2819.87, 2615.97), (1, 0.407583, 0.407583), 32.2822)
if "particle_169 geometry" not in marker_sets:
  s=new_marker_set('particle_169 geometry')
  marker_sets["particle_169 geometry"]=s
s= marker_sets["particle_169 geometry"]
mark=s.place_marker((-1642.31, 2964.56, 2804.4), (1, 0.398104, 0.398104), 230.943)
if "particle_170 geometry" not in marker_sets:
  s=new_marker_set('particle_170 geometry')
  marker_sets["particle_170 geometry"]=s
s= marker_sets["particle_170 geometry"]
mark=s.place_marker((-1207.39, 2632.21, 2450.76), (1, 0.388626, 0.388626), 158.612)
if "particle_171 geometry" not in marker_sets:
  s=new_marker_set('particle_171 geometry')
  marker_sets["particle_171 geometry"]=s
s= marker_sets["particle_171 geometry"]
mark=s.place_marker((-908.191, 2278.32, 1974.32), (1, 0.379147, 0.379147), 172.454)
if "particle_172 geometry" not in marker_sets:
  s=new_marker_set('particle_172 geometry')
  marker_sets["particle_172 geometry"]=s
s= marker_sets["particle_172 geometry"]
mark=s.place_marker((-734.015, 1978.47, 1555.01), (1, 0.369668, 0.369668), 192.153)
if "particle_173 geometry" not in marker_sets:
  s=new_marker_set('particle_173 geometry')
  marker_sets["particle_173 geometry"]=s
s= marker_sets["particle_173 geometry"]
mark=s.place_marker((-445.519, 1791.9, 1086.08), (1, 0.8, 0), 153.123)
if "particle_174 geometry" not in marker_sets:
  s=new_marker_set('particle_174 geometry')
  marker_sets["particle_174 geometry"]=s
s= marker_sets["particle_174 geometry"]
mark=s.place_marker((-320.581, 2735.48, 1251.83), (1, 0.350711, 0.350711), 164.079)
if "particle_175 geometry" not in marker_sets:
  s=new_marker_set('particle_175 geometry')
  marker_sets["particle_175 geometry"]=s
s= marker_sets["particle_175 geometry"]
mark=s.place_marker((-496.013, 3398.38, 1537.2), (1, 0.341232, 0.341232), 130.669)
if "particle_176 geometry" not in marker_sets:
  s=new_marker_set('particle_176 geometry')
  marker_sets["particle_176 geometry"]=s
s= marker_sets["particle_176 geometry"]
mark=s.place_marker((-853.55, 2783.33, 1401.37), (1, 0.331754, 0.331754), 260.579)
if "particle_177 geometry" not in marker_sets:
  s=new_marker_set('particle_177 geometry')
  marker_sets["particle_177 geometry"]=s
s= marker_sets["particle_177 geometry"]
mark=s.place_marker((-1066.6, 2318.05, 1035.32), (1, 0.322275, 0.322275), 214.737)
if "particle_178 geometry" not in marker_sets:
  s=new_marker_set('particle_178 geometry')
  marker_sets["particle_178 geometry"]=s
s= marker_sets["particle_178 geometry"]
mark=s.place_marker((-1578.94, 2269.23, 1202.47), (1, 0.312796, 0.312796), 284.617)
if "particle_179 geometry" not in marker_sets:
  s=new_marker_set('particle_179 geometry')
  marker_sets["particle_179 geometry"]=s
s= marker_sets["particle_179 geometry"]
mark=s.place_marker((-1835.05, 2578.68, 1710.47), (1, 0.303318, 0.303318), 277.891)
if "particle_180 geometry" not in marker_sets:
  s=new_marker_set('particle_180 geometry')
  marker_sets["particle_180 geometry"]=s
s= marker_sets["particle_180 geometry"]
mark=s.place_marker((-1934.86, 3079.88, 1800.77), (1, 0.293839, 0.293839), 132.318)
if "particle_181 geometry" not in marker_sets:
  s=new_marker_set('particle_181 geometry')
  marker_sets["particle_181 geometry"]=s
s= marker_sets["particle_181 geometry"]
mark=s.place_marker((-1944.94, 3511.04, 1789.09), (1, 0.28436, 0.28436), 179.917)
if "particle_182 geometry" not in marker_sets:
  s=new_marker_set('particle_182 geometry')
  marker_sets["particle_182 geometry"]=s
s= marker_sets["particle_182 geometry"]
mark=s.place_marker((-1627.91, 3683.39, 1944.8), (1, 0.274882, 0.274882), 120.125)
if "particle_183 geometry" not in marker_sets:
  s=new_marker_set('particle_183 geometry')
  marker_sets["particle_183 geometry"]=s
s= marker_sets["particle_183 geometry"]
mark=s.place_marker((-1408.34, 3308.92, 1648.64), (1, 0.265403, 0.265403), 220.204)
if "particle_184 geometry" not in marker_sets:
  s=new_marker_set('particle_184 geometry')
  marker_sets["particle_184 geometry"]=s
s= marker_sets["particle_184 geometry"]
mark=s.place_marker((-1653.35, 2974.71, 1361.6), (1, 0.255924, 0.255924), 218.035)
if "particle_185 geometry" not in marker_sets:
  s=new_marker_set('particle_185 geometry')
  marker_sets["particle_185 geometry"]=s
s= marker_sets["particle_185 geometry"]
mark=s.place_marker((-1489.07, 2401.71, 1416.37), (1, 0.246445, 0.246445), 236.063)
if "particle_186 geometry" not in marker_sets:
  s=new_marker_set('particle_186 geometry')
  marker_sets["particle_186 geometry"]=s
s= marker_sets["particle_186 geometry"]
mark=s.place_marker((-1714, 2332.27, 1820.45), (1, 0.236967, 0.236967), 157.853)
if "particle_187 geometry" not in marker_sets:
  s=new_marker_set('particle_187 geometry')
  marker_sets["particle_187 geometry"]=s
s= marker_sets["particle_187 geometry"]
mark=s.place_marker((-2193.44, 2566.36, 1950.65), (1, 0.227488, 0.227488), 151.735)
if "particle_188 geometry" not in marker_sets:
  s=new_marker_set('particle_188 geometry')
  marker_sets["particle_188 geometry"]=s
s= marker_sets["particle_188 geometry"]
mark=s.place_marker((-2145.06, 2525.43, 2191.23), (1, 0.218009, 0.218009), 132.101)
if "particle_189 geometry" not in marker_sets:
  s=new_marker_set('particle_189 geometry')
  marker_sets["particle_189 geometry"]=s
s= marker_sets["particle_189 geometry"]
mark=s.place_marker((-1775.66, 2667.98, 2064.75), (1, 0.208531, 0.208531), 180.567)
if "particle_190 geometry" not in marker_sets:
  s=new_marker_set('particle_190 geometry')
  marker_sets["particle_190 geometry"]=s
s= marker_sets["particle_190 geometry"]
mark=s.place_marker((-1189.66, 2864.6, 2102.23), (1, 0.199052, 0.199052), 231.073)
if "particle_191 geometry" not in marker_sets:
  s=new_marker_set('particle_191 geometry')
  marker_sets["particle_191 geometry"]=s
s= marker_sets["particle_191 geometry"]
mark=s.place_marker((-872.214, 3144.91, 2510.19), (1, 0.189573, 0.189573), 173.473)
if "particle_192 geometry" not in marker_sets:
  s=new_marker_set('particle_192 geometry')
  marker_sets["particle_192 geometry"]=s
s= marker_sets["particle_192 geometry"]
mark=s.place_marker((-1079.21, 2819.82, 2763.07), (1, 0.180095, 0.180095), 184.993)
if "particle_193 geometry" not in marker_sets:
  s=new_marker_set('particle_193 geometry')
  marker_sets["particle_193 geometry"]=s
s= marker_sets["particle_193 geometry"]
mark=s.place_marker((-1176.51, 3082.76, 2924.51), (1, 0.170616, 0.170616), 147.396)
if "particle_194 geometry" not in marker_sets:
  s=new_marker_set('particle_194 geometry')
  marker_sets["particle_194 geometry"]=s
s= marker_sets["particle_194 geometry"]
mark=s.place_marker((-979.789, 3529.28, 3021.17), (1, 0.161137, 0.161137), 236.172)
if "particle_195 geometry" not in marker_sets:
  s=new_marker_set('particle_195 geometry')
  marker_sets["particle_195 geometry"]=s
s= marker_sets["particle_195 geometry"]
mark=s.place_marker((-779.943, 3726.19, 2650.57), (1, 0.151659, 0.151659), 146.788)
if "particle_196 geometry" not in marker_sets:
  s=new_marker_set('particle_196 geometry')
  marker_sets["particle_196 geometry"]=s
s= marker_sets["particle_196 geometry"]
mark=s.place_marker((-653.973, 3414.57, 2278.37), (1, 0.14218, 0.14218), 257.758)
if "particle_197 geometry" not in marker_sets:
  s=new_marker_set('particle_197 geometry')
  marker_sets["particle_197 geometry"]=s
s= marker_sets["particle_197 geometry"]
mark=s.place_marker((-1298.86, 3306.33, 2231.04), (1, 0.132701, 0.132701), 215.822)
if "particle_198 geometry" not in marker_sets:
  s=new_marker_set('particle_198 geometry')
  marker_sets["particle_198 geometry"]=s
s= marker_sets["particle_198 geometry"]
mark=s.place_marker((-1950.21, 3288.24, 2071.9), (1, 0.123223, 0.123223), 215.583)
if "particle_199 geometry" not in marker_sets:
  s=new_marker_set('particle_199 geometry')
  marker_sets["particle_199 geometry"]=s
s= marker_sets["particle_199 geometry"]
mark=s.place_marker((-2202.23, 3342.52, 1743.09), (1, 0.113744, 0.113744), 136.961)
if "particle_200 geometry" not in marker_sets:
  s=new_marker_set('particle_200 geometry')
  marker_sets["particle_200 geometry"]=s
s= marker_sets["particle_200 geometry"]
mark=s.place_marker((-1753.3, 3309.86, 1849.96), (1, 0.104265, 0.104265), 180.134)
if "particle_201 geometry" not in marker_sets:
  s=new_marker_set('particle_201 geometry')
  marker_sets["particle_201 geometry"]=s
s= marker_sets["particle_201 geometry"]
mark=s.place_marker((-1158.82, 3441.27, 2018.19), (1, 0.0947867, 0.0947867), 256.869)
if "particle_202 geometry" not in marker_sets:
  s=new_marker_set('particle_202 geometry')
  marker_sets["particle_202 geometry"]=s
s= marker_sets["particle_202 geometry"]
mark=s.place_marker((-480.826, 3457.22, 2074.98), (1, 0.0853081, 0.0853081), 255.155)
if "particle_203 geometry" not in marker_sets:
  s=new_marker_set('particle_203 geometry')
  marker_sets["particle_203 geometry"]=s
s= marker_sets["particle_203 geometry"]
mark=s.place_marker((-619.835, 3370.96, 2618.38), (1, 0.0758294, 0.0758294), 245.869)
if "particle_204 geometry" not in marker_sets:
  s=new_marker_set('particle_204 geometry')
  marker_sets["particle_204 geometry"]=s
s= marker_sets["particle_204 geometry"]
mark=s.place_marker((-1062.79, 3262.46, 2899.14), (1, 0.0663507, 0.0663507), 188.248)
if "particle_205 geometry" not in marker_sets:
  s=new_marker_set('particle_205 geometry')
  marker_sets["particle_205 geometry"]=s
s= marker_sets["particle_205 geometry"]
mark=s.place_marker((-1377.55, 3419.61, 2920.11), (1, 0.056872, 0.056872), 140.258)
if "particle_206 geometry" not in marker_sets:
  s=new_marker_set('particle_206 geometry')
  marker_sets["particle_206 geometry"]=s
s= marker_sets["particle_206 geometry"]
mark=s.place_marker((-1101.71, 3430.95, 2546.19), (1, 0.0473934, 0.0473934), 254.092)
if "particle_207 geometry" not in marker_sets:
  s=new_marker_set('particle_207 geometry')
  marker_sets["particle_207 geometry"]=s
s= marker_sets["particle_207 geometry"]
mark=s.place_marker((-990.713, 3474.75, 2096.19), (1, 0.0379147, 0.0379147), 135.203)
if "particle_208 geometry" not in marker_sets:
  s=new_marker_set('particle_208 geometry')
  marker_sets["particle_208 geometry"]=s
s= marker_sets["particle_208 geometry"]
mark=s.place_marker((-1360.27, 3729.23, 2148.38), (1, 0.028436, 0.028436), 198.835)
if "particle_209 geometry" not in marker_sets:
  s=new_marker_set('particle_209 geometry')
  marker_sets["particle_209 geometry"]=s
s= marker_sets["particle_209 geometry"]
mark=s.place_marker((-1694.4, 3416.85, 2328.95), (1, 0.0189573, 0.0189573), 231.095)
if "particle_210 geometry" not in marker_sets:
  s=new_marker_set('particle_210 geometry')
  marker_sets["particle_210 geometry"]=s
s= marker_sets["particle_210 geometry"]
mark=s.place_marker((-1860.41, 3269.6, 2792.54), (1, 0.00947867, 0.00947867), 251.206)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
