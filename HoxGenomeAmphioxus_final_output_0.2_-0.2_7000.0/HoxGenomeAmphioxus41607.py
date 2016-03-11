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
mark=s.place_marker((-2501.24, 4970.04, 3183.13), (0, 0, 1), 201.612)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((-2395.75, 4528.63, 2909.87), (0.00947867, 0.00947867, 1), 254.309)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((-2219.39, 4095.23, 3032.54), (0.0189573, 0.0189573, 1), 183.366)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((-1963.12, 3702.27, 3099.7), (0.028436, 0.028436, 1), 225.888)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((-1567.01, 3312.9, 3201.63), (0.0379147, 0.0379147, 1), 222.634)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((-1508.72, 3098.71, 3653.14), (0.0473934, 0.0473934, 1), 191.111)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((-1673, 3414.13, 4082.36), (0.056872, 0.056872, 1), 109.473)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((-1572.24, 3684.16, 4542.81), (0.0663507, 0.0663507, 1), 208.923)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((-1240.84, 3775.87, 4792.66), (0.0758294, 0.0758294, 1), 122.729)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((-908.411, 3866.11, 4623.98), (0.0853081, 0.0853081, 1), 153.948)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((-566.914, 3994.02, 4364.84), (0.0947867, 0.0947867, 1), 178.073)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((-441.613, 3665.8, 3903.42), (0.104265, 0.104265, 1), 202.935)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((-175.787, 3469.48, 3629.11), (0.113744, 0.113744, 1), 120.017)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((20.7526, 3259.41, 3660.54), (0.123223, 0.123223, 1), 131.233)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((-187.642, 3605.41, 4120.62), (0.132701, 0.132701, 1), 193.91)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((-139.139, 3997.16, 4516.57), (0.14218, 0.14218, 1), 103.745)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((205.035, 4177.63, 4628.06), (0.151659, 0.151659, 1), 145.986)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((383.551, 3557.85, 3848.13), (0.161137, 0.161137, 1), 229.143)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((642.749, 2759.98, 2962.32), (1, 0.8, 0), 171.629)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((518.105, 3216.89, 3365.98), (0.180095, 0.180095, 1), 138.566)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((165.32, 3393.06, 3294.97), (0.189573, 0.189573, 1), 144.337)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((-62.9235, 3125.54, 3041.89), (0.199052, 0.199052, 1), 253.072)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((-312.174, 2880.17, 3328.06), (0.208531, 0.208531, 1), 195.906)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((-436.108, 2976.28, 3740.87), (0.218009, 0.218009, 1), 169.416)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((-277.331, 3084.48, 4238.58), (0.227488, 0.227488, 1), 310.152)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((180.789, 2700.79, 4317.35), (0.236967, 0.236967, 1), 191.892)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((278.413, 2663.36, 4771.43), (0.246445, 0.246445, 1), 112.163)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((227.021, 2612.13, 4949.14), (0.255924, 0.255924, 1), 197.728)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((97.0288, 2241.7, 5155.13), (0.265403, 0.265403, 1), 221.007)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((-261.064, 1951.56, 5012.89), (0.274882, 0.274882, 1), 209.118)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((-532.95, 1660.9, 4534.85), (0.28436, 0.28436, 1), 226.517)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((-1028.49, 1491.22, 4621.81), (0.293839, 0.293839, 1), 140.171)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((-1530.05, 1473.37, 5000.94), (0.303318, 0.303318, 1), 241.509)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((-2111.21, 1610.3, 5043.6), (0.312796, 0.312796, 1), 194.582)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((-2160.62, 1914.89, 4802.16), (0.322275, 0.322275, 1), 149.934)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((-1857.5, 1622.12, 4474.05), (0.331754, 0.331754, 1), 197.967)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((-2060.95, 1288.62, 4444.75), (0.341232, 0.341232, 1), 120.277)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((-2119.91, 1009.51, 4073.43), (0.350711, 0.350711, 1), 149.522)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((-2346.26, 1112.66, 3835.02), (0.36019, 0.36019, 1), 160.803)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((-2507.98, 1591.53, 4198.63), (0.369668, 0.369668, 1), 149.869)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((-2299.85, 1960.3, 4349.26), (0.379147, 0.379147, 1), 181.37)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((-2228.23, 1522.37, 4151.77), (0.388626, 0.388626, 1), 229.511)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((-2569.14, 944.154, 4053.14), (0.398104, 0.398104, 1), 264.093)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((-2792.52, 540.754, 4039.54), (0.407583, 0.407583, 1), 177.617)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((-2312.18, 557.073, 3930.53), (0.417062, 0.417062, 1), 167.16)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((-2019.23, 263.761, 4241.9), (0.42654, 0.42654, 1), 142.536)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((-1829.74, -125.395, 4567.94), (0.436019, 0.436019, 1), 189.571)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((-1614.25, -686.651, 4359.12), (0.445498, 0.445498, 1), 222.244)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((-1262.52, -903.774, 4547.98), (0.454976, 0.454976, 1), 137.438)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((-783.227, -741.971, 4575.46), (0.464455, 0.464455, 1), 225.953)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((-479.256, -598.042, 4999.06), (0.473934, 0.473934, 1), 202.545)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((-319.201, -240.769, 4890.76), (0.483412, 0.483412, 1), 160.955)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((-141.53, -250.395, 4447.99), (0.492891, 0.492891, 1), 146.767)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((152.625, -239.731, 3815.11), (0.50237, 0.50237, 1), 169.351)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((444.827, 6.35226, 3503.81), (0.511848, 0.511848, 1), 186.968)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((811.715, 52.4499, 3076.49), (0.521327, 0.521327, 1), 217.883)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((1193.27, 17.4252, 2587.53), (0.530806, 0.530806, 1), 238.667)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((1638.12, 28.8845, 2412.92), (0.540284, 0.540284, 1), 157.94)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((1948.1, 91.6865, 2724.9), (0.549763, 0.549763, 1), 182.477)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((1677.64, 123.516, 2263.68), (0.559242, 0.559242, 1), 341.892)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((2306.66, -116.757, 2508.52), (0.56872, 0.56872, 1), 245.002)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((2565.19, -486.213, 2759.91), (0.578199, 0.578199, 1), 147.786)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((2152.98, -633.329, 2713.12), (0.587678, 0.587678, 1), 157.354)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((1694.74, -835.312, 2489.36), (0.597156, 0.597156, 1), 278.238)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((1656.83, -1317.5, 2267.9), (0.606635, 0.606635, 1), 211.136)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((1866.45, -1755.42, 2623.01), (1, 0.8, 0), 195.667)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((1839.16, -1162.08, 2116.39), (0.625592, 0.625592, 1), 206.797)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((1868.7, -776.141, 1643.77), (0.635071, 0.635071, 1), 192.153)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((2039.49, -634.881, 1159.15), (0.64455, 0.64455, 1), 211.505)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((2434.18, -850.251, 876.379), (0.654028, 0.654028, 1), 199.29)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((3018.75, -1243.85, 668.562), (0.663507, 0.663507, 1), 201.937)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((3349.4, -1710.38, 572.536), (0.672986, 0.672986, 1), 115.895)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((2837.03, -1650.71, 587.801), (0.682464, 0.682464, 1), 162.756)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((2468.7, -1755.16, 668.212), (0.691943, 0.691943, 1), 172.996)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((2056.61, -1903.05, 581.402), (0.701422, 0.701422, 1), 270.103)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((1680.37, -2083.52, 877.696), (0.7109, 0.7109, 1), 231.551)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((1325.6, -1681.24, 1345.16), (1, 0.8, 0), 193.867)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((1476.17, -1103.33, 1228.56), (0.729858, 0.729858, 1), 148.047)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((1439.29, -741.945, 1155.78), (0.739336, 0.739336, 1), 219.553)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((1781.17, -1079.87, 1066.41), (0.748815, 0.748815, 1), 263.79)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((1431.96, -541.956, 1416.16), (0.758294, 0.758294, 1), 165.967)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((973.482, -336.401, 1617.9), (0.767773, 0.767773, 1), 208.706)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((730.51, -645.909, 1816.03), (0.777251, 0.777251, 1), 120.928)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((559.594, -980.956, 1791.78), (0.78673, 0.78673, 1), 243.765)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((256.718, -1131.43, 1606.25), (0.796209, 0.796209, 1), 206.558)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((449.615, -1628.12, 1516), (1, 0.3, 0), 187.488)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((473.023, -891.027, 1485.83), (0.815166, 0.815166, 1), 227.45)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((644.176, -743.595, 938.65), (0.824645, 0.824645, 1), 288.522)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((1095.43, -512.829, 706.377), (0.834123, 0.834123, 1), 208.554)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((1017.49, -908.79, 463.454), (0.843602, 0.843602, 1), 212.524)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((1255.3, -1203.71, 128.988), (0.853081, 0.853081, 1), 251.51)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((1361.27, -998.323, 188.774), (0.862559, 0.862559, 1), 216.364)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((753.676, -1061.28, 364.821), (0.872038, 0.872038, 1), 241.661)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((633.686, -1313.37, 214.032), (0.881517, 0.881517, 1), 243.613)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((504.759, -1700.88, -95.4117), (0.890995, 0.890995, 1), 259.581)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((441.432, -1967.45, 97.2452), (0.900474, 0.900474, 1), 174.081)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((183.557, -1826.35, 468.546), (1, 0.3, 0), 132.665)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((211.972, -2349.06, 277.244), (1, 0.3, 0), 201.612)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((268.33, -2071.96, -129.292), (0.92891, 0.92891, 1), 160.109)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((146.229, -1720.16, -25.9531), (0.938389, 0.938389, 1), 155.119)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((115.671, -1470.43, -163.535), (0.947867, 0.947867, 1), 239.187)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((-157.906, -1707.81, -130.659), (0.957346, 0.957346, 1), 121.145)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((-326.951, -1689.37, 446.806), (1, 0.3, 0), 228.513)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((-137.226, -1066.79, 372.803), (0.976303, 0.976303, 1), 147.7)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((-85.6835, -1156.02, -101.792), (0.985782, 0.985782, 1), 217.948)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((38.4995, -864.576, 219.227), (1, 0.3, 0), 190.374)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((544.929, -584.078, 375.493), (1, 0.995261, 0.995261), 245.088)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((856.877, -660.729, -44.0625), (1, 0.985782, 0.985782), 175.534)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((944.234, -771.497, -500.576), (1, 0.976303, 0.976303), 215.41)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((589.868, -916.06, -871.265), (1, 0.966825, 0.966825), 253.463)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((260.489, -1251.68, -1170.12), (1, 0.957346, 0.957346), 256.739)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((-29.8367, -1347.05, -956.401), (1, 0.947867, 0.947867), 151.236)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((81.9783, -971.074, -720.118), (1, 0.938389, 0.938389), 197.75)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((120.66, -465.013, -302.769), (1, 0.92891, 0.92891), 280.994)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((81.9835, -479.529, -718.993), (1, 0.919431, 0.919431), 265.026)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((-170.579, -978.36, -890.737), (1, 0.909953, 0.909953), 210.984)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((-211.046, -553.487, -731.435), (1, 0.900474, 0.900474), 193.91)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((-279.273, -258.421, -352.629), (1, 0.890995, 0.890995), 250.664)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((-444.566, -187.573, 98.7747), (1, 0.881517, 0.881517), 203.716)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((-832.819, -362.456, -362.664), (1, 0.3, 0), 277.501)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((-1085.31, -721.341, -193.797), (1, 0.862559, 0.862559), 198.791)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((-1180.35, -393.757, 169.286), (1, 0.3, 0), 162.647)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((-956.767, -995.333, -188.555), (1, 0.843602, 0.843602), 291.624)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((-752.348, -1331.73, -674.136), (1, 0.834123, 0.834123), 174.471)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((-376.164, -1278.57, -974.447), (1, 0.824645, 0.824645), 218.1)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((-65.3954, -833.505, -1083.59), (1, 0.815166, 0.815166), 260.101)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((124.889, -655.815, -1528.99), (1, 0.805687, 0.805687), 184.69)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((195.046, -551.432, -1853.5), (1, 0.796209, 0.796209), 134.791)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((212.364, -744.8, -1411.2), (1, 0.78673, 0.78673), 256.348)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((-232.389, -891.334, -1250.43), (1, 0.777251, 0.777251), 165.229)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((-664.533, -792.038, -1226.6), (1, 0.767773, 0.767773), 223.111)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((-1082.54, -599.343, -1320.17), (1, 0.758294, 0.758294), 163.428)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((-1478.83, -603.49, -1600.32), (1, 0.748815, 0.748815), 182.346)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((-1574.29, -597.217, -1340.93), (1, 0.739336, 0.739336), 148.784)
if "particle_134 geometry" not in marker_sets:
  s=new_marker_set('particle_134 geometry')
  marker_sets["particle_134 geometry"]=s
