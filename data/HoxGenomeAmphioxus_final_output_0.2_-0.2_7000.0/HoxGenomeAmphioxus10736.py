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
mark=s.place_marker((4605.57, 2803.57, -1224.89), (0, 0, 1), 201.612)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((4144.32, 2493.65, -1345.98), (0.00947867, 0.00947867, 1), 254.309)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((3755.03, 2474.91, -1561.23), (0.0189573, 0.0189573, 1), 183.366)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((3301.52, 2452.01, -1513.66), (0.028436, 0.028436, 1), 225.888)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((2822.07, 2610.66, -1267.49), (0.0379147, 0.0379147, 1), 222.634)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((2718.73, 3063.27, -1276.69), (0.0473934, 0.0473934, 1), 191.111)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((3208.26, 3341.9, -1370.46), (0.056872, 0.056872, 1), 109.473)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((3529.1, 3682.4, -1230.83), (0.0663507, 0.0663507, 1), 208.923)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((3585.18, 3863.63, -883.392), (0.0758294, 0.0758294, 1), 122.729)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((3581.51, 3708.64, -605.542), (0.0853081, 0.0853081, 1), 153.948)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((3435.79, 3779.67, -298.29), (0.0947867, 0.0947867, 1), 178.073)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((2908.13, 3450.73, -385.837), (0.104265, 0.104265, 1), 202.935)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((2420.22, 3522.13, -493.79), (0.113744, 0.113744, 1), 120.017)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((2119.15, 3710.93, -639.416), (0.123223, 0.123223, 1), 131.233)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((2559.74, 4029.93, -901.793), (0.132701, 0.132701, 1), 193.91)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((2931.34, 4487.54, -945.781), (0.14218, 0.14218, 1), 103.745)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((2955.9, 4926.34, -773.491), (0.151659, 0.151659, 1), 145.986)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((2048.1, 4421.17, -662.855), (0.161137, 0.161137, 1), 229.143)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((896.617, 3994.57, -540.173), (1, 0.8, 0), 171.629)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((1460.18, 4027.9, -559.943), (0.180095, 0.180095, 1), 138.566)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((1806.12, 3783.12, -634.701), (0.189573, 0.189573, 1), 144.337)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((1698.82, 3396.34, -775.237), (0.199052, 0.199052, 1), 253.072)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((1935.92, 3297.28, -611.936), (0.208531, 0.208531, 1), 195.906)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((2140.33, 3561.98, -813.886), (0.218009, 0.218009, 1), 169.416)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((2503.82, 3819.62, -533.112), (0.227488, 0.227488, 1), 310.152)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((2162.26, 3796.27, -33.8516), (0.236967, 0.236967, 1), 191.892)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((2421.58, 4034.43, 274.366), (0.246445, 0.246445, 1), 112.163)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((2713.02, 3781.68, 540.796), (0.255924, 0.255924, 1), 197.728)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((2966.65, 3499.93, 910.093), (0.265403, 0.265403, 1), 221.007)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((2942.24, 3056.25, 1002.91), (0.274882, 0.274882, 1), 209.118)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((2544.84, 2881.32, 603.96), (0.28436, 0.28436, 1), 226.517)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((2850.53, 2874.33, 197.053), (0.293839, 0.293839, 1), 140.171)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((3335.84, 3014.29, -130.89), (0.303318, 0.303318, 1), 241.509)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((3724.06, 2872.15, -548.95), (0.312796, 0.312796, 1), 194.582)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((3523.13, 3005.22, -869.699), (0.322275, 0.322275, 1), 149.934)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((2998.61, 2927.55, -784.749), (0.331754, 0.331754, 1), 197.967)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((2872.5, 2851.47, -1105.09), (0.341232, 0.341232, 1), 120.277)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((2616.19, 2485.85, -1213.24), (0.350711, 0.350711, 1), 149.522)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((2728.02, 2129.72, -1191.29), (0.36019, 0.36019, 1), 160.803)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((3108.13, 2467.31, -1205.14), (0.369668, 0.369668, 1), 149.869)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((3191.72, 2782.82, -961.118), (0.379147, 0.379147, 1), 181.37)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((2972.38, 2826.43, -549.917), (0.388626, 0.388626, 1), 229.511)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((3255.11, 2372.96, -586.601), (0.398104, 0.398104, 1), 264.093)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((3119.29, 2519.89, -92.7833), (0.407583, 0.407583, 1), 177.617)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((2864.49, 2303.4, 381.055), (0.417062, 0.417062, 1), 167.16)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((2677.73, 2291.99, 959.44), (0.42654, 0.42654, 1), 142.536)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((2398.5, 2261.6, 1478.81), (0.436019, 0.436019, 1), 189.571)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((1844.95, 2048.3, 1783.81), (0.445498, 0.445498, 1), 222.244)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((1964.76, 2578.3, 1956.01), (0.454976, 0.454976, 1), 137.438)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((1507.73, 2659.78, 2093.52), (0.464455, 0.464455, 1), 225.953)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((1322.11, 2699.27, 2569.35), (0.473934, 0.473934, 1), 202.545)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((1215.36, 2335.27, 2771.38), (0.483412, 0.483412, 1), 160.955)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((957.404, 1983.99, 2746.08), (0.492891, 0.492891, 1), 146.767)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((472.844, 1872.86, 2418.93), (0.50237, 0.50237, 1), 169.351)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((269.029, 1873, 2112.92), (0.511848, 0.511848, 1), 186.968)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((-142.061, 1803.68, 2008.31), (0.521327, 0.521327, 1), 217.883)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((-542.548, 1588.8, 1879.64), (0.530806, 0.530806, 1), 238.667)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((-547.168, 1984.54, 1825.74), (0.540284, 0.540284, 1), 157.94)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((-488.912, 2443.06, 1875.42), (0.549763, 0.549763, 1), 182.477)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((-695.486, 2418.99, 1361.59), (0.559242, 0.559242, 1), 341.892)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((-701.239, 2367.54, 2091.04), (0.56872, 0.56872, 1), 245.002)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((-1023.58, 2554.77, 2386.63), (0.578199, 0.578199, 1), 147.786)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((-1209.98, 2650.18, 1933.32), (0.587678, 0.587678, 1), 157.354)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((-1504.91, 2594.99, 1423.73), (0.597156, 0.597156, 1), 278.238)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((-1968.31, 2331.02, 1396.42), (0.606635, 0.606635, 1), 211.136)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((-2291.06, 2778.01, 1629.58), (1, 0.8, 0), 195.667)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((-1713.79, 2267.66, 1492.33), (0.625592, 0.625592, 1), 206.797)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((-1305.84, 1802.4, 1475.73), (0.635071, 0.635071, 1), 192.153)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((-1144.65, 1313.55, 1672.5), (0.64455, 0.64455, 1), 211.505)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((-1364.74, 1016.86, 2102.88), (0.654028, 0.654028, 1), 199.29)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((-1715.28, 766.296, 2735.46), (0.663507, 0.663507, 1), 201.937)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((-2128.19, 632.249, 3115.9), (0.672986, 0.672986, 1), 115.895)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((-2157.92, 613.712, 2588.55), (0.682464, 0.682464, 1), 162.756)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((-2363.17, 567.159, 2233.25), (0.691943, 0.691943, 1), 172.996)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((-2601.71, 417.026, 1857), (0.701422, 0.701422, 1), 270.103)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((-2618.21, 703.563, 1616.46), (0.7109, 0.7109, 1), 231.551)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((-2328.37, 1268.44, 1269.26), (1, 0.8, 0), 193.867)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((-1777.36, 1135.13, 1339.02), (0.729858, 0.729858, 1), 148.047)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((-1515.46, 978.36, 1324.96), (0.739336, 0.739336, 1), 219.553)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((-1594.35, 672.589, 1697.6), (0.748815, 0.748815, 1), 263.79)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((-1165.16, 1122.52, 1340.11), (0.758294, 0.758294, 1), 165.967)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((-1010.38, 1411.06, 934.366), (0.767773, 0.767773, 1), 208.706)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((-1355.51, 1568.29, 840.464), (0.777251, 0.777251, 1), 120.928)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((-1684, 1387.08, 785.807), (0.78673, 0.78673, 1), 243.765)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((-1999.64, 1039.94, 736.835), (0.796209, 0.796209, 1), 206.558)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((-2490.97, 1339.42, 569.859), (1, 0.3, 0), 187.488)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((-1797.13, 1368.87, 458.869), (0.815166, 0.815166, 1), 227.45)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((-1579.93, 788.458, 579.537), (0.824645, 0.824645, 1), 288.522)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((-1326.66, 519.705, 974.508), (0.834123, 0.834123, 1), 208.554)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((-1704.86, 347.435, 747.66), (0.843602, 0.843602, 1), 212.524)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((-1999.88, -13.9884, 925.435), (0.853081, 0.853081, 1), 251.51)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((-1609.09, 205.281, 967.425), (0.862559, 0.862559, 1), 216.364)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((-1698.73, 453.323, 373.652), (0.872038, 0.872038, 1), 241.661)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((-2002.09, 298.364, 237.333), (0.881517, 0.881517, 1), 243.613)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((-2376.57, -30.4137, 72.4003), (0.890995, 0.890995, 1), 259.581)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((-2654.54, 125.591, 6.36756), (0.900474, 0.900474, 1), 174.081)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((-2388.32, 433.283, -130.693), (1, 0.3, 0), 132.665)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((-2853.9, 402.008, -331.52), (1, 0.3, 0), 201.612)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((-2624.67, 125.623, -477.965), (0.92891, 0.92891, 1), 160.109)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((-2280.48, 406.459, -496.871), (0.938389, 0.938389, 1), 155.119)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((-1883.29, 660.905, -457.063), (0.947867, 0.947867, 1), 239.187)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((-1666.14, 1080.42, -519.492), (0.957346, 0.957346, 1), 121.145)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((-2009.05, 812.735, -708.035), (1, 0.3, 0), 228.513)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((-1457.29, 1112.26, -661.673), (0.976303, 0.976303, 1), 147.7)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((-1388.93, 772.785, -704.082), (0.985782, 0.985782, 1), 217.948)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((-1430.88, 445.75, -379.287), (1, 0.3, 0), 190.374)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((-1086.9, 706.627, 58.741), (1, 0.995261, 0.995261), 245.088)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((-985.497, 361.33, 420.49), (1, 0.985782, 0.985782), 175.534)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((-1043.14, -104.974, 565.229), (1, 0.976303, 0.976303), 215.41)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((-1277.3, -603.746, 366.663), (1, 0.966825, 0.966825), 253.463)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((-1658.99, -991.359, 173.78), (1, 0.957346, 0.957346), 256.739)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((-1892.35, -873.6, -131.018), (1, 0.947867, 0.947867), 151.236)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((-1545.65, -575.575, -117.538), (1, 0.938389, 0.938389), 197.75)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((-1066.11, -117.691, -195.392), (1, 0.92891, 0.92891), 280.994)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((-1184.39, -653.573, -232.68), (1, 0.919431, 0.919431), 265.026)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((-1700.92, -919.595, -361.716), (1, 0.909953, 0.909953), 210.984)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((-1409.02, -861.792, -518.661), (1, 0.900474, 0.900474), 193.91)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((-1236.26, -606.044, -650.754), (1, 0.890995, 0.890995), 250.664)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((-1143.92, -145.668, -716.016), (1, 0.881517, 0.881517), 203.716)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((-1403.19, -474.543, -1181.88), (1, 0.3, 0), 277.501)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((-1604.26, -313.477, -1484.42), (1, 0.862559, 0.862559), 198.791)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((-1144.71, 33.2563, -1433.4), (1, 0.3, 0), 162.647)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((-1506.37, -378.559, -880.348), (1, 0.843602, 0.843602), 291.624)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((-1433.59, -700.906, -343.744), (1, 0.834123, 0.834123), 174.471)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((-1057.94, -495.788, -6.71608), (1, 0.824645, 0.824645), 218.1)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((-542.127, -262.734, -52.9096), (1, 0.815166, 0.815166), 260.101)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((-62.9986, -502.333, 58.305), (1, 0.805687, 0.805687), 184.69)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((282.834, -662.531, 14.6684), (1, 0.796209, 0.796209), 134.791)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((10.6628, -220.454, 7.2791), (1, 0.78673, 0.78673), 256.348)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((-172.864, 4.37682, -409.018), (1, 0.777251, 0.777251), 165.229)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((-45.1483, 182.749, -891.441), (1, 0.767773, 0.767773), 223.111)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((129.311, 267.634, -1384.13), (1, 0.758294, 0.758294), 163.428)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((256.144, 87.9458, -1843.17), (1, 0.748815, 0.748815), 182.346)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((5.66032, -4.87336, -1939.45), (1, 0.739336, 0.739336), 148.784)
if "particle_134 geometry" not in marker_sets:
  s=new_marker_set('particle_134 geometry')
  marker_sets["particle_134 geometry"]=s
