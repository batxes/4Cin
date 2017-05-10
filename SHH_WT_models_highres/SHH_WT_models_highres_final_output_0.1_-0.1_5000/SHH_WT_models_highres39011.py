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
mark=s.place_marker((1717.74, 1098.19, 60.5632), (0.7, 0.7, 0.7), 182.271)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((1720.22, 929.625, -347.667), (0.7, 0.7, 0.7), 258.199)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((1700.48, 1165.82, -33.6452), (0.7, 0.7, 0.7), 123.897)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((1581.07, 1283.56, -408.81), (0.7, 0.7, 0.7), 146.739)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((1504.28, 1513.01, -804.696), (0.7, 0.7, 0.7), 179.098)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((1792.46, 1703.1, -341.216), (0.7, 0.7, 0.7), 148.854)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((2017.62, 1957.21, 38.7024), (0.7, 0.7, 0.7), 196.357)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((1651.91, 2137.81, -292.721), (0.7, 0.7, 0.7), 166.873)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((1337.66, 2395.51, -650.803), (0.7, 0.7, 0.7), 95.4711)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((1647.35, 2419.39, -369.979), (0.7, 0.7, 0.7), 185.401)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((2028.83, 2245.87, -113.059), (0.7, 0.7, 0.7), 151.984)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((2447.6, 1974.44, 250.57), (0.7, 0.7, 0.7), 185.612)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((2857.73, 1797.12, 183.974), (0.7, 0.7, 0.7), 210.273)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((3178.44, 1741.05, 8.32261), (0.7, 0.7, 0.7), 106.892)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((3660.87, 1650.77, -69.1355), (0.7, 0.7, 0.7), 202.025)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((4141.49, 1262.33, -70.7277), (0.7, 0.7, 0.7), 192.169)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((4526.94, 765.351, 2.45732), (0.7, 0.7, 0.7), 241.11)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((4598.05, 363.52, 212.038), (0.7, 0.7, 0.7), 128.465)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((4543.49, -118.749, 155.635), (0.7, 0.7, 0.7), 217.38)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((4610.88, -739.312, -174.877), (0.7, 0.7, 0.7), 184.555)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((4413.77, -289.453, 251.991), (0.7, 0.7, 0.7), 140.055)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((4590.78, 96.2548, 457.058), (0.7, 0.7, 0.7), 169.708)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((4939.46, 307.804, 637.697), (0.7, 0.7, 0.7), 184.639)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((4890.66, 351.275, 969.199), (0.7, 0.7, 0.7), 119.286)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((4773.14, 87.8042, 1085.37), (0.7, 0.7, 0.7), 147.754)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((4509.93, -23.5786, 898.849), (0.7, 0.7, 0.7), 171.4)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((4314.08, 330.039, 759.699), (0.7, 0.7, 0.7), 156.341)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((3815.58, 618.022, 894.948), (0.7, 0.7, 0.7), 186.501)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((3397.61, 924.977, 1086.57), (0.7, 0.7, 0.7), 308.325)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((3152.95, 1294.89, 993.589), (0.7, 0.7, 0.7), 138.617)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((3119.25, 1602.69, 1014.41), (0.7, 0.7, 0.7), 130.03)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((3352.21, 1388.91, 974.012), (0.7, 0.7, 0.7), 156.552)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((3159.51, 1156.15, 958.459), (0.7, 0.7, 0.7), 183.244)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((2999.51, 937.423, 964.043), (0.7, 0.7, 0.7), 181.382)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((2998.22, 783.855, 1098.36), (0.7, 0.7, 0.7), 101.943)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((2997.61, 421.559, 1064.83), (1, 0.7, 0), 138.913)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((2301.51, 782.743, 343.039), (0.7, 0.7, 0.7), 221.737)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((1562.17, 975.815, -12.5323), (0.7, 0.7, 0.7), 256.38)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((1041.87, 1252.56, 243.732), (0.7, 0.7, 0.7), 221.694)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((1237.58, 1710.86, 727.499), (0.7, 0.7, 0.7), 259.341)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((1925.05, 1998.34, 1053.72), (0.7, 0.7, 0.7), 117.89)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((2733.76, 1837.11, 1285.94), (0.7, 0.7, 0.7), 116.071)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((2862.75, 1448.27, 1551.64), (0.7, 0.7, 0.7), 268.224)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((2562.3, 1420.47, 1657.46), (0.7, 0.7, 0.7), 386.918)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((2088.59, 1817.83, 1626.15), (0.7, 0.7, 0.7), 121.316)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((1649.84, 1780.01, 1754.7), (0.7, 0.7, 0.7), 138.363)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((2023.11, 1179.06, 1696.86), (1, 0.7, 0), 175.207)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((1350.15, 1309.79, 1897.49), (0.7, 0.7, 0.7), 131.468)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((683.415, 1228.56, 2191.58), (0.7, 0.7, 0.7), 287.894)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((1146.48, 1290.98, 2457.38), (0.7, 0.7, 0.7), 88.1109)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((1725.66, 1410.76, 2333.31), (0.7, 0.7, 0.7), 145.385)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((1899.66, 1554.69, 2346.31), (0.7, 0.7, 0.7), 155.452)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((1383.32, 1633.81, 2698.38), (0.7, 0.7, 0.7), 145.512)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((974.82, 1774.71, 2967.23), (0.7, 0.7, 0.7), 99.9972)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((615.992, 1950.33, 3153.09), (0.7, 0.7, 0.7), 327.529)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((1049.06, 2372.37, 2919.4), (0.7, 0.7, 0.7), 137.983)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((1541.2, 2311.05, 2793.18), (0.7, 0.7, 0.7), 83.3733)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((2059.16, 2123.58, 2624.43), (0.7, 0.7, 0.7), 101.562)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((2453.26, 1860.86, 2390.97), (0.7, 0.7, 0.7), 165.689)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((2370.04, 1568.11, 2462.4), (0.7, 0.7, 0.7), 136.925)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((2303.8, 1471.5, 2501.31), (0.7, 0.7, 0.7), 123.389)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((2087.15, 1733.9, 2800.32), (0.7, 0.7, 0.7), 184.47)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((1733.75, 2088.22, 3423.17), (0.7, 0.7, 0.7), 148.473)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((1292.61, 2436.67, 4238.27), (0.7, 0.7, 0.7), 241.406)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((1384.49, 2623.81, 3606.82), (0.7, 0.7, 0.7), 182.736)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((1434.99, 2571.67, 3148.42), (0.7, 0.7, 0.7), 166.62)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((1545.39, 2316.28, 3112.12), (0.7, 0.7, 0.7), 113.872)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((1668, 2116.04, 2901.85), (0.7, 0.7, 0.7), 110.065)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((1649.1, 1771.41, 2731.89), (0.7, 0.7, 0.7), 150.08)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((1520.51, 1334.84, 2579.11), (0.7, 0.7, 0.7), 118.525)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((1360.82, 811.466, 2592.74), (0.7, 0.7, 0.7), 163.955)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((1227.87, 641.049, 2916.06), (0.7, 0.7, 0.7), 170.131)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((1150.1, 1218.05, 3403), (0.7, 0.7, 0.7), 78.2127)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((1061.37, 1927.36, 3821.29), (0.7, 0.7, 0.7), 251.896)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((996.722, 2588.79, 3959.43), (0.7, 0.7, 0.7), 167.55)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((1022.48, 2989.21, 3834.82), (0.7, 0.7, 0.7), 167.846)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((1226.95, 2801.21, 4253.73), (0.7, 0.7, 0.7), 259.68)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((1154.72, 2361.79, 4392.66), (0.7, 0.7, 0.7), 80.2854)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((989.704, 2366.06, 4504.19), (0.7, 0.7, 0.7), 82.4427)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((1043.58, 2502.84, 4852.88), (0.7, 0.7, 0.7), 212.811)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((1770.11, 2664.23, 4830.02), (0.7, 0.7, 0.7), 176.391)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((2258.3, 2600.83, 4283.77), (0.7, 0.7, 0.7), 99.3204)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((2473.05, 2257.85, 3831.59), (0.7, 0.7, 0.7), 166.62)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((2680.8, 2023.69, 3777.18), (0.7, 0.7, 0.7), 102.831)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((2489.36, 2338.35, 4586.17), (0.7, 0.7, 0.7), 65.0997)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((2048.46, 2498.14, 4309), (0.7, 0.7, 0.7), 92.1294)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((1784.93, 2524.19, 3777.85), (0.7, 0.7, 0.7), 194.791)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((1591.02, 2659.26, 3399.45), (0.7, 0.7, 0.7), 120.766)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((1378.09, 3060.14, 3745.98), (0.7, 0.7, 0.7), 217.803)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((1355.2, 2699.62, 3910.41), (0.7, 0.7, 0.7), 115.775)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((1312.27, 2301.9, 3783.4), (0.7, 0.7, 0.7), 115.648)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((1533.35, 2283.61, 3538.88), (0.7, 0.7, 0.7), 83.8386)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((1557.95, 2598.08, 3364.35), (0.7, 0.7, 0.7), 124.32)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((1392.18, 2871.34, 3075.75), (0.7, 0.7, 0.7), 185.993)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((816.054, 3044.95, 2946.32), (0.7, 0.7, 0.7), 238.826)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((314.667, 2897.21, 3080.54), (0.7, 0.7, 0.7), 128.465)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((611.612, 2375.81, 3316.58), (0.7, 0.7, 0.7), 203.209)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((1100.97, 2279.03, 3368.72), (0.7, 0.7, 0.7), 160.486)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((1058.44, 2610.7, 3274.59), (0.7, 0.7, 0.7), 149.277)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((632.072, 2738.17, 3599.96), (0.7, 0.7, 0.7), 35.7435)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((1360.15, 2104.42, 3385.68), (0.7, 0.7, 0.7), 98.3898)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((2221.65, 1638.54, 3045.9), (0.7, 0.7, 0.7), 188.404)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((2652.97, 1785.54, 2833.68), (0.7, 0.7, 0.7), 110.318)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((2496.67, 2021.9, 3098.46), (0.7, 0.7, 0.7), 127.534)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((2196.99, 2167.78, 3283.03), (0.7, 0.7, 0.7), 91.368)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((1824.58, 2269.49, 3375.44), (0.7, 0.7, 0.7), 131.045)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((1415.45, 2271.87, 3279.82), (0.7, 0.7, 0.7), 143.608)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((1227.77, 2554.41, 3090.07), (0.7, 0.7, 0.7), 135.783)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((1108.42, 2820.8, 2929.95), (0.7, 0.7, 0.7), 92.5947)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((1356.57, 2933.09, 2890.46), (0.7, 0.7, 0.7), 150.123)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((1600.99, 2966.82, 2974.07), (0.7, 0.7, 0.7), 121.57)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((1614.66, 3284.91, 3060.65), (0.7, 0.7, 0.7), 104.777)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((1980.15, 3171.84, 2898.3), (0.7, 0.7, 0.7), 114.844)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((2363.07, 3052.03, 2711.52), (0.7, 0.7, 0.7), 150.588)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((2488.48, 2666.8, 2795.34), (0.7, 0.7, 0.7), 103.55)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((2624.62, 2344.98, 3217.23), (0.7, 0.7, 0.7), 215.392)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((2884.92, 1985.32, 3556.62), (0.7, 0.7, 0.7), 99.9126)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((3025.54, 2000.36, 4239.16), (0.7, 0.7, 0.7), 99.7857)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((2904.11, 2000.09, 4779.01), (0.7, 0.7, 0.7), 109.98)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((2871.87, 2270.14, 4347.15), (0.7, 0.7, 0.7), 102.831)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((2671.79, 2328.07, 3992.4), (0.7, 0.7, 0.7), 103.593)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((2318.84, 2431.97, 3640.91), (0.7, 0.7, 0.7), 173.472)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((1757.46, 2581.84, 3635.32), (0.7, 0.7, 0.7), 113.575)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((1417.46, 2718.39, 3290.42), (0.7, 0.7, 0.7), 128.296)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((1117.46, 2919.13, 2974.36), (0.7, 0.7, 0.7), 145.004)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((954.853, 3106.04, 2479.41), (0.7, 0.7, 0.7), 148.261)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((483.727, 3369.8, 2119.79), (0.7, 0.7, 0.7), 127.704)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((-60.9841, 3456.6, 1899.02), (0.7, 0.7, 0.7), 129.607)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((-52.7166, 3131.45, 2249.14), (0.7, 0.7, 0.7), 139.759)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((222.92, 2691.53, 2605.82), (0.7, 0.7, 0.7), 118.567)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((456.769, 2796.93, 2929.97), (0.7, 0.7, 0.7), 136.164)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((881.485, 2835.44, 3117.75), (0.7, 0.7, 0.7), 121.655)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((1307.93, 2979.94, 3216.9), (0.7, 0.7, 0.7), 127.492)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((1493.03, 3295.8, 3479.59), (0.7, 0.7, 0.7), 138.617)
if "particle_134 geometry" not in marker_sets:
  s=new_marker_set('particle_134 geometry')
  marker_sets["particle_134 geometry"]=s