s= marker_sets["particle_134 geometry"]
mark=s.place_marker((-1300.7, -631.22, -1049.64), (1, 0.729858, 0.729858), 239.318)
if "particle_135 geometry" not in marker_sets:
  s=new_marker_set('particle_135 geometry')
  marker_sets["particle_135 geometry"]=s
s= marker_sets["particle_135 geometry"]
mark=s.place_marker((-1704.28, -445.211, -971.6), (1, 0.3, 0), 146.268)
if "particle_136 geometry" not in marker_sets:
  s=new_marker_set('particle_136 geometry')
  marker_sets["particle_136 geometry"]=s
s= marker_sets["particle_136 geometry"]
mark=s.place_marker((-1643.12, -503.7, -1432.1), (1, 0.7109, 0.7109), 187.163)
if "particle_137 geometry" not in marker_sets:
  s=new_marker_set('particle_137 geometry')
  marker_sets["particle_137 geometry"]=s
s= marker_sets["particle_137 geometry"]
mark=s.place_marker((-1936.13, -323.417, -1939.49), (1, 0.701422, 0.701422), 174.059)
if "particle_138 geometry" not in marker_sets:
  s=new_marker_set('particle_138 geometry')
  marker_sets["particle_138 geometry"]=s
s= marker_sets["particle_138 geometry"]
mark=s.place_marker((-2319.94, -74.1691, -2414.57), (1, 0.691943, 0.691943), 155.032)
if "particle_139 geometry" not in marker_sets:
  s=new_marker_set('particle_139 geometry')
  marker_sets["particle_139 geometry"]=s