s= marker_sets["particle_134 geometry"]
mark=s.place_marker((-331.194, -111.322, -1702.05), (1, 0.729858, 0.729858), 239.318)
if "particle_135 geometry" not in marker_sets:
  s=new_marker_set('particle_135 geometry')
  marker_sets["particle_135 geometry"]=s
s= marker_sets["particle_135 geometry"]
mark=s.place_marker((-473.609, -504.541, -1995.31), (1, 0.3, 0), 146.268)
if "particle_136 geometry" not in marker_sets:
  s=new_marker_set('particle_136 geometry')
  marker_sets["particle_136 geometry"]=s
s= marker_sets["particle_136 geometry"]
mark=s.place_marker((-689.352, -998.003, -2118.56), (1, 0.7109, 0.7109), 187.163)
if "particle_137 geometry" not in marker_sets:
  s=new_marker_set('particle_137 geometry')
  marker_sets["particle_137 geometry"]=s
s= marker_sets["particle_137 geometry"]
mark=s.place_marker((-522.489, -1603.99, -2344.56), (1, 0.701422, 0.701422), 174.059)
if "particle_138 geometry" not in marker_sets:
  s=new_marker_set('particle_138 geometry')
  marker_sets["particle_138 geometry"]=s
s= marker_sets["particle_138 geometry"]
mark=s.place_marker((-187.811, -2146.54, -2575.31), (1, 0.691943, 0.691943), 155.032)
if "particle_139 geometry" not in marker_sets:
  s=new_marker_set('particle_139 geometry')
  marker_sets["particle_139 geometry"]=s