s= marker_sets["particle_134 geometry"]
mark=s.place_marker((1843.57, 3434.47, 3420.31), (0.7, 0.7, 0.7), 120.766)
if "particle_135 geometry" not in marker_sets:
  s=new_marker_set('particle_135 geometry')
  marker_sets["particle_135 geometry"]=s
s= marker_sets["particle_135 geometry"]
mark=s.place_marker((2097.7, 3272.24, 3467.05), (0.7, 0.7, 0.7), 145.893)
if "particle_136 geometry" not in marker_sets:
  s=new_marker_set('particle_136 geometry')
  marker_sets["particle_136 geometry"]=s
s= marker_sets["particle_136 geometry"]
mark=s.place_marker((2013.24, 2858.36, 3265.23), (0.7, 0.7, 0.7), 185.02)
if "particle_137 geometry" not in marker_sets:
  s=new_marker_set('particle_137 geometry')
  marker_sets["particle_137 geometry"]=s
s= marker_sets["particle_137 geometry"]
mark=s.place_marker((2184.14, 2495.75, 2913.53), (0.7, 0.7, 0.7), 221.314)
if "particle_138 geometry" not in marker_sets:
  s=new_marker_set('particle_138 geometry')
  marker_sets["particle_138 geometry"]=s
s= marker_sets["particle_138 geometry"]
mark=s.place_marker((2405.16, 2368.35, 2480.76), (0.7, 0.7, 0.7), 165.139)
if "particle_139 geometry" not in marker_sets:
  s=new_marker_set('particle_139 geometry')
  marker_sets["particle_139 geometry"]=s
s= marker_sets["particle_139 geometry"]
mark=s.place_marker((2236.91, 2386.32, 2238.05), (0.7, 0.7, 0.7), 179.437)
if "particle_140 geometry" not in marker_sets:
  s=new_marker_set('particle_140 geometry')
  marker_sets["particle_140 geometry"]=s
s= marker_sets["particle_140 geometry"]
mark=s.place_marker((2055.72, 2370.27, 2613.79), (0.7, 0.7, 0.7), 137.898)
if "particle_141 geometry" not in marker_sets:
  s=new_marker_set('particle_141 geometry')
  marker_sets["particle_141 geometry"]=s
s= marker_sets["particle_141 geometry"]
mark=s.place_marker((1817.75, 2359.55, 2899.19), (0.7, 0.7, 0.7), 124.658)
if "particle_142 geometry" not in marker_sets:
  s=new_marker_set('particle_142 geometry')
  marker_sets["particle_142 geometry"]=s
s= marker_sets["particle_142 geometry"]
mark=s.place_marker((1772.57, 2647.15, 3030.41), (0.7, 0.7, 0.7), 97.7553)
if "particle_143 geometry" not in marker_sets:
  s=new_marker_set('particle_143 geometry')
  marker_sets["particle_143 geometry"]=s
s= marker_sets["particle_143 geometry"]
mark=s.place_marker((1775.33, 2850.62, 3269.25), (0.7, 0.7, 0.7), 92.9331)
if "particle_144 geometry" not in marker_sets:
  s=new_marker_set('particle_144 geometry')
  marker_sets["particle_144 geometry"]=s
s= marker_sets["particle_144 geometry"]
mark=s.place_marker((1723.09, 2987.51, 3618.11), (0.7, 0.7, 0.7), 123.135)
if "particle_145 geometry" not in marker_sets:
  s=new_marker_set('particle_145 geometry')
  marker_sets["particle_145 geometry"]=s
s= marker_sets["particle_145 geometry"]
mark=s.place_marker((1916.86, 2663.33, 3434.8), (0.7, 0.7, 0.7), 125.716)
if "particle_146 geometry" not in marker_sets:
  s=new_marker_set('particle_146 geometry')
  marker_sets["particle_146 geometry"]=s
s= marker_sets["particle_146 geometry"]
mark=s.place_marker((2072.9, 2541.72, 3194.61), (0.7, 0.7, 0.7), 127.534)
if "particle_147 geometry" not in marker_sets:
  s=new_marker_set('particle_147 geometry')
  marker_sets["particle_147 geometry"]=s
s= marker_sets["particle_147 geometry"]
mark=s.place_marker((1860.45, 2656.19, 3088.98), (0.7, 0.7, 0.7), 94.9212)
if "particle_148 geometry" not in marker_sets:
  s=new_marker_set('particle_148 geometry')
  marker_sets["particle_148 geometry"]=s
s= marker_sets["particle_148 geometry"]
mark=s.place_marker((2023.08, 2439.06, 2754.97), (0.7, 0.7, 0.7), 137.644)
if "particle_149 geometry" not in marker_sets:
  s=new_marker_set('particle_149 geometry')
  marker_sets["particle_149 geometry"]=s
s= marker_sets["particle_149 geometry"]
mark=s.place_marker((2073.44, 2356.97, 2429.74), (0.7, 0.7, 0.7), 149.277)
if "particle_150 geometry" not in marker_sets:
  s=new_marker_set('particle_150 geometry')
  marker_sets["particle_150 geometry"]=s
s= marker_sets["particle_150 geometry"]
mark=s.place_marker((2218.11, 2670.23, 2463.87), (0.7, 0.7, 0.7), 103.677)
if "particle_151 geometry" not in marker_sets:
  s=new_marker_set('particle_151 geometry')
  marker_sets["particle_151 geometry"]=s
s= marker_sets["particle_151 geometry"]
mark=s.place_marker((2183.34, 3138.7, 2574.32), (0.7, 0.7, 0.7), 99.6588)
if "particle_152 geometry" not in marker_sets:
  s=new_marker_set('particle_152 geometry')
  marker_sets["particle_152 geometry"]=s
s= marker_sets["particle_152 geometry"]
mark=s.place_marker((2139.81, 3502.86, 2625.76), (0.7, 0.7, 0.7), 134.133)
if "particle_153 geometry" not in marker_sets:
  s=new_marker_set('particle_153 geometry')
  marker_sets["particle_153 geometry"]=s
s= marker_sets["particle_153 geometry"]
mark=s.place_marker((2381.82, 3293.59, 2732.06), (0.7, 0.7, 0.7), 173.007)
if "particle_154 geometry" not in marker_sets:
  s=new_marker_set('particle_154 geometry')
  marker_sets["particle_154 geometry"]=s
s= marker_sets["particle_154 geometry"]
mark=s.place_marker((2502.88, 2764.56, 2551.19), (0.7, 0.7, 0.7), 141.028)
if "particle_155 geometry" not in marker_sets:
  s=new_marker_set('particle_155 geometry')
  marker_sets["particle_155 geometry"]=s
s= marker_sets["particle_155 geometry"]
mark=s.place_marker((2539.13, 2298.22, 2487.28), (0.7, 0.7, 0.7), 161.121)
if "particle_156 geometry" not in marker_sets:
  s=new_marker_set('particle_156 geometry')
  marker_sets["particle_156 geometry"]=s
s= marker_sets["particle_156 geometry"]
mark=s.place_marker((2232.16, 2134.72, 2538.55), (0.7, 0.7, 0.7), 119.582)
if "particle_157 geometry" not in marker_sets:
  s=new_marker_set('particle_157 geometry')
  marker_sets["particle_157 geometry"]=s
s= marker_sets["particle_157 geometry"]
mark=s.place_marker((2017.5, 2337.39, 2817.56), (0.7, 0.7, 0.7), 137.094)
if "particle_158 geometry" not in marker_sets:
  s=new_marker_set('particle_158 geometry')
  marker_sets["particle_158 geometry"]=s