s= marker_sets["particle_139 geometry"]
mark=s.place_marker((-2459.23, 167.643, -2660.74), (1, 0.682464, 0.682464), 71.4199)
if "particle_140 geometry" not in marker_sets:
  s=new_marker_set('particle_140 geometry')
  marker_sets["particle_140 geometry"]=s
s= marker_sets["particle_140 geometry"]
mark=s.place_marker((-2058.44, 400.576, -2382.46), (1, 0.672986, 0.672986), 364.085)
if "particle_141 geometry" not in marker_sets:
  s=new_marker_set('particle_141 geometry')
  marker_sets["particle_141 geometry"]=s
s= marker_sets["particle_141 geometry"]
mark=s.place_marker((-1504.8, 650.625, -1864.11), (1, 0.663507, 0.663507), 155.9)
if "particle_142 geometry" not in marker_sets:
  s=new_marker_set('particle_142 geometry')
  marker_sets["particle_142 geometry"]=s
s= marker_sets["particle_142 geometry"]
mark=s.place_marker((-1214.35, 1135.61, -1702.2), (1, 0.654028, 0.654028), 206.992)
if "particle_143 geometry" not in marker_sets:
  s=new_marker_set('particle_143 geometry')
  marker_sets["particle_143 geometry"]=s
s= marker_sets["particle_143 geometry"]
mark=s.place_marker((-1098.91, 1618.54, -1491.77), (1, 0.64455, 0.64455), 148.459)
if "particle_144 geometry" not in marker_sets:
  s=new_marker_set('particle_144 geometry')
  marker_sets["particle_144 geometry"]=s