s= marker_sets["particle_139 geometry"]
mark=s.place_marker((107.749, -2436.27, -2570.46), (1, 0.682464, 0.682464), 71.4199)
if "particle_140 geometry" not in marker_sets:
  s=new_marker_set('particle_140 geometry')
  marker_sets["particle_140 geometry"]=s
s= marker_sets["particle_140 geometry"]
mark=s.place_marker((357.325, -2303.49, -2033.41), (1, 0.672986, 0.672986), 364.085)
if "particle_141 geometry" not in marker_sets:
  s=new_marker_set('particle_141 geometry')
  marker_sets["particle_141 geometry"]=s
s= marker_sets["particle_141 geometry"]
mark=s.place_marker((481.159, -1834.03, -1352.2), (1, 0.663507, 0.663507), 155.9)
if "particle_142 geometry" not in marker_sets:
  s=new_marker_set('particle_142 geometry')
  marker_sets["particle_142 geometry"]=s
s= marker_sets["particle_142 geometry"]
mark=s.place_marker((822.971, -1604.05, -958.059), (1, 0.654028, 0.654028), 206.992)
if "particle_143 geometry" not in marker_sets:
  s=new_marker_set('particle_143 geometry')
  marker_sets["particle_143 geometry"]=s
s= marker_sets["particle_143 geometry"]
mark=s.place_marker((1132.26, -1279.37, -987.913), (1, 0.64455, 0.64455), 148.459)
if "particle_144 geometry" not in marker_sets:
  s=new_marker_set('particle_144 geometry')
  marker_sets["particle_144 geometry"]=s