s= marker_sets["particle_158 geometry"]
mark=s.place_marker((1900.29, 2486.89, 3280.77), (0.7, 0.7, 0.7), 149.234)
if "particle_159 geometry" not in marker_sets:
  s=new_marker_set('particle_159 geometry')
  marker_sets["particle_159 geometry"]=s
s= marker_sets["particle_159 geometry"]
mark=s.place_marker((2144.38, 2191.02, 3485.81), (0.7, 0.7, 0.7), 151.011)
if "particle_160 geometry" not in marker_sets:
  s=new_marker_set('particle_160 geometry')
  marker_sets["particle_160 geometry"]=s
s= marker_sets["particle_160 geometry"]
mark=s.place_marker((2550.15, 1902.58, 3342.28), (0.7, 0.7, 0.7), 184.216)
if "particle_161 geometry" not in marker_sets:
  s=new_marker_set('particle_161 geometry')
  marker_sets["particle_161 geometry"]=s
s= marker_sets["particle_161 geometry"]
mark=s.place_marker((2837.61, 2178.82, 3271.14), (0.7, 0.7, 0.7), 170.596)
if "particle_162 geometry" not in marker_sets:
  s=new_marker_set('particle_162 geometry')
  marker_sets["particle_162 geometry"]=s
s= marker_sets["particle_162 geometry"]
mark=s.place_marker((2643.76, 2567.55, 3745.04), (0.7, 0.7, 0.7), 215.603)
if "particle_163 geometry" not in marker_sets:
  s=new_marker_set('particle_163 geometry')
  marker_sets["particle_163 geometry"]=s
s= marker_sets["particle_163 geometry"]
mark=s.place_marker((2355.28, 3055.89, 4443.2), (0.7, 0.7, 0.7), 79.0164)
if "particle_164 geometry" not in marker_sets:
  s=new_marker_set('particle_164 geometry')
  marker_sets["particle_164 geometry"]=s
s= marker_sets["particle_164 geometry"]
mark=s.place_marker((2402.93, 3385.72, 4345.56), (0.7, 0.7, 0.7), 77.2821)
if "particle_165 geometry" not in marker_sets:
  s=new_marker_set('particle_165 geometry')
  marker_sets["particle_165 geometry"]=s
s= marker_sets["particle_165 geometry"]
mark=s.place_marker((2388.18, 3433.61, 3995.08), (0.7, 0.7, 0.7), 188.658)
if "particle_166 geometry" not in marker_sets:
  s=new_marker_set('particle_166 geometry')
  marker_sets["particle_166 geometry"]=s
s= marker_sets["particle_166 geometry"]
mark=s.place_marker((2700.32, 3518.09, 3944.77), (0.7, 0.7, 0.7), 115.437)
if "particle_167 geometry" not in marker_sets:
  s=new_marker_set('particle_167 geometry')
  marker_sets["particle_167 geometry"]=s
s= marker_sets["particle_167 geometry"]
mark=s.place_marker((2672.57, 3043, 3570.88), (0.7, 0.7, 0.7), 88.4916)
if "particle_168 geometry" not in marker_sets:
  s=new_marker_set('particle_168 geometry')
  marker_sets["particle_168 geometry"]=s
s= marker_sets["particle_168 geometry"]
mark=s.place_marker((2613.83, 2546.26, 3185.05), (0.7, 0.7, 0.7), 108.88)
if "particle_169 geometry" not in marker_sets:
  s=new_marker_set('particle_169 geometry')
  marker_sets["particle_169 geometry"]=s
s= marker_sets["particle_169 geometry"]
mark=s.place_marker((2503.49, 2207.05, 3119.92), (0.7, 0.7, 0.7), 172.119)
if "particle_170 geometry" not in marker_sets:
  s=new_marker_set('particle_170 geometry')
  marker_sets["particle_170 geometry"]=s
s= marker_sets["particle_170 geometry"]
mark=s.place_marker((2467.03, 2455.59, 3532.33), (0.7, 0.7, 0.7), 139.505)
if "particle_171 geometry" not in marker_sets:
  s=new_marker_set('particle_171 geometry')
  marker_sets["particle_171 geometry"]=s
s= marker_sets["particle_171 geometry"]
mark=s.place_marker((2427.51, 2701.77, 3956.99), (0.7, 0.7, 0.7), 92.7639)
if "particle_172 geometry" not in marker_sets:
  s=new_marker_set('particle_172 geometry')
  marker_sets["particle_172 geometry"]=s
s= marker_sets["particle_172 geometry"]
mark=s.place_marker((2435.44, 2466.48, 4032.54), (0.7, 0.7, 0.7), 89.8452)
if "particle_173 geometry" not in marker_sets:
  s=new_marker_set('particle_173 geometry')
  marker_sets["particle_173 geometry"]=s
s= marker_sets["particle_173 geometry"]
mark=s.place_marker((2700.76, 2546.33, 3928.96), (0.7, 0.7, 0.7), 149.446)
if "particle_174 geometry" not in marker_sets:
  s=new_marker_set('particle_174 geometry')
  marker_sets["particle_174 geometry"]=s
s= marker_sets["particle_174 geometry"]
mark=s.place_marker((2965.56, 2735.24, 3997.49), (0.7, 0.7, 0.7), 126.858)
if "particle_175 geometry" not in marker_sets:
  s=new_marker_set('particle_175 geometry')
  marker_sets["particle_175 geometry"]=s
s= marker_sets["particle_175 geometry"]
mark=s.place_marker((2697.65, 2857.88, 4197.34), (0.7, 0.7, 0.7), 106.046)
if "particle_176 geometry" not in marker_sets:
  s=new_marker_set('particle_176 geometry')
  marker_sets["particle_176 geometry"]=s
s= marker_sets["particle_176 geometry"]
mark=s.place_marker((2228.26, 2642.27, 4305.5), (0.7, 0.7, 0.7), 156.298)
if "particle_177 geometry" not in marker_sets:
  s=new_marker_set('particle_177 geometry')
  marker_sets["particle_177 geometry"]=s
s= marker_sets["particle_177 geometry"]
mark=s.place_marker((1648.4, 2431.28, 4353.81), (0.7, 0.7, 0.7), 231.212)
if "particle_178 geometry" not in marker_sets:
  s=new_marker_set('particle_178 geometry')
  marker_sets["particle_178 geometry"]=s
s= marker_sets["particle_178 geometry"]
mark=s.place_marker((1492.38, 1927.78, 4114.37), (0.7, 0.7, 0.7), 88.4916)
if "particle_179 geometry" not in marker_sets:
  s=new_marker_set('particle_179 geometry')
  marker_sets["particle_179 geometry"]=s
s= marker_sets["particle_179 geometry"]
mark=s.place_marker((1697.94, 1676.1, 3754), (0.7, 0.7, 0.7), 111.334)
if "particle_180 geometry" not in marker_sets:
  s=new_marker_set('particle_180 geometry')
  marker_sets["particle_180 geometry"]=s
s= marker_sets["particle_180 geometry"]
mark=s.place_marker((2151.57, 1738.78, 3349.61), (0.7, 0.7, 0.7), 127.619)
if "particle_181 geometry" not in marker_sets:
  s=new_marker_set('particle_181 geometry')
  marker_sets["particle_181 geometry"]=s
s= marker_sets["particle_181 geometry"]
mark=s.place_marker((2465.34, 1832.28, 3040.13), (0.7, 0.7, 0.7), 230.746)
if "particle_182 geometry" not in marker_sets:
  s=new_marker_set('particle_182 geometry')
  marker_sets["particle_182 geometry"]=s
s= marker_sets["particle_182 geometry"]
mark=s.place_marker((2337.5, 2083.01, 3331.67), (0.7, 0.7, 0.7), 124.573)
if "particle_183 geometry" not in marker_sets:
  s=new_marker_set('particle_183 geometry')
  marker_sets["particle_183 geometry"]=s
s= marker_sets["particle_183 geometry"]
mark=s.place_marker((2189.89, 2320.65, 3896.05), (0.7, 0.7, 0.7), 124.489)
if "particle_184 geometry" not in marker_sets:
  s=new_marker_set('particle_184 geometry')
  marker_sets["particle_184 geometry"]=s
s= marker_sets["particle_184 geometry"]
mark=s.place_marker((2378.4, 2627.41, 4026.56), (0.7, 0.7, 0.7), 196.61)
if "particle_185 geometry" not in marker_sets:
  s=new_marker_set('particle_185 geometry')
  marker_sets["particle_185 geometry"]=s
s= marker_sets["particle_185 geometry"]
mark=s.place_marker((2650.71, 2386.94, 4010.6), (0.7, 0.7, 0.7), 134.049)
if "particle_186 geometry" not in marker_sets:
  s=new_marker_set('particle_186 geometry')
  marker_sets["particle_186 geometry"]=s
s= marker_sets["particle_186 geometry"]
mark=s.place_marker((2766.41, 2108.39, 4170.37), (0.7, 0.7, 0.7), 141.493)
if "particle_187 geometry" not in marker_sets:
  s=new_marker_set('particle_187 geometry')
  marker_sets["particle_187 geometry"]=s
s= marker_sets["particle_187 geometry"]
mark=s.place_marker((2824.4, 1884.35, 4530.69), (0.7, 0.7, 0.7), 172.203)
if "particle_188 geometry" not in marker_sets:
  s=new_marker_set('particle_188 geometry')
  marker_sets["particle_188 geometry"]=s
s= marker_sets["particle_188 geometry"]
mark=s.place_marker((2999.45, 2326.11, 4123.24), (0.7, 0.7, 0.7), 271.354)
if "particle_189 geometry" not in marker_sets:
  s=new_marker_set('particle_189 geometry')
  marker_sets["particle_189 geometry"]=s
s= marker_sets["particle_189 geometry"]
mark=s.place_marker((2761.24, 2652.67, 3837.76), (0.7, 0.7, 0.7), 97.0785)
if "particle_190 geometry" not in marker_sets:
  s=new_marker_set('particle_190 geometry')
  marker_sets["particle_190 geometry"]=s
s= marker_sets["particle_190 geometry"]
mark=s.place_marker((2487.6, 2916.77, 3741.16), (0.7, 0.7, 0.7), 151.857)
if "particle_191 geometry" not in marker_sets:
  s=new_marker_set('particle_191 geometry')
  marker_sets["particle_191 geometry"]=s
s= marker_sets["particle_191 geometry"]
mark=s.place_marker((2251.62, 3367.94, 3458.36), (0.7, 0.7, 0.7), 199.233)
if "particle_192 geometry" not in marker_sets:
  s=new_marker_set('particle_192 geometry')
  marker_sets["particle_192 geometry"]=s