s= marker_sets["particle_144 geometry"]
mark=s.place_marker((-757.525, 1522.61, -1136.98), (1, 0.635071, 0.635071), 221.224)
if "particle_145 geometry" not in marker_sets:
  s=new_marker_set('particle_145 geometry')
  marker_sets["particle_145 geometry"]=s
s= marker_sets["particle_145 geometry"]
mark=s.place_marker((-363.092, 1539.64, -815.849), (1, 0.625592, 0.625592), 206.124)
if "particle_146 geometry" not in marker_sets:
  s=new_marker_set('particle_146 geometry')
  marker_sets["particle_146 geometry"]=s
s= marker_sets["particle_146 geometry"]
mark=s.place_marker((-286.946, 1385.8, -390.773), (1, 0.616114, 0.616114), 151.388)
if "particle_147 geometry" not in marker_sets:
  s=new_marker_set('particle_147 geometry')
  marker_sets["particle_147 geometry"]=s
s= marker_sets["particle_147 geometry"]
mark=s.place_marker((-789.272, 1274.29, -721.431), (1, 0.8, 0), 177.378)
if "particle_148 geometry" not in marker_sets:
  s=new_marker_set('particle_148 geometry')
  marker_sets["particle_148 geometry"]=s
s= marker_sets["particle_148 geometry"]
mark=s.place_marker((-637.176, 1599.06, -1430.8), (1, 0.597156, 0.597156), 191.458)
if "particle_149 geometry" not in marker_sets:
  s=new_marker_set('particle_149 geometry')
  marker_sets["particle_149 geometry"]=s
s= marker_sets["particle_149 geometry"]
mark=s.place_marker((-759.835, 1982.72, -2253.31), (1, 0.587678, 0.587678), 249.579)
if "particle_150 geometry" not in marker_sets:
  s=new_marker_set('particle_150 geometry')
  marker_sets["particle_150 geometry"]=s
s= marker_sets["particle_150 geometry"]
mark=s.place_marker((-935.022, 2440.27, -3105.16), (1, 0.578199, 0.578199), 151.735)
if "particle_151 geometry" not in marker_sets:
  s=new_marker_set('particle_151 geometry')
  marker_sets["particle_151 geometry"]=s
s= marker_sets["particle_151 geometry"]
mark=s.place_marker((-1027.39, 1944.43, -2929.23), (1, 0.56872, 0.56872), 124.573)
if "particle_152 geometry" not in marker_sets:
  s=new_marker_set('particle_152 geometry')
  marker_sets["particle_152 geometry"]=s