s= marker_sets["particle_144 geometry"]
mark=s.place_marker((681.135, -1196.86, -925.12), (1, 0.635071, 0.635071), 221.224)
if "particle_145 geometry" not in marker_sets:
  s=new_marker_set('particle_145 geometry')
  marker_sets["particle_145 geometry"]=s
s= marker_sets["particle_145 geometry"]
mark=s.place_marker((519.433, -945.962, -604.276), (1, 0.625592, 0.625592), 206.124)
if "particle_146 geometry" not in marker_sets:
  s=new_marker_set('particle_146 geometry')
  marker_sets["particle_146 geometry"]=s
s= marker_sets["particle_146 geometry"]
mark=s.place_marker((240.551, -644.53, -750.589), (1, 0.616114, 0.616114), 151.388)
if "particle_147 geometry" not in marker_sets:
  s=new_marker_set('particle_147 geometry')
  marker_sets["particle_147 geometry"]=s
s= marker_sets["particle_147 geometry"]
mark=s.place_marker((65.3875, -1200.87, -1303.64), (1, 0.8, 0), 177.378)
if "particle_148 geometry" not in marker_sets:
  s=new_marker_set('particle_148 geometry')
  marker_sets["particle_148 geometry"]=s
s= marker_sets["particle_148 geometry"]
mark=s.place_marker((637.611, -1606.45, -850.552), (1, 0.597156, 0.597156), 191.458)
if "particle_149 geometry" not in marker_sets:
  s=new_marker_set('particle_149 geometry')
  marker_sets["particle_149 geometry"]=s
s= marker_sets["particle_149 geometry"]
mark=s.place_marker((1322.48, -2154.7, -753.399), (1, 0.587678, 0.587678), 249.579)
if "particle_150 geometry" not in marker_sets:
  s=new_marker_set('particle_150 geometry')
  marker_sets["particle_150 geometry"]=s
s= marker_sets["particle_150 geometry"]
mark=s.place_marker((2012.76, -2830.2, -768.881), (1, 0.578199, 0.578199), 151.735)
if "particle_151 geometry" not in marker_sets:
  s=new_marker_set('particle_151 geometry')
  marker_sets["particle_151 geometry"]=s
s= marker_sets["particle_151 geometry"]
mark=s.place_marker((1544.81, -2624.82, -863.212), (1, 0.56872, 0.56872), 124.573)
if "particle_152 geometry" not in marker_sets:
  s=new_marker_set('particle_152 geometry')
  marker_sets["particle_152 geometry"]=s