s= marker_sets["particle_192 geometry"]
mark=s.place_marker((2342.79, 3332.49, 2869.33), (0.7, 0.7, 0.7), 118.863)
if "particle_193 geometry" not in marker_sets:
  s=new_marker_set('particle_193 geometry')
  marker_sets["particle_193 geometry"]=s
s= marker_sets["particle_193 geometry"]
mark=s.place_marker((2003.87, 3410.83, 2544.47), (0.7, 0.7, 0.7), 172.415)
if "particle_194 geometry" not in marker_sets:
  s=new_marker_set('particle_194 geometry')
  marker_sets["particle_194 geometry"]=s
s= marker_sets["particle_194 geometry"]
mark=s.place_marker((1526.8, 3718.22, 2449.92), (0.7, 0.7, 0.7), 134.26)
if "particle_195 geometry" not in marker_sets:
  s=new_marker_set('particle_195 geometry')
  marker_sets["particle_195 geometry"]=s
s= marker_sets["particle_195 geometry"]
mark=s.place_marker((841.433, 4385.46, 2529.04), (0.7, 0.7, 0.7), 139.548)
if "particle_196 geometry" not in marker_sets:
  s=new_marker_set('particle_196 geometry')
  marker_sets["particle_196 geometry"]=s
s= marker_sets["particle_196 geometry"]
mark=s.place_marker((583.136, 4032.76, 2817.54), (0.7, 0.7, 0.7), 196.526)
if "particle_197 geometry" not in marker_sets:
  s=new_marker_set('particle_197 geometry')
  marker_sets["particle_197 geometry"]=s
s= marker_sets["particle_197 geometry"]
mark=s.place_marker((906.608, 3403.64, 3103.89), (0.7, 0.7, 0.7), 136.206)
if "particle_198 geometry" not in marker_sets:
  s=new_marker_set('particle_198 geometry')
  marker_sets["particle_198 geometry"]=s
s= marker_sets["particle_198 geometry"]
mark=s.place_marker((1455.35, 2606.75, 2975.34), (0.7, 0.7, 0.7), 152.322)
if "particle_199 geometry" not in marker_sets:
  s=new_marker_set('particle_199 geometry')
  marker_sets["particle_199 geometry"]=s
s= marker_sets["particle_199 geometry"]
mark=s.place_marker((1950.5, 2187.44, 2887.97), (0.7, 0.7, 0.7), 126.054)
if "particle_200 geometry" not in marker_sets:
  s=new_marker_set('particle_200 geometry')
  marker_sets["particle_200 geometry"]=s
s= marker_sets["particle_200 geometry"]
mark=s.place_marker((2139.06, 2213.75, 3289.18), (0.7, 0.7, 0.7), 164.378)
if "particle_201 geometry" not in marker_sets:
  s=new_marker_set('particle_201 geometry')
  marker_sets["particle_201 geometry"]=s
s= marker_sets["particle_201 geometry"]
mark=s.place_marker((2354.39, 2459.35, 3623.92), (0.7, 0.7, 0.7), 122.205)
if "particle_202 geometry" not in marker_sets:
  s=new_marker_set('particle_202 geometry')
  marker_sets["particle_202 geometry"]=s
s= marker_sets["particle_202 geometry"]
mark=s.place_marker((2609.53, 2780.28, 3786.74), (0.7, 0.7, 0.7), 134.979)
if "particle_203 geometry" not in marker_sets:
  s=new_marker_set('particle_203 geometry')
  marker_sets["particle_203 geometry"]=s
s= marker_sets["particle_203 geometry"]
mark=s.place_marker((2745.08, 2874.2, 3455.71), (0.7, 0.7, 0.7), 136.375)
if "particle_204 geometry" not in marker_sets:
  s=new_marker_set('particle_204 geometry')
  marker_sets["particle_204 geometry"]=s
s= marker_sets["particle_204 geometry"]
mark=s.place_marker((2452.21, 2920.15, 3528.52), (0.7, 0.7, 0.7), 151.688)
if "particle_205 geometry" not in marker_sets:
  s=new_marker_set('particle_205 geometry')
  marker_sets["particle_205 geometry"]=s
s= marker_sets["particle_205 geometry"]
mark=s.place_marker((2304.6, 2961.98, 3620.68), (0.7, 0.7, 0.7), 116.156)
if "particle_206 geometry" not in marker_sets:
  s=new_marker_set('particle_206 geometry')
  marker_sets["particle_206 geometry"]=s
s= marker_sets["particle_206 geometry"]
mark=s.place_marker((2465.08, 2569.48, 3046.2), (0.7, 0.7, 0.7), 122.839)
if "particle_207 geometry" not in marker_sets:
  s=new_marker_set('particle_207 geometry')
  marker_sets["particle_207 geometry"]=s
s= marker_sets["particle_207 geometry"]
mark=s.place_marker((2388.83, 2254.26, 2708.96), (0.7, 0.7, 0.7), 164.716)
if "particle_208 geometry" not in marker_sets:
  s=new_marker_set('particle_208 geometry')
  marker_sets["particle_208 geometry"]=s
s= marker_sets["particle_208 geometry"]
mark=s.place_marker((1713.03, 2522.9, 3175.02), (0.7, 0.7, 0.7), 303.672)
if "particle_209 geometry" not in marker_sets:
  s=new_marker_set('particle_209 geometry')
  marker_sets["particle_209 geometry"]=s
s= marker_sets["particle_209 geometry"]
mark=s.place_marker((1279.39, 3300.96, 3781.84), (0.7, 0.7, 0.7), 220.298)
if "particle_210 geometry" not in marker_sets:
  s=new_marker_set('particle_210 geometry')
  marker_sets["particle_210 geometry"]=s
s= marker_sets["particle_210 geometry"]
mark=s.place_marker((1852.35, 3298.93, 4082.92), (0.7, 0.7, 0.7), 175.883)
if "particle_211 geometry" not in marker_sets:
  s=new_marker_set('particle_211 geometry')
  marker_sets["particle_211 geometry"]=s
s= marker_sets["particle_211 geometry"]
mark=s.place_marker((2319.59, 2916.06, 4441.23), (0.7, 0.7, 0.7), 233.581)
if "particle_212 geometry" not in marker_sets:
  s=new_marker_set('particle_212 geometry')
  marker_sets["particle_212 geometry"]=s
s= marker_sets["particle_212 geometry"]
mark=s.place_marker((2436.08, 2135.35, 4514.7), (0.7, 0.7, 0.7), 231.127)
if "particle_213 geometry" not in marker_sets:
  s=new_marker_set('particle_213 geometry')
  marker_sets["particle_213 geometry"]=s
s= marker_sets["particle_213 geometry"]
mark=s.place_marker((2922.83, 1763.8, 4642.55), (0.7, 0.7, 0.7), 247.413)
if "particle_214 geometry" not in marker_sets:
  s=new_marker_set('particle_214 geometry')
  marker_sets["particle_214 geometry"]=s
s= marker_sets["particle_214 geometry"]
mark=s.place_marker((3546.38, 1837.92, 4785.65), (0.7, 0.7, 0.7), 200.206)
if "particle_215 geometry" not in marker_sets:
  s=new_marker_set('particle_215 geometry')
  marker_sets["particle_215 geometry"]=s
s= marker_sets["particle_215 geometry"]
mark=s.place_marker((3686.43, 2252.91, 4757.14), (0.7, 0.7, 0.7), 150.419)
if "particle_216 geometry" not in marker_sets:
  s=new_marker_set('particle_216 geometry')
  marker_sets["particle_216 geometry"]=s
s= marker_sets["particle_216 geometry"]
mark=s.place_marker((3525, 1992.22, 4232.9), (0.7, 0.7, 0.7), 140.14)
if "particle_217 geometry" not in marker_sets:
  s=new_marker_set('particle_217 geometry')
  marker_sets["particle_217 geometry"]=s
s= marker_sets["particle_217 geometry"]
mark=s.place_marker((3406.75, 1603.75, 4037.58), (0.7, 0.7, 0.7), 132.949)
if "particle_218 geometry" not in marker_sets:
  s=new_marker_set('particle_218 geometry')
  marker_sets["particle_218 geometry"]=s
s= marker_sets["particle_218 geometry"]
mark=s.place_marker((3270.83, 1390.92, 3742.26), (0.7, 0.7, 0.7), 141.113)
if "particle_219 geometry" not in marker_sets:
  s=new_marker_set('particle_219 geometry')
  marker_sets["particle_219 geometry"]=s
s= marker_sets["particle_219 geometry"]
mark=s.place_marker((2925.11, 1373.14, 3845.82), (0.7, 0.7, 0.7), 171.526)
if "particle_220 geometry" not in marker_sets:
  s=new_marker_set('particle_220 geometry')
  marker_sets["particle_220 geometry"]=s
s= marker_sets["particle_220 geometry"]
mark=s.place_marker((2555.54, 1641.19, 4251.86), (0.7, 0.7, 0.7), 326.937)
if "particle_221 geometry" not in marker_sets:
  s=new_marker_set('particle_221 geometry')
  marker_sets["particle_221 geometry"]=s
s= marker_sets["particle_221 geometry"]
mark=s.place_marker((2291.92, 2163.98, 4325.01), (0.7, 0.7, 0.7), 92.0871)
if "particle_222 geometry" not in marker_sets:
  s=new_marker_set('particle_222 geometry')
  marker_sets["particle_222 geometry"]=s
s= marker_sets["particle_222 geometry"]
mark=s.place_marker((2045.14, 2199.71, 3917.5), (0.7, 0.7, 0.7), 210.273)
if "particle_223 geometry" not in marker_sets:
  s=new_marker_set('particle_223 geometry')
  marker_sets["particle_223 geometry"]=s
s= marker_sets["particle_223 geometry"]
mark=s.place_marker((2261.49, 1866.17, 3272.28), (0.7, 0.7, 0.7), 122.628)
if "particle_224 geometry" not in marker_sets:
  s=new_marker_set('particle_224 geometry')
  marker_sets["particle_224 geometry"]=s
s= marker_sets["particle_224 geometry"]
mark=s.place_marker((2404.04, 1702.71, 3133.33), (0.7, 0.7, 0.7), 109.176)
if "particle_225 geometry" not in marker_sets:
  s=new_marker_set('particle_225 geometry')
  marker_sets["particle_225 geometry"]=s