s= marker_sets["particle_152 geometry"]
mark=s.place_marker((-775.864, 1475.6, -2367.12), (1, 0.559242, 0.559242), 184.342)
if "particle_153 geometry" not in marker_sets:
  s=new_marker_set('particle_153 geometry')
  marker_sets["particle_153 geometry"]=s
s= marker_sets["particle_153 geometry"]
mark=s.place_marker((-555.645, 1113.53, -2066.13), (1, 0.549763, 0.549763), 202.588)
if "particle_154 geometry" not in marker_sets:
  s=new_marker_set('particle_154 geometry')
  marker_sets["particle_154 geometry"]=s
s= marker_sets["particle_154 geometry"]
mark=s.place_marker((-315.499, 807.742, -2317.82), (1, 0.540284, 0.540284), 221.463)
if "particle_155 geometry" not in marker_sets:
  s=new_marker_set('particle_155 geometry')
  marker_sets["particle_155 geometry"]=s
s= marker_sets["particle_155 geometry"]
mark=s.place_marker((-130.54, 522.585, -2101.84), (1, 0.8, 0), 134.639)
if "particle_156 geometry" not in marker_sets:
  s=new_marker_set('particle_156 geometry')
  marker_sets["particle_156 geometry"]=s
s= marker_sets["particle_156 geometry"]
mark=s.place_marker((341.462, 580.111, -2578.46), (1, 0.521327, 0.521327), 219.727)
if "particle_157 geometry" not in marker_sets:
  s=new_marker_set('particle_157 geometry')
  marker_sets["particle_157 geometry"]=s
s= marker_sets["particle_157 geometry"]
mark=s.place_marker((791.529, 585.77, -2932.25), (1, 0.511848, 0.511848), 185.536)
if "particle_158 geometry" not in marker_sets:
  s=new_marker_set('particle_158 geometry')
  marker_sets["particle_158 geometry"]=s
s= marker_sets["particle_158 geometry"]
mark=s.place_marker((1118.99, 216.978, -2788.59), (1, 0.50237, 0.50237), 191.263)
if "particle_159 geometry" not in marker_sets:
  s=new_marker_set('particle_159 geometry')
  marker_sets["particle_159 geometry"]=s
s= marker_sets["particle_159 geometry"]
mark=s.place_marker((1268.69, -63.9726, -2388.66), (1, 0.492891, 0.492891), 162.496)
if "particle_160 geometry" not in marker_sets:
  s=new_marker_set('particle_160 geometry')
  marker_sets["particle_160 geometry"]=s
s= marker_sets["particle_160 geometry"]
mark=s.place_marker((1235.67, -76.2502, -1943.78), (1, 0.483412, 0.483412), 202.935)
if "particle_161 geometry" not in marker_sets:
  s=new_marker_set('particle_161 geometry')
  marker_sets["particle_161 geometry"]=s
s= marker_sets["particle_161 geometry"]
mark=s.place_marker((1548.61, 169.137, -1887.28), (1, 0.473934, 0.473934), 186.295)
if "particle_162 geometry" not in marker_sets:
  s=new_marker_set('particle_162 geometry')
  marker_sets["particle_162 geometry"]=s
s= marker_sets["particle_162 geometry"]
mark=s.place_marker((1927.42, 86.1016, -2025.14), (1, 0.464455, 0.464455), 153.297)
if "particle_163 geometry" not in marker_sets:
  s=new_marker_set('particle_163 geometry')
  marker_sets["particle_163 geometry"]=s
s= marker_sets["particle_163 geometry"]
mark=s.place_marker((2054.46, 377.745, -2230.4), (1, 0.454976, 0.454976), 144.944)
if "particle_164 geometry" not in marker_sets:
  s=new_marker_set('particle_164 geometry')
  marker_sets["particle_164 geometry"]=s
s= marker_sets["particle_164 geometry"]
mark=s.place_marker((2326.98, 489.974, -2541.32), (1, 0.445498, 0.445498), 165.489)
if "particle_165 geometry" not in marker_sets:
  s=new_marker_set('particle_165 geometry')
  marker_sets["particle_165 geometry"]=s
s= marker_sets["particle_165 geometry"]
mark=s.place_marker((2574.58, 770.131, -2735.33), (1, 0.436019, 0.436019), 160.326)
if "particle_166 geometry" not in marker_sets:
  s=new_marker_set('particle_166 geometry')
  marker_sets["particle_166 geometry"]=s