s= marker_sets["particle_152 geometry"]
mark=s.place_marker((876.247, -2204.03, -667.611), (1, 0.559242, 0.559242), 184.342)
if "particle_153 geometry" not in marker_sets:
  s=new_marker_set('particle_153 geometry')
  marker_sets["particle_153 geometry"]=s
s= marker_sets["particle_153 geometry"]
mark=s.place_marker((333.035, -2094.46, -531.638), (1, 0.549763, 0.549763), 202.588)
if "particle_154 geometry" not in marker_sets:
  s=new_marker_set('particle_154 geometry')
  marker_sets["particle_154 geometry"]=s
s= marker_sets["particle_154 geometry"]
mark=s.place_marker((-75.6495, -2271.54, -332.354), (1, 0.540284, 0.540284), 221.463)
if "particle_155 geometry" not in marker_sets:
  s=new_marker_set('particle_155 geometry')
  marker_sets["particle_155 geometry"]=s
s= marker_sets["particle_155 geometry"]
mark=s.place_marker((-428.315, -2096.01, -178.733), (1, 0.8, 0), 134.639)
if "particle_156 geometry" not in marker_sets:
  s=new_marker_set('particle_156 geometry')
  marker_sets["particle_156 geometry"]=s
s= marker_sets["particle_156 geometry"]
mark=s.place_marker((33.2028, -2423.95, 255.966), (1, 0.521327, 0.521327), 219.727)
if "particle_157 geometry" not in marker_sets:
  s=new_marker_set('particle_157 geometry')
  marker_sets["particle_157 geometry"]=s
s= marker_sets["particle_157 geometry"]
mark=s.place_marker((494.822, -2554.68, 624.311), (1, 0.511848, 0.511848), 185.536)
if "particle_158 geometry" not in marker_sets:
  s=new_marker_set('particle_158 geometry')
  marker_sets["particle_158 geometry"]=s
s= marker_sets["particle_158 geometry"]
mark=s.place_marker((525.668, -2238.05, 998.825), (1, 0.50237, 0.50237), 191.263)
if "particle_159 geometry" not in marker_sets:
  s=new_marker_set('particle_159 geometry')
  marker_sets["particle_159 geometry"]=s
s= marker_sets["particle_159 geometry"]
mark=s.place_marker((412.449, -1764.11, 1107.7), (1, 0.492891, 0.492891), 162.496)
if "particle_160 geometry" not in marker_sets:
  s=new_marker_set('particle_160 geometry')
  marker_sets["particle_160 geometry"]=s
s= marker_sets["particle_160 geometry"]
mark=s.place_marker((465.994, -1313.11, 917.124), (1, 0.483412, 0.483412), 202.935)
if "particle_161 geometry" not in marker_sets:
  s=new_marker_set('particle_161 geometry')
  marker_sets["particle_161 geometry"]=s
s= marker_sets["particle_161 geometry"]
mark=s.place_marker((726.444, -999.323, 977.207), (1, 0.473934, 0.473934), 186.295)
if "particle_162 geometry" not in marker_sets:
  s=new_marker_set('particle_162 geometry')
  marker_sets["particle_162 geometry"]=s
s= marker_sets["particle_162 geometry"]
mark=s.place_marker((730.366, -1138.58, 1381.46), (1, 0.464455, 0.464455), 153.297)
if "particle_163 geometry" not in marker_sets:
  s=new_marker_set('particle_163 geometry')
  marker_sets["particle_163 geometry"]=s
s= marker_sets["particle_163 geometry"]
mark=s.place_marker((930.381, -1375.42, 1554.51), (1, 0.454976, 0.454976), 144.944)
if "particle_164 geometry" not in marker_sets:
  s=new_marker_set('particle_164 geometry')
  marker_sets["particle_164 geometry"]=s
s= marker_sets["particle_164 geometry"]
mark=s.place_marker((1220.73, -1563.57, 1803.14), (1, 0.445498, 0.445498), 165.489)
if "particle_165 geometry" not in marker_sets:
  s=new_marker_set('particle_165 geometry')
  marker_sets["particle_165 geometry"]=s
s= marker_sets["particle_165 geometry"]
mark=s.place_marker((1583.87, -1577.85, 1991.95), (1, 0.436019, 0.436019), 160.326)
if "particle_166 geometry" not in marker_sets:
  s=new_marker_set('particle_166 geometry')
  marker_sets["particle_166 geometry"]=s