s= marker_sets["particle_225 geometry"]
mark=s.place_marker((2480.39, 1884.05, 3360.73), (0.7, 0.7, 0.7), 142.213)
if "particle_226 geometry" not in marker_sets:
  s=new_marker_set('particle_226 geometry')
  marker_sets["particle_226 geometry"]=s
s= marker_sets["particle_226 geometry"]
mark=s.place_marker((2126.42, 2041.41, 3462.84), (0.7, 0.7, 0.7), 250.078)
if "particle_227 geometry" not in marker_sets:
  s=new_marker_set('particle_227 geometry')
  marker_sets["particle_227 geometry"]=s
s= marker_sets["particle_227 geometry"]
mark=s.place_marker((2387.14, 2388.91, 3316.84), (0.7, 0.7, 0.7), 123.558)
if "particle_228 geometry" not in marker_sets:
  s=new_marker_set('particle_228 geometry')
  marker_sets["particle_228 geometry"]=s
s= marker_sets["particle_228 geometry"]
mark=s.place_marker((2713.46, 2478.71, 2978.8), (0.7, 0.7, 0.7), 235.992)
if "particle_229 geometry" not in marker_sets:
  s=new_marker_set('particle_229 geometry')
  marker_sets["particle_229 geometry"]=s
s= marker_sets["particle_229 geometry"]
mark=s.place_marker((2994.15, 2728.27, 2665.04), (0.7, 0.7, 0.7), 172.373)
if "particle_230 geometry" not in marker_sets:
  s=new_marker_set('particle_230 geometry')
  marker_sets["particle_230 geometry"]=s
s= marker_sets["particle_230 geometry"]
mark=s.place_marker((3032.19, 3171.24, 2771.54), (0.7, 0.7, 0.7), 152.322)
if "particle_231 geometry" not in marker_sets:
  s=new_marker_set('particle_231 geometry')
  marker_sets["particle_231 geometry"]=s
s= marker_sets["particle_231 geometry"]
mark=s.place_marker((3151.77, 3388.17, 2990.95), (0.7, 0.7, 0.7), 196.653)
if "particle_232 geometry" not in marker_sets:
  s=new_marker_set('particle_232 geometry')
  marker_sets["particle_232 geometry"]=s
s= marker_sets["particle_232 geometry"]
mark=s.place_marker((3398.75, 3147.76, 2954.23), (0.7, 0.7, 0.7), 134.091)
if "particle_233 geometry" not in marker_sets:
  s=new_marker_set('particle_233 geometry')
  marker_sets["particle_233 geometry"]=s
s= marker_sets["particle_233 geometry"]
mark=s.place_marker((3597.77, 2912.7, 2859.64), (0.7, 0.7, 0.7), 180.325)
if "particle_234 geometry" not in marker_sets:
  s=new_marker_set('particle_234 geometry')
  marker_sets["particle_234 geometry"]=s
s= marker_sets["particle_234 geometry"]
mark=s.place_marker((3151.26, 2797.05, 2861.04), (0.7, 0.7, 0.7), 218.437)
if "particle_235 geometry" not in marker_sets:
  s=new_marker_set('particle_235 geometry')
  marker_sets["particle_235 geometry"]=s
s= marker_sets["particle_235 geometry"]
mark=s.place_marker((2804.63, 2771.34, 3176.3), (0.7, 0.7, 0.7), 148.008)
if "particle_236 geometry" not in marker_sets:
  s=new_marker_set('particle_236 geometry')
  marker_sets["particle_236 geometry"]=s
s= marker_sets["particle_236 geometry"]
mark=s.place_marker((2664.72, 2947.52, 3773.1), (0.7, 0.7, 0.7), 191.873)
if "particle_237 geometry" not in marker_sets:
  s=new_marker_set('particle_237 geometry')
  marker_sets["particle_237 geometry"]=s
s= marker_sets["particle_237 geometry"]
mark=s.place_marker((2700.3, 2875.93, 4313.22), (0.7, 0.7, 0.7), 138.575)
if "particle_238 geometry" not in marker_sets:
  s=new_marker_set('particle_238 geometry')
  marker_sets["particle_238 geometry"]=s
s= marker_sets["particle_238 geometry"]
mark=s.place_marker((2973.08, 3098.18, 4554.52), (0.7, 0.7, 0.7), 161.205)
if "particle_239 geometry" not in marker_sets:
  s=new_marker_set('particle_239 geometry')
  marker_sets["particle_239 geometry"]=s
s= marker_sets["particle_239 geometry"]
mark=s.place_marker((2660.95, 3219.97, 4217.4), (0.7, 0.7, 0.7), 288.021)
if "particle_240 geometry" not in marker_sets:
  s=new_marker_set('particle_240 geometry')
  marker_sets["particle_240 geometry"]=s
s= marker_sets["particle_240 geometry"]
mark=s.place_marker((3043.68, 3207.98, 3619.67), (0.7, 0.7, 0.7), 227.405)
if "particle_241 geometry" not in marker_sets:
  s=new_marker_set('particle_241 geometry')
  marker_sets["particle_241 geometry"]=s
s= marker_sets["particle_241 geometry"]
mark=s.place_marker((3084.27, 3084.29, 3114.12), (0.7, 0.7, 0.7), 126.519)
if "particle_242 geometry" not in marker_sets:
  s=new_marker_set('particle_242 geometry')
  marker_sets["particle_242 geometry"]=s
s= marker_sets["particle_242 geometry"]
mark=s.place_marker((2938.92, 3350.56, 3174.7), (0.7, 0.7, 0.7), 117.975)
if "particle_243 geometry" not in marker_sets:
  s=new_marker_set('particle_243 geometry')
  marker_sets["particle_243 geometry"]=s
s= marker_sets["particle_243 geometry"]
mark=s.place_marker((2749.04, 3042.13, 2995.38), (0.7, 0.7, 0.7), 200.883)
if "particle_244 geometry" not in marker_sets:
  s=new_marker_set('particle_244 geometry')
  marker_sets["particle_244 geometry"]=s
s= marker_sets["particle_244 geometry"]
mark=s.place_marker((2998.92, 2775.88, 2903.76), (0.7, 0.7, 0.7), 158.794)
if "particle_245 geometry" not in marker_sets:
  s=new_marker_set('particle_245 geometry')
  marker_sets["particle_245 geometry"]=s
s= marker_sets["particle_245 geometry"]
mark=s.place_marker((3226.54, 2570.85, 2996.53), (0.7, 0.7, 0.7), 115.86)
if "particle_246 geometry" not in marker_sets:
  s=new_marker_set('particle_246 geometry')
  marker_sets["particle_246 geometry"]=s
s= marker_sets["particle_246 geometry"]
mark=s.place_marker((3248.01, 2410.3, 2816.65), (0.7, 0.7, 0.7), 133.034)
if "particle_247 geometry" not in marker_sets:
  s=new_marker_set('particle_247 geometry')
  marker_sets["particle_247 geometry"]=s
s= marker_sets["particle_247 geometry"]
mark=s.place_marker((3091.75, 2583.45, 2401.14), (0.7, 0.7, 0.7), 314.627)
if "particle_248 geometry" not in marker_sets:
  s=new_marker_set('particle_248 geometry')
  marker_sets["particle_248 geometry"]=s
s= marker_sets["particle_248 geometry"]
mark=s.place_marker((2957.51, 2841.35, 2629.16), (0.7, 0.7, 0.7), 115.352)
if "particle_249 geometry" not in marker_sets:
  s=new_marker_set('particle_249 geometry')
  marker_sets["particle_249 geometry"]=s
s= marker_sets["particle_249 geometry"]
mark=s.place_marker((3031.27, 2988.28, 3017.27), (0.7, 0.7, 0.7), 180.621)
if "particle_250 geometry" not in marker_sets:
  s=new_marker_set('particle_250 geometry')
  marker_sets["particle_250 geometry"]=s
s= marker_sets["particle_250 geometry"]
mark=s.place_marker((3230.54, 2736.85, 3175.86), (0.7, 0.7, 0.7), 126.265)
if "particle_251 geometry" not in marker_sets:
  s=new_marker_set('particle_251 geometry')
  marker_sets["particle_251 geometry"]=s
s= marker_sets["particle_251 geometry"]
mark=s.place_marker((3231.19, 2354.37, 3155.58), (0.7, 0.7, 0.7), 133.541)
if "particle_252 geometry" not in marker_sets:
  s=new_marker_set('particle_252 geometry')
  marker_sets["particle_252 geometry"]=s
s= marker_sets["particle_252 geometry"]
mark=s.place_marker((3217.74, 1973.91, 3354.74), (0.7, 0.7, 0.7), 171.019)
if "particle_253 geometry" not in marker_sets:
  s=new_marker_set('particle_253 geometry')
  marker_sets["particle_253 geometry"]=s
s= marker_sets["particle_253 geometry"]
mark=s.place_marker((3210.15, 1746.4, 3681.11), (0.7, 0.7, 0.7), 115.437)
if "particle_254 geometry" not in marker_sets:
  s=new_marker_set('particle_254 geometry')
  marker_sets["particle_254 geometry"]=s
s= marker_sets["particle_254 geometry"]
mark=s.place_marker((3364.57, 2015.75, 3571.95), (0.7, 0.7, 0.7), 158.583)
if "particle_255 geometry" not in marker_sets:
  s=new_marker_set('particle_255 geometry')
  marker_sets["particle_255 geometry"]=s
s= marker_sets["particle_255 geometry"]
mark=s.place_marker((3140.78, 2064.02, 3179.68), (0.7, 0.7, 0.7), 192)
if "particle_256 geometry" not in marker_sets:
  s=new_marker_set('particle_256 geometry')
  marker_sets["particle_256 geometry"]=s
s= marker_sets["particle_256 geometry"]
mark=s.place_marker((3081.96, 2222.92, 2790.79), (0.7, 0.7, 0.7), 150.165)
if "particle_257 geometry" not in marker_sets:
  s=new_marker_set('particle_257 geometry')
  marker_sets["particle_257 geometry"]=s
s= marker_sets["particle_257 geometry"]
mark=s.place_marker((3066.2, 1985.48, 2775.2), (0.7, 0.7, 0.7), 157.567)
if "particle_258 geometry" not in marker_sets:
  s=new_marker_set('particle_258 geometry')
  marker_sets["particle_258 geometry"]=s