s= marker_sets["particle_166 geometry"]
mark=s.place_marker((2301.39, 520.1, -2352.84), (1, 0.42654, 0.42654), 168.006)
if "particle_167 geometry" not in marker_sets:
  s=new_marker_set('particle_167 geometry')
  marker_sets["particle_167 geometry"]=s
s= marker_sets["particle_167 geometry"]
mark=s.place_marker((2323.73, 131.914, -2475.72), (1, 0.417062, 0.417062), 262.423)
if "particle_168 geometry" not in marker_sets:
  s=new_marker_set('particle_168 geometry')
  marker_sets["particle_168 geometry"]=s
s= marker_sets["particle_168 geometry"]
mark=s.place_marker((2636.22, 395.558, -2913.73), (1, 0.407583, 0.407583), 32.2822)
if "particle_169 geometry" not in marker_sets:
  s=new_marker_set('particle_169 geometry')
  marker_sets["particle_169 geometry"]=s
s= marker_sets["particle_169 geometry"]
mark=s.place_marker((2447.29, 747.05, -2992.02), (1, 0.398104, 0.398104), 230.943)
if "particle_170 geometry" not in marker_sets:
  s=new_marker_set('particle_170 geometry')
  marker_sets["particle_170 geometry"]=s
s= marker_sets["particle_170 geometry"]
mark=s.place_marker((2131.44, 818.248, -2428.57), (1, 0.388626, 0.388626), 158.612)
if "particle_171 geometry" not in marker_sets:
  s=new_marker_set('particle_171 geometry')
  marker_sets["particle_171 geometry"]=s
s= marker_sets["particle_171 geometry"]
mark=s.place_marker((1921.71, 775.097, -1802.08), (1, 0.379147, 0.379147), 172.454)
if "particle_172 geometry" not in marker_sets:
  s=new_marker_set('particle_172 geometry')
  marker_sets["particle_172 geometry"]=s
s= marker_sets["particle_172 geometry"]
mark=s.place_marker((1796.03, 687.558, -1283.55), (1, 0.369668, 0.369668), 192.153)
if "particle_173 geometry" not in marker_sets:
  s=new_marker_set('particle_173 geometry')
  marker_sets["particle_173 geometry"]=s
s= marker_sets["particle_173 geometry"]
mark=s.place_marker((1726.56, 738.46, -712.605), (1, 0.8, 0), 153.123)
if "particle_174 geometry" not in marker_sets:
  s=new_marker_set('particle_174 geometry')
  marker_sets["particle_174 geometry"]=s
s= marker_sets["particle_174 geometry"]
mark=s.place_marker((2274.66, 1418.58, -1049.43), (1, 0.350711, 0.350711), 164.079)
if "particle_175 geometry" not in marker_sets:
  s=new_marker_set('particle_175 geometry')
  marker_sets["particle_175 geometry"]=s
s= marker_sets["particle_175 geometry"]
mark=s.place_marker((2725.89, 1693.85, -1536.31), (1, 0.341232, 0.341232), 130.669)
if "particle_176 geometry" not in marker_sets:
  s=new_marker_set('particle_176 geometry')
  marker_sets["particle_176 geometry"]=s
s= marker_sets["particle_176 geometry"]
mark=s.place_marker((2514.57, 1004.29, -1383.15), (1, 0.331754, 0.331754), 260.579)
if "particle_177 geometry" not in marker_sets:
  s=new_marker_set('particle_177 geometry')
  marker_sets["particle_177 geometry"]=s
s= marker_sets["particle_177 geometry"]
mark=s.place_marker((2432.52, 484.503, -1023.28), (1, 0.322275, 0.322275), 214.737)
if "particle_178 geometry" not in marker_sets:
  s=new_marker_set('particle_178 geometry')
  marker_sets["particle_178 geometry"]=s
s= marker_sets["particle_178 geometry"]
mark=s.place_marker((2590.24, 83.9532, -1348.13), (1, 0.312796, 0.312796), 284.617)
if "particle_179 geometry" not in marker_sets:
  s=new_marker_set('particle_179 geometry')
  marker_sets["particle_179 geometry"]=s
s= marker_sets["particle_179 geometry"]
mark=s.place_marker((2749.24, 186.759, -1970.4), (1, 0.303318, 0.303318), 277.891)
if "particle_180 geometry" not in marker_sets:
  s=new_marker_set('particle_180 geometry')
  marker_sets["particle_180 geometry"]=s
s= marker_sets["particle_180 geometry"]
mark=s.place_marker((3145.54, 436.159, -2196.9), (1, 0.293839, 0.293839), 132.318)
if "particle_181 geometry" not in marker_sets:
  s=new_marker_set('particle_181 geometry')
  marker_sets["particle_181 geometry"]=s