s= marker_sets["particle_166 geometry"]
mark=s.place_marker((1153.97, -1355.24, 1802.5), (1, 0.42654, 0.42654), 168.006)
if "particle_167 geometry" not in marker_sets:
  s=new_marker_set('particle_167 geometry')
  marker_sets["particle_167 geometry"]=s
s= marker_sets["particle_167 geometry"]
mark=s.place_marker((796.892, -1628.19, 2015.96), (1, 0.417062, 0.417062), 262.423)
if "particle_168 geometry" not in marker_sets:
  s=new_marker_set('particle_168 geometry')
  marker_sets["particle_168 geometry"]=s
s= marker_sets["particle_168 geometry"]
mark=s.place_marker((1018.86, -2029.14, 2351.72), (1, 0.407583, 0.407583), 32.2822)
if "particle_169 geometry" not in marker_sets:
  s=new_marker_set('particle_169 geometry')
  marker_sets["particle_169 geometry"]=s
s= marker_sets["particle_169 geometry"]
mark=s.place_marker((1036.55, -2336.95, 2140.34), (1, 0.398104, 0.398104), 230.943)
if "particle_170 geometry" not in marker_sets:
  s=new_marker_set('particle_170 geometry')
  marker_sets["particle_170 geometry"]=s
s= marker_sets["particle_170 geometry"]
mark=s.place_marker((642.306, -2061.62, 1814.01), (1, 0.388626, 0.388626), 158.612)
if "particle_171 geometry" not in marker_sets:
  s=new_marker_set('particle_171 geometry')
  marker_sets["particle_171 geometry"]=s
s= marker_sets["particle_171 geometry"]
mark=s.place_marker((225.799, -1697, 1656.49), (1, 0.379147, 0.379147), 172.454)
if "particle_172 geometry" not in marker_sets:
  s=new_marker_set('particle_172 geometry')
  marker_sets["particle_172 geometry"]=s
s= marker_sets["particle_172 geometry"]
mark=s.place_marker((-176.729, -1437.32, 1591.19), (1, 0.369668, 0.369668), 192.153)
if "particle_173 geometry" not in marker_sets:
  s=new_marker_set('particle_173 geometry')
  marker_sets["particle_173 geometry"]=s
s= marker_sets["particle_173 geometry"]
mark=s.place_marker((-500.621, -1173.18, 1728.06), (1, 0.8, 0), 153.123)
if "particle_174 geometry" not in marker_sets:
  s=new_marker_set('particle_174 geometry')
  marker_sets["particle_174 geometry"]=s
s= marker_sets["particle_174 geometry"]
mark=s.place_marker((322.884, -1298.62, 2113.8), (1, 0.350711, 0.350711), 164.079)
if "particle_175 geometry" not in marker_sets:
  s=new_marker_set('particle_175 geometry')
  marker_sets["particle_175 geometry"]=s
s= marker_sets["particle_175 geometry"]
mark=s.place_marker((815.701, -1650.1, 2484.81), (1, 0.341232, 0.341232), 130.669)
if "particle_176 geometry" not in marker_sets:
  s=new_marker_set('particle_176 geometry')
  marker_sets["particle_176 geometry"]=s
s= marker_sets["particle_176 geometry"]
mark=s.place_marker((279.213, -1317.16, 2277.39), (1, 0.331754, 0.331754), 260.579)
if "particle_177 geometry" not in marker_sets:
  s=new_marker_set('particle_177 geometry')
  marker_sets["particle_177 geometry"]=s
s= marker_sets["particle_177 geometry"]
mark=s.place_marker((-10.1448, -804.725, 2180.23), (1, 0.322275, 0.322275), 214.737)
if "particle_178 geometry" not in marker_sets:
  s=new_marker_set('particle_178 geometry')
  marker_sets["particle_178 geometry"]=s
s= marker_sets["particle_178 geometry"]
mark=s.place_marker((471.343, -626.434, 2162.84), (1, 0.312796, 0.312796), 284.617)
if "particle_179 geometry" not in marker_sets:
  s=new_marker_set('particle_179 geometry')
  marker_sets["particle_179 geometry"]=s
s= marker_sets["particle_179 geometry"]
mark=s.place_marker((704.903, -1212.17, 2343.04), (1, 0.303318, 0.303318), 277.891)
if "particle_180 geometry" not in marker_sets:
  s=new_marker_set('particle_180 geometry')
  marker_sets["particle_180 geometry"]=s
s= marker_sets["particle_180 geometry"]
mark=s.place_marker((904.065, -1487.3, 2716.2), (1, 0.293839, 0.293839), 132.318)
if "particle_181 geometry" not in marker_sets:
  s=new_marker_set('particle_181 geometry')
  marker_sets["particle_181 geometry"]=s