s= marker_sets["particle_258 geometry"]
mark=s.place_marker((2948.76, 1992.9, 2741.89), (0.7, 0.7, 0.7), 199.36)
if "particle_259 geometry" not in marker_sets:
  s=new_marker_set('particle_259 geometry')
  marker_sets["particle_259 geometry"]=s
s= marker_sets["particle_259 geometry"]
mark=s.place_marker((2817.51, 2142.52, 3163.01), (0.7, 0.7, 0.7), 105.369)
if "particle_260 geometry" not in marker_sets:
  s=new_marker_set('particle_260 geometry')
  marker_sets["particle_260 geometry"]=s
s= marker_sets["particle_260 geometry"]
mark=s.place_marker((2634.18, 2276.43, 3312.8), (0.7, 0.7, 0.7), 118.651)
if "particle_261 geometry" not in marker_sets:
  s=new_marker_set('particle_261 geometry')
  marker_sets["particle_261 geometry"]=s
s= marker_sets["particle_261 geometry"]
mark=s.place_marker((2727.22, 2349.72, 2880.79), (0.7, 0.7, 0.7), 219.664)
if "particle_262 geometry" not in marker_sets:
  s=new_marker_set('particle_262 geometry')
  marker_sets["particle_262 geometry"]=s
s= marker_sets["particle_262 geometry"]
mark=s.place_marker((2910.09, 2232.54, 2327.43), (0.7, 0.7, 0.7), 196.018)
if "particle_263 geometry" not in marker_sets:
  s=new_marker_set('particle_263 geometry')
  marker_sets["particle_263 geometry"]=s
s= marker_sets["particle_263 geometry"]
mark=s.place_marker((2984.53, 2143.91, 1840.4), (0.7, 0.7, 0.7), 218.141)
if "particle_264 geometry" not in marker_sets:
  s=new_marker_set('particle_264 geometry')
  marker_sets["particle_264 geometry"]=s
s= marker_sets["particle_264 geometry"]
mark=s.place_marker((2803.65, 1838.54, 1826.78), (0.7, 0.7, 0.7), 181.636)
if "particle_265 geometry" not in marker_sets:
  s=new_marker_set('particle_265 geometry')
  marker_sets["particle_265 geometry"]=s
s= marker_sets["particle_265 geometry"]
mark=s.place_marker((2684.95, 1796.39, 2096.69), (0.7, 0.7, 0.7), 195.003)
if "particle_266 geometry" not in marker_sets:
  s=new_marker_set('particle_266 geometry')
  marker_sets["particle_266 geometry"]=s
s= marker_sets["particle_266 geometry"]
mark=s.place_marker((2851.63, 1792.83, 1902.82), (0.7, 0.7, 0.7), 139.209)
if "particle_267 geometry" not in marker_sets:
  s=new_marker_set('particle_267 geometry')
  marker_sets["particle_267 geometry"]=s
s= marker_sets["particle_267 geometry"]
mark=s.place_marker((2907.81, 1731.98, 1907.73), (0.7, 0.7, 0.7), 189.885)
if "particle_268 geometry" not in marker_sets:
  s=new_marker_set('particle_268 geometry')
  marker_sets["particle_268 geometry"]=s
s= marker_sets["particle_268 geometry"]
mark=s.place_marker((3124.84, 1825.61, 2118.33), (0.7, 0.7, 0.7), 267.674)
if "particle_269 geometry" not in marker_sets:
  s=new_marker_set('particle_269 geometry')
  marker_sets["particle_269 geometry"]=s
s= marker_sets["particle_269 geometry"]
mark=s.place_marker((3517.01, 2116.59, 2401.73), (0.7, 0.7, 0.7), 196.568)
if "particle_270 geometry" not in marker_sets:
  s=new_marker_set('particle_270 geometry')
  marker_sets["particle_270 geometry"]=s
s= marker_sets["particle_270 geometry"]
mark=s.place_marker((3585.86, 1843.82, 2418.15), (0.7, 0.7, 0.7), 192.423)
if "particle_271 geometry" not in marker_sets:
  s=new_marker_set('particle_271 geometry')
  marker_sets["particle_271 geometry"]=s
s= marker_sets["particle_271 geometry"]
mark=s.place_marker((3476.07, 1563.6, 2133.65), (1, 0.7, 0), 202.405)
if "particle_272 geometry" not in marker_sets:
  s=new_marker_set('particle_272 geometry')
  marker_sets["particle_272 geometry"]=s
s= marker_sets["particle_272 geometry"]
mark=s.place_marker((3793.57, 2096.87, 2750.71), (0.7, 0.7, 0.7), 135.529)
if "particle_273 geometry" not in marker_sets:
  s=new_marker_set('particle_273 geometry')
  marker_sets["particle_273 geometry"]=s
s= marker_sets["particle_273 geometry"]
mark=s.place_marker((4164.1, 2554.51, 3547.2), (0.7, 0.7, 0.7), 114.21)
if "particle_274 geometry" not in marker_sets:
  s=new_marker_set('particle_274 geometry')
  marker_sets["particle_274 geometry"]=s
s= marker_sets["particle_274 geometry"]
mark=s.place_marker((3876.11, 2594.99, 3690.75), (0.7, 0.7, 0.7), 159.133)
if "particle_275 geometry" not in marker_sets:
  s=new_marker_set('particle_275 geometry')
  marker_sets["particle_275 geometry"]=s
s= marker_sets["particle_275 geometry"]
mark=s.place_marker((3545.25, 2698.17, 3469.88), (0.7, 0.7, 0.7), 144.412)
if "particle_276 geometry" not in marker_sets:
  s=new_marker_set('particle_276 geometry')
  marker_sets["particle_276 geometry"]=s
s= marker_sets["particle_276 geometry"]
mark=s.place_marker((3308.69, 2796.34, 3279.22), (0.7, 0.7, 0.7), 70.8525)
if "particle_277 geometry" not in marker_sets:
  s=new_marker_set('particle_277 geometry')
  marker_sets["particle_277 geometry"]=s
s= marker_sets["particle_277 geometry"]
mark=s.place_marker((3100.51, 2445.65, 2803.63), (0.7, 0.7, 0.7), 141.874)
if "particle_278 geometry" not in marker_sets:
  s=new_marker_set('particle_278 geometry')
  marker_sets["particle_278 geometry"]=s
s= marker_sets["particle_278 geometry"]
mark=s.place_marker((2985.9, 2063.54, 2337.76), (0.7, 0.7, 0.7), 217.337)
if "particle_279 geometry" not in marker_sets:
  s=new_marker_set('particle_279 geometry')
  marker_sets["particle_279 geometry"]=s
s= marker_sets["particle_279 geometry"]
mark=s.place_marker((3011.19, 2091.52, 2281.53), (0.7, 0.7, 0.7), 237.641)
if "particle_280 geometry" not in marker_sets:
  s=new_marker_set('particle_280 geometry')
  marker_sets["particle_280 geometry"]=s
s= marker_sets["particle_280 geometry"]
mark=s.place_marker((3053.11, 2527.63, 2420.06), (0.7, 0.7, 0.7), 229.393)
if "particle_281 geometry" not in marker_sets:
  s=new_marker_set('particle_281 geometry')
  marker_sets["particle_281 geometry"]=s
s= marker_sets["particle_281 geometry"]
mark=s.place_marker((3124.27, 2589.11, 1819.18), (0.7, 0.7, 0.7), 349.906)
if "particle_282 geometry" not in marker_sets:
  s=new_marker_set('particle_282 geometry')
  marker_sets["particle_282 geometry"]=s
s= marker_sets["particle_282 geometry"]
mark=s.place_marker((3428.38, 2400.67, 1368.19), (0.7, 0.7, 0.7), 162.347)
if "particle_283 geometry" not in marker_sets:
  s=new_marker_set('particle_283 geometry')
  marker_sets["particle_283 geometry"]=s
s= marker_sets["particle_283 geometry"]
mark=s.place_marker((3543.69, 2425.85, 1250.44), (0.7, 0.7, 0.7), 194.072)
if "particle_284 geometry" not in marker_sets:
  s=new_marker_set('particle_284 geometry')
  marker_sets["particle_284 geometry"]=s
s= marker_sets["particle_284 geometry"]
mark=s.place_marker((3549.53, 2607.28, 1225.32), (0.7, 0.7, 0.7), 242.21)
if "particle_285 geometry" not in marker_sets:
  s=new_marker_set('particle_285 geometry')
  marker_sets["particle_285 geometry"]=s
s= marker_sets["particle_285 geometry"]
mark=s.place_marker((3986.23, 2883.29, 1348.85), (0.7, 0.7, 0.7), 320.93)
if "particle_286 geometry" not in marker_sets:
  s=new_marker_set('particle_286 geometry')
  marker_sets["particle_286 geometry"]=s
s= marker_sets["particle_286 geometry"]
mark=s.place_marker((4358.21, 3125.92, 966.886), (0.7, 0.7, 0.7), 226.432)
if "particle_287 geometry" not in marker_sets:
  s=new_marker_set('particle_287 geometry')
  marker_sets["particle_287 geometry"]=s
s= marker_sets["particle_287 geometry"]
mark=s.place_marker((4066.26, 3094.41, 669.205), (0.7, 0.7, 0.7), 125.208)
if "particle_288 geometry" not in marker_sets:
  s=new_marker_set('particle_288 geometry')
  marker_sets["particle_288 geometry"]=s
s= marker_sets["particle_288 geometry"]
mark=s.place_marker((3551.66, 3002.96, 577.826), (0.7, 0.7, 0.7), 197.837)
if "particle_289 geometry" not in marker_sets:
  s=new_marker_set('particle_289 geometry')
  marker_sets["particle_289 geometry"]=s
s= marker_sets["particle_289 geometry"]
mark=s.place_marker((3198.9, 3459.9, 299.33), (0.7, 0.7, 0.7), 167.804)
if "particle_290 geometry" not in marker_sets:
  s=new_marker_set('particle_290 geometry')
  marker_sets["particle_290 geometry"]=s
s= marker_sets["particle_290 geometry"]
mark=s.place_marker((3057.47, 4183.55, -86.1594), (0.7, 0.7, 0.7), 136.84)
if "particle_291 geometry" not in marker_sets:
  s=new_marker_set('particle_291 geometry')
  marker_sets["particle_291 geometry"]=s