s= marker_sets["particle_181 geometry"]
mark=s.place_marker((3479.94, 699.913, -2301.79), (1, 0.28436, 0.28436), 179.917)
if "particle_182 geometry" not in marker_sets:
  s=new_marker_set('particle_182 geometry')
  marker_sets["particle_182 geometry"]=s
s= marker_sets["particle_182 geometry"]
mark=s.place_marker((3358.69, 1054.55, -2358.63), (1, 0.274882, 0.274882), 120.125)
if "particle_183 geometry" not in marker_sets:
  s=new_marker_set('particle_183 geometry')
  marker_sets["particle_183 geometry"]=s
s= marker_sets["particle_183 geometry"]
mark=s.place_marker((3081.5, 932.764, -1930.86), (1, 0.265403, 0.265403), 220.204)
if "particle_184 geometry" not in marker_sets:
  s=new_marker_set('particle_184 geometry')
  marker_sets["particle_184 geometry"]=s
s= marker_sets["particle_184 geometry"]
mark=s.place_marker((3066.56, 481.206, -1700.85), (1, 0.255924, 0.255924), 218.035)
if "particle_185 geometry" not in marker_sets:
  s=new_marker_set('particle_185 geometry')
  marker_sets["particle_185 geometry"]=s
s= marker_sets["particle_185 geometry"]
mark=s.place_marker((2533.07, 251.489, -1544.86), (1, 0.246445, 0.246445), 236.063)
if "particle_186 geometry" not in marker_sets:
  s=new_marker_set('particle_186 geometry')
  marker_sets["particle_186 geometry"]=s
s= marker_sets["particle_186 geometry"]
mark=s.place_marker((2425.54, 47.5071, -1950.07), (1, 0.236967, 0.236967), 157.853)
if "particle_187 geometry" not in marker_sets:
  s=new_marker_set('particle_187 geometry')
  marker_sets["particle_187 geometry"]=s
s= marker_sets["particle_187 geometry"]
mark=s.place_marker((2783.57, -196.171, -2281.45), (1, 0.227488, 0.227488), 151.735)
if "particle_188 geometry" not in marker_sets:
  s=new_marker_set('particle_188 geometry')
  marker_sets["particle_188 geometry"]=s
s= marker_sets["particle_188 geometry"]
mark=s.place_marker((2610.71, -134.963, -2467), (1, 0.218009, 0.218009), 132.101)
if "particle_189 geometry" not in marker_sets:
  s=new_marker_set('particle_189 geometry')
  marker_sets["particle_189 geometry"]=s
s= marker_sets["particle_189 geometry"]
mark=s.place_marker((2575.24, 240.698, -2284.75), (1, 0.208531, 0.208531), 180.567)
if "particle_190 geometry" not in marker_sets:
  s=new_marker_set('particle_190 geometry')
  marker_sets["particle_190 geometry"]=s
s= marker_sets["particle_190 geometry"]
mark=s.place_marker((2410.53, 840.131, -2178.84), (1, 0.199052, 0.199052), 231.073)
if "particle_191 geometry" not in marker_sets:
  s=new_marker_set('particle_191 geometry')
  marker_sets["particle_191 geometry"]=s
s= marker_sets["particle_191 geometry"]
mark=s.place_marker((2270.76, 1326.53, -2500.58), (1, 0.189573, 0.189573), 173.473)
if "particle_192 geometry" not in marker_sets:
  s=new_marker_set('particle_192 geometry')
  marker_sets["particle_192 geometry"]=s
s= marker_sets["particle_192 geometry"]
mark=s.place_marker((2041.38, 1006.49, -2728.64), (1, 0.180095, 0.180095), 184.993)
if "particle_193 geometry" not in marker_sets:
  s=new_marker_set('particle_193 geometry')
  marker_sets["particle_193 geometry"]=s
s= marker_sets["particle_193 geometry"]
mark=s.place_marker((2212.07, 1189.31, -2949.71), (1, 0.170616, 0.170616), 147.396)
if "particle_194 geometry" not in marker_sets:
  s=new_marker_set('particle_194 geometry')
  marker_sets["particle_194 geometry"]=s
s= marker_sets["particle_194 geometry"]
mark=s.place_marker((2395.48, 1628.44, -3090.5), (1, 0.161137, 0.161137), 236.172)
if "particle_195 geometry" not in marker_sets:
  s=new_marker_set('particle_195 geometry')
  marker_sets["particle_195 geometry"]=s
s= marker_sets["particle_195 geometry"]
mark=s.place_marker((2565.49, 1860.61, -2733.54), (1, 0.151659, 0.151659), 146.788)
if "particle_196 geometry" not in marker_sets:
  s=new_marker_set('particle_196 geometry')
  marker_sets["particle_196 geometry"]=s