s= marker_sets["particle_181 geometry"]
mark=s.place_marker((1287.5, -1476.54, 2903.79), (1, 0.28436, 0.28436), 179.917)
if "particle_182 geometry" not in marker_sets:
  s=new_marker_set('particle_182 geometry')
  marker_sets["particle_182 geometry"]=s
s= marker_sets["particle_182 geometry"]
mark=s.place_marker((1709.56, -1358.81, 2636.96), (1, 0.274882, 0.274882), 120.125)
if "particle_183 geometry" not in marker_sets:
  s=new_marker_set('particle_183 geometry')
  marker_sets["particle_183 geometry"]=s
s= marker_sets["particle_183 geometry"]
mark=s.place_marker((1525.08, -935.579, 2289.04), (1, 0.265403, 0.265403), 220.204)
if "particle_184 geometry" not in marker_sets:
  s=new_marker_set('particle_184 geometry')
  marker_sets["particle_184 geometry"]=s
s= marker_sets["particle_184 geometry"]
mark=s.place_marker((1077.36, -719.346, 2402.85), (1, 0.255924, 0.255924), 218.035)
if "particle_185 geometry" not in marker_sets:
  s=new_marker_set('particle_185 geometry')
  marker_sets["particle_185 geometry"]=s
s= marker_sets["particle_185 geometry"]
mark=s.place_marker((634.963, -802.099, 2026.72), (1, 0.246445, 0.246445), 236.063)
if "particle_186 geometry" not in marker_sets:
  s=new_marker_set('particle_186 geometry')
  marker_sets["particle_186 geometry"]=s
s= marker_sets["particle_186 geometry"]
mark=s.place_marker((593.292, -1261.13, 2140.54), (1, 0.236967, 0.236967), 157.853)
if "particle_187 geometry" not in marker_sets:
  s=new_marker_set('particle_187 geometry')
  marker_sets["particle_187 geometry"]=s
s= marker_sets["particle_187 geometry"]
mark=s.place_marker((715.091, -1472.5, 2622.31), (1, 0.227488, 0.227488), 151.735)
if "particle_188 geometry" not in marker_sets:
  s=new_marker_set('particle_188 geometry')
  marker_sets["particle_188 geometry"]=s
s= marker_sets["particle_188 geometry"]
mark=s.place_marker((963.445, -1481.01, 2467.31), (1, 0.218009, 0.218009), 132.101)
if "particle_189 geometry" not in marker_sets:
  s=new_marker_set('particle_189 geometry')
  marker_sets["particle_189 geometry"]=s
s= marker_sets["particle_189 geometry"]
mark=s.place_marker((1093.86, -1197.64, 2251.7), (1, 0.208531, 0.208531), 180.567)
if "particle_190 geometry" not in marker_sets:
  s=new_marker_set('particle_190 geometry')
  marker_sets["particle_190 geometry"]=s
s= marker_sets["particle_190 geometry"]
mark=s.place_marker((1422.81, -992.786, 1805.27), (1, 0.199052, 0.199052), 231.073)
if "particle_191 geometry" not in marker_sets:
  s=new_marker_set('particle_191 geometry')
  marker_sets["particle_191 geometry"]=s
s= marker_sets["particle_191 geometry"]
mark=s.place_marker((1907.25, -1202.54, 1509.49), (1, 0.189573, 0.189573), 173.473)
if "particle_192 geometry" not in marker_sets:
  s=new_marker_set('particle_192 geometry')
  marker_sets["particle_192 geometry"]=s
s= marker_sets["particle_192 geometry"]
mark=s.place_marker((1659.02, -1612.79, 1429.81), (1, 0.180095, 0.180095), 184.993)
if "particle_193 geometry" not in marker_sets:
  s=new_marker_set('particle_193 geometry')
  marker_sets["particle_193 geometry"]=s
s= marker_sets["particle_193 geometry"]
mark=s.place_marker((1769.66, -1911.92, 1530.54), (1, 0.170616, 0.170616), 147.396)
if "particle_194 geometry" not in marker_sets:
  s=new_marker_set('particle_194 geometry')
  marker_sets["particle_194 geometry"]=s
s= marker_sets["particle_194 geometry"]
mark=s.place_marker((2240.39, -1866.93, 1650.14), (1, 0.161137, 0.161137), 236.172)
if "particle_195 geometry" not in marker_sets:
  s=new_marker_set('particle_195 geometry')
  marker_sets["particle_195 geometry"]=s
s= marker_sets["particle_195 geometry"]
mark=s.place_marker((2436.84, -1368.06, 1656.62), (1, 0.151659, 0.151659), 146.788)
if "particle_196 geometry" not in marker_sets:
  s=new_marker_set('particle_196 geometry')
  marker_sets["particle_196 geometry"]=s