s= marker_sets["particle_291 geometry"]
mark=s.place_marker((3259.95, 4469.43, 215.349), (0.7, 0.7, 0.7), 85.7421)
if "particle_292 geometry" not in marker_sets:
  s=new_marker_set('particle_292 geometry')
  marker_sets["particle_292 geometry"]=s
s= marker_sets["particle_292 geometry"]
mark=s.place_marker((3784.65, 3343.36, 859.232), (1, 0.7, 0), 256)
if "particle_293 geometry" not in marker_sets:
  s=new_marker_set('particle_293 geometry')
  marker_sets["particle_293 geometry"]=s
s= marker_sets["particle_293 geometry"]
mark=s.place_marker((2962.8, 3669.35, 160.907), (0.7, 0.7, 0.7), 138.702)
if "particle_294 geometry" not in marker_sets:
  s=new_marker_set('particle_294 geometry')
  marker_sets["particle_294 geometry"]=s
s= marker_sets["particle_294 geometry"]
mark=s.place_marker((2657.15, 3663.95, -206.081), (0.7, 0.7, 0.7), 140.732)
if "particle_295 geometry" not in marker_sets:
  s=new_marker_set('particle_295 geometry')
  marker_sets["particle_295 geometry"]=s
s= marker_sets["particle_295 geometry"]
mark=s.place_marker((2967.17, 3647.58, -164.798), (0.7, 0.7, 0.7), 81.3006)
if "particle_296 geometry" not in marker_sets:
  s=new_marker_set('particle_296 geometry')
  marker_sets["particle_296 geometry"]=s
s= marker_sets["particle_296 geometry"]
mark=s.place_marker((3296.18, 3909.84, -307.588), (0.7, 0.7, 0.7), 133.837)
if "particle_297 geometry" not in marker_sets:
  s=new_marker_set('particle_297 geometry')
  marker_sets["particle_297 geometry"]=s
s= marker_sets["particle_297 geometry"]
mark=s.place_marker((3518.12, 3557.79, 158.548), (0.7, 0.7, 0.7), 98.3475)
if "particle_298 geometry" not in marker_sets:
  s=new_marker_set('particle_298 geometry')
  marker_sets["particle_298 geometry"]=s
s= marker_sets["particle_298 geometry"]
mark=s.place_marker((3518.76, 2914.68, 674.411), (0.7, 0.7, 0.7), 297.623)
if "particle_299 geometry" not in marker_sets:
  s=new_marker_set('particle_299 geometry')
  marker_sets["particle_299 geometry"]=s
s= marker_sets["particle_299 geometry"]
mark=s.place_marker((3644.25, 2749.65, 1039.54), (0.7, 0.7, 0.7), 212.938)
if "particle_300 geometry" not in marker_sets:
  s=new_marker_set('particle_300 geometry')
  marker_sets["particle_300 geometry"]=s
s= marker_sets["particle_300 geometry"]
mark=s.place_marker((3754.77, 2631.98, 893.523), (0.7, 0.7, 0.7), 154.183)
if "particle_301 geometry" not in marker_sets:
  s=new_marker_set('particle_301 geometry')
  marker_sets["particle_301 geometry"]=s
s= marker_sets["particle_301 geometry"]
mark=s.place_marker((4141.17, 2771.64, 982.908), (0.7, 0.7, 0.7), 180.832)
if "particle_302 geometry" not in marker_sets:
  s=new_marker_set('particle_302 geometry')
  marker_sets["particle_302 geometry"]=s
s= marker_sets["particle_302 geometry"]
mark=s.place_marker((4328.27, 3019.89, 1205.25), (0.7, 0.7, 0.7), 122.332)
if "particle_303 geometry" not in marker_sets:
  s=new_marker_set('particle_303 geometry')
  marker_sets["particle_303 geometry"]=s
s= marker_sets["particle_303 geometry"]
mark=s.place_marker((4354.64, 3309.31, 1452.81), (0.7, 0.7, 0.7), 209.047)
if "particle_304 geometry" not in marker_sets:
  s=new_marker_set('particle_304 geometry')
  marker_sets["particle_304 geometry"]=s
s= marker_sets["particle_304 geometry"]
mark=s.place_marker((4727.89, 3147.74, 1399), (0.7, 0.7, 0.7), 126.985)
if "particle_305 geometry" not in marker_sets:
  s=new_marker_set('particle_305 geometry')
  marker_sets["particle_305 geometry"]=s
s= marker_sets["particle_305 geometry"]
mark=s.place_marker((5084.54, 3268.01, 1205.58), (0.7, 0.7, 0.7), 122.205)
if "particle_306 geometry" not in marker_sets:
  s=new_marker_set('particle_306 geometry')
  marker_sets["particle_306 geometry"]=s
s= marker_sets["particle_306 geometry"]
mark=s.place_marker((5128.08, 3300.78, 931.937), (0.7, 0.7, 0.7), 107.95)
if "particle_307 geometry" not in marker_sets:
  s=new_marker_set('particle_307 geometry')
  marker_sets["particle_307 geometry"]=s
s= marker_sets["particle_307 geometry"]
mark=s.place_marker((4655.73, 2936.11, 1031.75), (0.7, 0.7, 0.7), 182.567)
if "particle_308 geometry" not in marker_sets:
  s=new_marker_set('particle_308 geometry')
  marker_sets["particle_308 geometry"]=s
s= marker_sets["particle_308 geometry"]
mark=s.place_marker((4061.23, 2731.61, 1134.54), (0.7, 0.7, 0.7), 185.274)
if "particle_309 geometry" not in marker_sets:
  s=new_marker_set('particle_309 geometry')
  marker_sets["particle_309 geometry"]=s
s= marker_sets["particle_309 geometry"]
mark=s.place_marker((3650.01, 2814.93, 1347.39), (0.7, 0.7, 0.7), 413.567)
if "particle_310 geometry" not in marker_sets:
  s=new_marker_set('particle_310 geometry')
  marker_sets["particle_310 geometry"]=s
s= marker_sets["particle_310 geometry"]
mark=s.place_marker((3537.23, 2619.41, 1316.17), (0.7, 0.7, 0.7), 240.01)
if "particle_311 geometry" not in marker_sets:
  s=new_marker_set('particle_311 geometry')
  marker_sets["particle_311 geometry"]=s
s= marker_sets["particle_311 geometry"]
mark=s.place_marker((3560.3, 2648.68, 1339.89), (0.7, 0.7, 0.7), 238.995)
if "particle_312 geometry" not in marker_sets:
  s=new_marker_set('particle_312 geometry')
  marker_sets["particle_312 geometry"]=s
s= marker_sets["particle_312 geometry"]
mark=s.place_marker((3758.63, 2583.3, 1195.47), (0.7, 0.7, 0.7), 203.674)
if "particle_313 geometry" not in marker_sets:
  s=new_marker_set('particle_313 geometry')
  marker_sets["particle_313 geometry"]=s
s= marker_sets["particle_313 geometry"]
mark=s.place_marker((4312.93, 2364.84, 1289.75), (0.7, 0.7, 0.7), 266.744)
if "particle_314 geometry" not in marker_sets:
  s=new_marker_set('particle_314 geometry')
  marker_sets["particle_314 geometry"]=s
s= marker_sets["particle_314 geometry"]
mark=s.place_marker((4272.75, 2253.3, 845.808), (0.7, 0.7, 0.7), 147.585)
if "particle_315 geometry" not in marker_sets:
  s=new_marker_set('particle_315 geometry')
  marker_sets["particle_315 geometry"]=s
s= marker_sets["particle_315 geometry"]
mark=s.place_marker((4039.02, 2313, 948.825), (0.7, 0.7, 0.7), 249.485)
if "particle_316 geometry" not in marker_sets:
  s=new_marker_set('particle_316 geometry')
  marker_sets["particle_316 geometry"]=s
s= marker_sets["particle_316 geometry"]
mark=s.place_marker((4028.75, 2429.05, 1359.06), (0.7, 0.7, 0.7), 119.371)
if "particle_317 geometry" not in marker_sets:
  s=new_marker_set('particle_317 geometry')
  marker_sets["particle_317 geometry"]=s
s= marker_sets["particle_317 geometry"]
mark=s.place_marker((4211.63, 2962.9, 1773.79), (0.7, 0.7, 0.7), 155.875)
if "particle_318 geometry" not in marker_sets:
  s=new_marker_set('particle_318 geometry')
  marker_sets["particle_318 geometry"]=s
s= marker_sets["particle_318 geometry"]
mark=s.place_marker((4136.41, 3717.58, 1854.68), (0.7, 0.7, 0.7), 189.419)
if "particle_319 geometry" not in marker_sets:
  s=new_marker_set('particle_319 geometry')
  marker_sets["particle_319 geometry"]=s
s= marker_sets["particle_319 geometry"]
mark=s.place_marker((3638.37, 3917.85, 1737.07), (0.7, 0.7, 0.7), 137.475)
if "particle_320 geometry" not in marker_sets:
  s=new_marker_set('particle_320 geometry')
  marker_sets["particle_320 geometry"]=s
s= marker_sets["particle_320 geometry"]
mark=s.place_marker((3160.03, 3828.51, 1668.18), (0.7, 0.7, 0.7), 176.179)
if "particle_321 geometry" not in marker_sets:
  s=new_marker_set('particle_321 geometry')
  marker_sets["particle_321 geometry"]=s
s= marker_sets["particle_321 geometry"]
mark=s.place_marker((2732.56, 3905.6, 1527.45), (0.7, 0.7, 0.7), 138.829)
if "particle_322 geometry" not in marker_sets:
  s=new_marker_set('particle_322 geometry')
  marker_sets["particle_322 geometry"]=s
s= marker_sets["particle_322 geometry"]
mark=s.place_marker((2423.6, 4054.59, 1297.77), (0.7, 0.7, 0.7), 148.727)
if "particle_323 geometry" not in marker_sets:
  s=new_marker_set('particle_323 geometry')
  marker_sets["particle_323 geometry"]=s
s= marker_sets["particle_323 geometry"]
mark=s.place_marker((2193.93, 4399.24, 986.091), (0.7, 0.7, 0.7), 230.323)
if "particle_324 geometry" not in marker_sets:
  s=new_marker_set('particle_324 geometry')
  marker_sets["particle_324 geometry"]=s