s= marker_sets["particle_196 geometry"]
mark=s.place_marker((2413.64, 1699.82, -2287.99), (1, 0.14218, 0.14218), 257.758)
if "particle_197 geometry" not in marker_sets:
  s=new_marker_set('particle_197 geometry')
  marker_sets["particle_197 geometry"]=s
s= marker_sets["particle_197 geometry"]
mark=s.place_marker((2697.89, 1118.62, -2437), (1, 0.132701, 0.132701), 215.822)
if "particle_198 geometry" not in marker_sets:
  s=new_marker_set('particle_198 geometry')
  marker_sets["particle_198 geometry"]=s
s= marker_sets["particle_198 geometry"]
mark=s.place_marker((3117.42, 579.906, -2511.11), (1, 0.123223, 0.123223), 215.583)
if "particle_199 geometry" not in marker_sets:
  s=new_marker_set('particle_199 geometry')
  marker_sets["particle_199 geometry"]=s
s= marker_sets["particle_199 geometry"]
mark=s.place_marker((3440.84, 390.568, -2327.25), (1, 0.113744, 0.113744), 136.961)
if "particle_200 geometry" not in marker_sets:
  s=new_marker_set('particle_200 geometry')
  marker_sets["particle_200 geometry"]=s
s= marker_sets["particle_200 geometry"]
mark=s.place_marker((3139.77, 764.353, -2284.68), (1, 0.104265, 0.104265), 180.134)
if "particle_201 geometry" not in marker_sets:
  s=new_marker_set('particle_201 geometry')
  marker_sets["particle_201 geometry"]=s
s= marker_sets["particle_201 geometry"]
mark=s.place_marker((2801, 1307.65, -2246.43), (1, 0.0947867, 0.0947867), 256.869)
if "particle_202 geometry" not in marker_sets:
  s=new_marker_set('particle_202 geometry')
  marker_sets["particle_202 geometry"]=s
s= marker_sets["particle_202 geometry"]
mark=s.place_marker((2401.43, 1840.99, -2064.33), (1, 0.0853081, 0.0853081), 255.155)
if "particle_203 geometry" not in marker_sets:
  s=new_marker_set('particle_203 geometry')
  marker_sets["particle_203 geometry"]=s
s= marker_sets["particle_203 geometry"]
mark=s.place_marker((2136.93, 1760.85, -2559.91), (1, 0.0758294, 0.0758294), 245.869)
if "particle_204 geometry" not in marker_sets:
  s=new_marker_set('particle_204 geometry')
  marker_sets["particle_204 geometry"]=s
s= marker_sets["particle_204 geometry"]
mark=s.place_marker((2183.98, 1415.68, -2965.86), (1, 0.0663507, 0.0663507), 188.248)
if "particle_205 geometry" not in marker_sets:
  s=new_marker_set('particle_205 geometry')
  marker_sets["particle_205 geometry"]=s
s= marker_sets["particle_205 geometry"]
mark=s.place_marker((2479.39, 1291.03, -3119.92), (1, 0.056872, 0.056872), 140.258)
if "particle_206 geometry" not in marker_sets:
  s=new_marker_set('particle_206 geometry')
  marker_sets["particle_206 geometry"]=s
s= marker_sets["particle_206 geometry"]
mark=s.place_marker((2505.94, 1452.9, -2678.26), (1, 0.0473934, 0.0473934), 254.092)
if "particle_207 geometry" not in marker_sets:
  s=new_marker_set('particle_207 geometry')
  marker_sets["particle_207 geometry"]=s
s= marker_sets["particle_207 geometry"]
mark=s.place_marker((2675.22, 1515.86, -2239.65), (1, 0.0379147, 0.0379147), 135.203)
if "particle_208 geometry" not in marker_sets:
  s=new_marker_set('particle_208 geometry')
  marker_sets["particle_208 geometry"]=s
s= marker_sets["particle_208 geometry"]
mark=s.place_marker((3039.29, 1430.01, -2484.46), (1, 0.028436, 0.028436), 198.835)
if "particle_209 geometry" not in marker_sets:
  s=new_marker_set('particle_209 geometry')
  marker_sets["particle_209 geometry"]=s
s= marker_sets["particle_209 geometry"]
mark=s.place_marker((2913.23, 1004.19, -2704.4), (1, 0.0189573, 0.0189573), 231.095)
if "particle_210 geometry" not in marker_sets:
  s=new_marker_set('particle_210 geometry')
  marker_sets["particle_210 geometry"]=s
s= marker_sets["particle_210 geometry"]
mark=s.place_marker((2716.8, 910.901, -3171.86), (1, 0.00947867, 0.00947867), 251.206)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