s= marker_sets["particle_196 geometry"]
mark=s.place_marker((2299.27, -859.685, 1504.61), (1, 0.14218, 0.14218), 257.758)
if "particle_197 geometry" not in marker_sets:
  s=new_marker_set('particle_197 geometry')
  marker_sets["particle_197 geometry"]=s
s= marker_sets["particle_197 geometry"]
mark=s.place_marker((1977.05, -973.307, 1990.61), (1, 0.132701, 0.132701), 215.822)
if "particle_198 geometry" not in marker_sets:
  s=new_marker_set('particle_198 geometry')
  marker_sets["particle_198 geometry"]=s
s= marker_sets["particle_198 geometry"]
mark=s.place_marker((1717.41, -1085.15, 2585.33), (1, 0.123223, 0.123223), 215.583)
if "particle_199 geometry" not in marker_sets:
  s=new_marker_set('particle_199 geometry')
  marker_sets["particle_199 geometry"]=s
s= marker_sets["particle_199 geometry"]
mark=s.place_marker((1426.28, -1109.39, 2921.95), (1, 0.113744, 0.113744), 136.961)
if "particle_200 geometry" not in marker_sets:
  s=new_marker_set('particle_200 geometry')
  marker_sets["particle_200 geometry"]=s
s= marker_sets["particle_200 geometry"]
mark=s.place_marker((1470.35, -1211.13, 2483.63), (1, 0.104265, 0.104265), 180.134)
if "particle_201 geometry" not in marker_sets:
  s=new_marker_set('particle_201 geometry')
  marker_sets["particle_201 geometry"]=s
s= marker_sets["particle_201 geometry"]
mark=s.place_marker((1794.89, -1151.83, 1963.36), (1, 0.0947867, 0.0947867), 256.869)
if "particle_202 geometry" not in marker_sets:
  s=new_marker_set('particle_202 geometry')
  marker_sets["particle_202 geometry"]=s
s= marker_sets["particle_202 geometry"]
mark=s.place_marker((2094.26, -800.341, 1468.75), (1, 0.0853081, 0.0853081), 255.155)
if "particle_203 geometry" not in marker_sets:
  s=new_marker_set('particle_203 geometry')
  marker_sets["particle_203 geometry"]=s
s= marker_sets["particle_203 geometry"]
mark=s.place_marker((2217.69, -1255.21, 1195.3), (1, 0.0758294, 0.0758294), 245.869)
if "particle_204 geometry" not in marker_sets:
  s=new_marker_set('particle_204 geometry')
  marker_sets["particle_204 geometry"]=s
s= marker_sets["particle_204 geometry"]
mark=s.place_marker((2161.06, -1763.64, 1281.12), (1, 0.0663507, 0.0663507), 188.248)
if "particle_205 geometry" not in marker_sets:
  s=new_marker_set('particle_205 geometry')
  marker_sets["particle_205 geometry"]=s
s= marker_sets["particle_205 geometry"]
mark=s.place_marker((2493.59, -1690.86, 1232.48), (1, 0.056872, 0.056872), 140.258)
if "particle_206 geometry" not in marker_sets:
  s=new_marker_set('particle_206 geometry')
  marker_sets["particle_206 geometry"]=s
s= marker_sets["particle_206 geometry"]
mark=s.place_marker((2454.9, -1222.5, 1074.23), (1, 0.0473934, 0.0473934), 254.092)
if "particle_207 geometry" not in marker_sets:
  s=new_marker_set('particle_207 geometry')
  marker_sets["particle_207 geometry"]=s
s= marker_sets["particle_207 geometry"]
mark=s.place_marker((2354.39, -804.203, 1213.79), (1, 0.0379147, 0.0379147), 135.203)
if "particle_208 geometry" not in marker_sets:
  s=new_marker_set('particle_208 geometry')
  marker_sets["particle_208 geometry"]=s
s= marker_sets["particle_208 geometry"]
mark=s.place_marker((2472.91, -1090.18, 1517.13), (1, 0.028436, 0.028436), 198.835)
if "particle_209 geometry" not in marker_sets:
  s=new_marker_set('particle_209 geometry')
  marker_sets["particle_209 geometry"]=s
s= marker_sets["particle_209 geometry"]
mark=s.place_marker((2190.6, -1530.69, 1536.51), (1, 0.0189573, 0.0189573), 231.095)
if "particle_210 geometry" not in marker_sets:
  s=new_marker_set('particle_210 geometry')
  marker_sets["particle_210 geometry"]=s
s= marker_sets["particle_210 geometry"]
mark=s.place_marker((2328.57, -2056.53, 1432.35), (1, 0.00947867, 0.00947867), 251.206)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