s= marker_sets["particle_324 geometry"]
mark=s.place_marker((2754.59, 4170.02, 1176.25), (0.7, 0.7, 0.7), 175.376)
if "particle_325 geometry" not in marker_sets:
  s=new_marker_set('particle_325 geometry')
  marker_sets["particle_325 geometry"]=s
s= marker_sets["particle_325 geometry"]
mark=s.place_marker((3076.9, 3841.43, 1389.32), (0.7, 0.7, 0.7), 161.163)
if "particle_326 geometry" not in marker_sets:
  s=new_marker_set('particle_326 geometry')
  marker_sets["particle_326 geometry"]=s
s= marker_sets["particle_326 geometry"]
mark=s.place_marker((3009.67, 4059.36, 1809.8), (0.7, 0.7, 0.7), 125.885)
if "particle_327 geometry" not in marker_sets:
  s=new_marker_set('particle_327 geometry')
  marker_sets["particle_327 geometry"]=s
s= marker_sets["particle_327 geometry"]
mark=s.place_marker((3106.62, 4383.4, 2139.22), (0.7, 0.7, 0.7), 206.635)
if "particle_328 geometry" not in marker_sets:
  s=new_marker_set('particle_328 geometry')
  marker_sets["particle_328 geometry"]=s
s= marker_sets["particle_328 geometry"]
mark=s.place_marker((2787.48, 4039.22, 2116.9), (0.7, 0.7, 0.7), 151.392)
if "particle_329 geometry" not in marker_sets:
  s=new_marker_set('particle_329 geometry')
  marker_sets["particle_329 geometry"]=s
s= marker_sets["particle_329 geometry"]
mark=s.place_marker((2511.36, 3805.95, 1966.32), (0.7, 0.7, 0.7), 173.388)
if "particle_330 geometry" not in marker_sets:
  s=new_marker_set('particle_330 geometry')
  marker_sets["particle_330 geometry"]=s
s= marker_sets["particle_330 geometry"]
mark=s.place_marker((2322.9, 3918.32, 1686.05), (0.7, 0.7, 0.7), 135.825)
if "particle_331 geometry" not in marker_sets:
  s=new_marker_set('particle_331 geometry')
  marker_sets["particle_331 geometry"]=s
s= marker_sets["particle_331 geometry"]
mark=s.place_marker((2222.23, 4215.06, 1373.81), (0.7, 0.7, 0.7), 186.839)
if "particle_332 geometry" not in marker_sets:
  s=new_marker_set('particle_332 geometry')
  marker_sets["particle_332 geometry"]=s
s= marker_sets["particle_332 geometry"]
mark=s.place_marker((2172.2, 4577.3, 1065.78), (0.7, 0.7, 0.7), 121.189)
if "particle_333 geometry" not in marker_sets:
  s=new_marker_set('particle_333 geometry')
  marker_sets["particle_333 geometry"]=s
s= marker_sets["particle_333 geometry"]
mark=s.place_marker((2485.89, 4356.86, 1248.05), (0.7, 0.7, 0.7), 102.916)
if "particle_334 geometry" not in marker_sets:
  s=new_marker_set('particle_334 geometry')
  marker_sets["particle_334 geometry"]=s
s= marker_sets["particle_334 geometry"]
mark=s.place_marker((2933.79, 3952.74, 1415.22), (0.7, 0.7, 0.7), 212.769)
if "particle_335 geometry" not in marker_sets:
  s=new_marker_set('particle_335 geometry')
  marker_sets["particle_335 geometry"]=s
s= marker_sets["particle_335 geometry"]
mark=s.place_marker((3191.76, 3383.93, 1687.74), (0.7, 0.7, 0.7), 173.092)
if "particle_336 geometry" not in marker_sets:
  s=new_marker_set('particle_336 geometry')
  marker_sets["particle_336 geometry"]=s
s= marker_sets["particle_336 geometry"]
mark=s.place_marker((3582.15, 3109.6, 1857.89), (0.7, 0.7, 0.7), 264.502)
if "particle_337 geometry" not in marker_sets:
  s=new_marker_set('particle_337 geometry')
  marker_sets["particle_337 geometry"]=s
s= marker_sets["particle_337 geometry"]
mark=s.place_marker((4129.39, 3198.52, 1921.66), (0.7, 0.7, 0.7), 208.666)
if "particle_338 geometry" not in marker_sets:
  s=new_marker_set('particle_338 geometry')
  marker_sets["particle_338 geometry"]=s
s= marker_sets["particle_338 geometry"]
mark=s.place_marker((4578.27, 3265.37, 1718.38), (0.7, 0.7, 0.7), 186.797)
if "particle_339 geometry" not in marker_sets:
  s=new_marker_set('particle_339 geometry')
  marker_sets["particle_339 geometry"]=s
s= marker_sets["particle_339 geometry"]
mark=s.place_marker((4742.66, 2850.93, 1479.45), (0.7, 0.7, 0.7), 255.534)
if "particle_340 geometry" not in marker_sets:
  s=new_marker_set('particle_340 geometry')
  marker_sets["particle_340 geometry"]=s
s= marker_sets["particle_340 geometry"]
mark=s.place_marker((4804.52, 2837.98, 1053.08), (0.7, 0.7, 0.7), 153.126)
if "particle_341 geometry" not in marker_sets:
  s=new_marker_set('particle_341 geometry')
  marker_sets["particle_341 geometry"]=s
s= marker_sets["particle_341 geometry"]
mark=s.place_marker((5108.72, 3050.02, 1168.14), (0.7, 0.7, 0.7), 165.816)
if "particle_342 geometry" not in marker_sets:
  s=new_marker_set('particle_342 geometry')
  marker_sets["particle_342 geometry"]=s
s= marker_sets["particle_342 geometry"]
mark=s.place_marker((5028.22, 2825.31, 1470.13), (0.7, 0.7, 0.7), 134.429)
if "particle_343 geometry" not in marker_sets:
  s=new_marker_set('particle_343 geometry')
  marker_sets["particle_343 geometry"]=s
s= marker_sets["particle_343 geometry"]
mark=s.place_marker((4741.71, 2904.1, 1706.44), (0.7, 0.7, 0.7), 178.971)
if "particle_344 geometry" not in marker_sets:
  s=new_marker_set('particle_344 geometry')
  marker_sets["particle_344 geometry"]=s
s= marker_sets["particle_344 geometry"]
mark=s.place_marker((4487.58, 3335.84, 1720.72), (0.7, 0.7, 0.7), 189.969)
if "particle_345 geometry" not in marker_sets:
  s=new_marker_set('particle_345 geometry')
  marker_sets["particle_345 geometry"]=s
s= marker_sets["particle_345 geometry"]
mark=s.place_marker((4662.85, 3920.73, 1830.91), (0.7, 0.7, 0.7), 121.359)
if "particle_346 geometry" not in marker_sets:
  s=new_marker_set('particle_346 geometry')
  marker_sets["particle_346 geometry"]=s
s= marker_sets["particle_346 geometry"]
mark=s.place_marker((4257.31, 4278.15, 1879.02), (0.7, 0.7, 0.7), 187.262)
if "particle_347 geometry" not in marker_sets:
  s=new_marker_set('particle_347 geometry')
  marker_sets["particle_347 geometry"]=s
s= marker_sets["particle_347 geometry"]
mark=s.place_marker((3609.59, 4216.13, 1951.61), (0.7, 0.7, 0.7), 164.335)
if "particle_348 geometry" not in marker_sets:
  s=new_marker_set('particle_348 geometry')
  marker_sets["particle_348 geometry"]=s
s= marker_sets["particle_348 geometry"]
mark=s.place_marker((3215.98, 4195.82, 1593.53), (0.7, 0.7, 0.7), 138.363)
if "particle_349 geometry" not in marker_sets:
  s=new_marker_set('particle_349 geometry')
  marker_sets["particle_349 geometry"]=s
s= marker_sets["particle_349 geometry"]
mark=s.place_marker((2892.95, 4312.66, 1392.93), (0.7, 0.7, 0.7), 138.49)
if "particle_350 geometry" not in marker_sets:
  s=new_marker_set('particle_350 geometry')
  marker_sets["particle_350 geometry"]=s
s= marker_sets["particle_350 geometry"]
mark=s.place_marker((2693.42, 4305.96, 1678.61), (0.7, 0.7, 0.7), 116.325)
if "particle_351 geometry" not in marker_sets:
  s=new_marker_set('particle_351 geometry')
  marker_sets["particle_351 geometry"]=s
s= marker_sets["particle_351 geometry"]
mark=s.place_marker((3012.3, 4108.74, 1928.68), (0.7, 0.7, 0.7), 106.511)
if "particle_352 geometry" not in marker_sets:
  s=new_marker_set('particle_352 geometry')
  marker_sets["particle_352 geometry"]=s
s= marker_sets["particle_352 geometry"]
mark=s.place_marker((3492.04, 3849.01, 1934.07), (0.7, 0.7, 0.7), 151.096)
if "particle_353 geometry" not in marker_sets:
  s=new_marker_set('particle_353 geometry')
  marker_sets["particle_353 geometry"]=s
s= marker_sets["particle_353 geometry"]
mark=s.place_marker((4134.64, 3708.43, 1823.6), (0.7, 0.7, 0.7), 240.856)
if "particle_354 geometry" not in marker_sets:
  s=new_marker_set('particle_354 geometry')
  marker_sets["particle_354 geometry"]=s
s= marker_sets["particle_354 geometry"]
mark=s.place_marker((4603.65, 3633.98, 1645.61), (0.7, 0.7, 0.7), 149.7)
if "particle_355 geometry" not in marker_sets:
  s=new_marker_set('particle_355 geometry')
  marker_sets["particle_355 geometry"]=s
s= marker_sets["particle_355 geometry"]
mark=s.place_marker((4789.87, 3372.5, 1704.85), (0.7, 0.7, 0.7), 165.943)
if "particle_356 geometry" not in marker_sets:
  s=new_marker_set('particle_356 geometry')
  marker_sets["particle_356 geometry"]=s
s= marker_sets["particle_356 geometry"]
mark=s.place_marker((4444.13, 2870.38, 1659.71), (0.7, 0.7, 0.7), 178.971)
if "particle_357 geometry" not in marker_sets:
  s=new_marker_set('particle_357 geometry')
  marker_sets["particle_357 geometry"]=s
s= marker_sets["particle_357 geometry"]
mark=s.place_marker((4243.69, 2144.01, 1751.19), (0.7, 0.7, 0.7), 154.945)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
