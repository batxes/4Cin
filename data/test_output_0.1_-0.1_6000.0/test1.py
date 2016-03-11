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
mark=s.place_marker((889.336, -2802.22, -615.436), (0, 0, 1), 471.518)
if "particle_1 geometry" not in marker_sets:
  s=new_marker_set('particle_1 geometry')
  marker_sets["particle_1 geometry"]=s
s= marker_sets["particle_1 geometry"]
mark=s.place_marker((1048.09, -1201.19, -758.397), (0, 1, 0), 388.864)
if "particle_2 geometry" not in marker_sets:
  s=new_marker_set('particle_2 geometry')
  marker_sets["particle_2 geometry"]=s
s= marker_sets["particle_2 geometry"]
mark=s.place_marker((1364.38, -2366, -42.3934), (0.0149254, 0, 0.985075), 489.707)
if "particle_3 geometry" not in marker_sets:
  s=new_marker_set('particle_3 geometry')
  marker_sets["particle_3 geometry"]=s
s= marker_sets["particle_3 geometry"]
mark=s.place_marker((1862.82, -2068.75, -729.505), (0.0223881, 0, 0.977612), 360.396)
if "particle_4 geometry" not in marker_sets:
  s=new_marker_set('particle_4 geometry')
  marker_sets["particle_4 geometry"]=s
s= marker_sets["particle_4 geometry"]
mark=s.place_marker((1626.75, -1590.09, -923.869), (0.0298507, 0, 0.970149), 553.622)
if "particle_5 geometry" not in marker_sets:
  s=new_marker_set('particle_5 geometry')
  marker_sets["particle_5 geometry"]=s
s= marker_sets["particle_5 geometry"]
mark=s.place_marker((1041.55, -2064.32, -986.857), (0.0373134, 0, 0.962687), 426.299)
if "particle_6 geometry" not in marker_sets:
  s=new_marker_set('particle_6 geometry')
  marker_sets["particle_6 geometry"]=s
s= marker_sets["particle_6 geometry"]
mark=s.place_marker((47.4617, -2331.48, -897.979), (0.0447761, 0, 0.955224), 442.331)
if "particle_7 geometry" not in marker_sets:
  s=new_marker_set('particle_7 geometry')
  marker_sets["particle_7 geometry"]=s
s= marker_sets["particle_7 geometry"]
mark=s.place_marker((-960.287, -2732.98, -1206.17), (0.0522388, 0, 0.947761), 300.668)
if "particle_8 geometry" not in marker_sets:
  s=new_marker_set('particle_8 geometry')
  marker_sets["particle_8 geometry"]=s
s= marker_sets["particle_8 geometry"]
mark=s.place_marker((-470.718, -1587.1, -1035.98), (0.0597015, 0, 0.940299), 342.376)
if "particle_9 geometry" not in marker_sets:
  s=new_marker_set('particle_9 geometry')
  marker_sets["particle_9 geometry"]=s
s= marker_sets["particle_9 geometry"]
mark=s.place_marker((350.295, -1626.41, -1001.88), (0.0671642, 0, 0.932836), 410.056)
if "particle_10 geometry" not in marker_sets:
  s=new_marker_set('particle_10 geometry')
  marker_sets["particle_10 geometry"]=s
s= marker_sets["particle_10 geometry"]
mark=s.place_marker((1020.55, -2230.13, -881.217), (0.0746269, 0, 0.925373), 467.415)
if "particle_11 geometry" not in marker_sets:
  s=new_marker_set('particle_11 geometry')
  marker_sets["particle_11 geometry"]=s
s= marker_sets["particle_11 geometry"]
mark=s.place_marker((1922.52, -1683.24, -637.543), (0.0820896, 0, 0.91791), 566.778)
if "particle_12 geometry" not in marker_sets:
  s=new_marker_set('particle_12 geometry')
  marker_sets["particle_12 geometry"]=s
s= marker_sets["particle_12 geometry"]
mark=s.place_marker((1313.34, -1958.56, -693.333), (0.0895522, 0, 0.910448), 447.576)
if "particle_13 geometry" not in marker_sets:
  s=new_marker_set('particle_13 geometry')
  marker_sets["particle_13 geometry"]=s
s= marker_sets["particle_13 geometry"]
mark=s.place_marker((1079.65, -1318.15, -1129.32), (0.0970149, 0, 0.902985), 213.403)
if "particle_14 geometry" not in marker_sets:
  s=new_marker_set('particle_14 geometry')
  marker_sets["particle_14 geometry"]=s
s= marker_sets["particle_14 geometry"]
mark=s.place_marker((1287.75, -1262.6, -1557.73), (0.104478, 0, 0.895522), 516.525)
if "particle_15 geometry" not in marker_sets:
  s=new_marker_set('particle_15 geometry')
  marker_sets["particle_15 geometry"]=s
s= marker_sets["particle_15 geometry"]
mark=s.place_marker((1438.81, -1342.18, -1611.88), (0.11194, 0, 0.88806), 444.108)
if "particle_16 geometry" not in marker_sets:
  s=new_marker_set('particle_16 geometry')
  marker_sets["particle_16 geometry"]=s
s= marker_sets["particle_16 geometry"]
mark=s.place_marker((1426.7, -1244.13, -1508.42), (0.119403, 0, 0.880597), 631.327)
if "particle_17 geometry" not in marker_sets:
  s=new_marker_set('particle_17 geometry')
  marker_sets["particle_17 geometry"]=s
s= marker_sets["particle_17 geometry"]
mark=s.place_marker((1117.25, -1080.67, -1999.82), (0, 1, 0), 548.673)
if "particle_18 geometry" not in marker_sets:
  s=new_marker_set('particle_18 geometry')
  marker_sets["particle_18 geometry"]=s
s= marker_sets["particle_18 geometry"]
mark=s.place_marker((1862.19, -907.569, -1606.68), (0.134328, 0, 0.865672), 321.734)
if "particle_19 geometry" not in marker_sets:
  s=new_marker_set('particle_19 geometry')
  marker_sets["particle_19 geometry"]=s
s= marker_sets["particle_19 geometry"]
mark=s.place_marker((1807.05, -335.328, -1510.53), (0.141791, 0, 0.858209), 454.344)
if "particle_20 geometry" not in marker_sets:
  s=new_marker_set('particle_20 geometry')
  marker_sets["particle_20 geometry"]=s
s= marker_sets["particle_20 geometry"]
mark=s.place_marker((2320.7, -275.538, -929.745), (0.149254, 0, 0.850746), 301.684)
if "particle_21 geometry" not in marker_sets:
  s=new_marker_set('particle_21 geometry')
  marker_sets["particle_21 geometry"]=s
s= marker_sets["particle_21 geometry"]
mark=s.place_marker((2003.74, -167.489, -571.167), (0.156716, 0, 0.843284), 353.628)
if "particle_22 geometry" not in marker_sets:
  s=new_marker_set('particle_22 geometry')
  marker_sets["particle_22 geometry"]=s
s= marker_sets["particle_22 geometry"]
mark=s.place_marker((1519.11, 121.942, -429.54), (0.164179, 0, 0.835821), 333.662)
if "particle_23 geometry" not in marker_sets:
  s=new_marker_set('particle_23 geometry')
  marker_sets["particle_23 geometry"]=s
s= marker_sets["particle_23 geometry"]
mark=s.place_marker((1773.32, 423.426, -1091.65), (0.171642, 0, 0.828358), 599.433)
if "particle_24 geometry" not in marker_sets:
  s=new_marker_set('particle_24 geometry')
  marker_sets["particle_24 geometry"]=s
s= marker_sets["particle_24 geometry"]
mark=s.place_marker((1771.89, 433.176, -631.767), (0.179104, 0, 0.820896), 317.377)
if "particle_25 geometry" not in marker_sets:
  s=new_marker_set('particle_25 geometry')
  marker_sets["particle_25 geometry"]=s
s= marker_sets["particle_25 geometry"]
mark=s.place_marker((1294.37, 1041.12, -1605.44), (1, 0.7, 0), 412.171)
if "particle_26 geometry" not in marker_sets:
  s=new_marker_set('particle_26 geometry')
  marker_sets["particle_26 geometry"]=s
s= marker_sets["particle_26 geometry"]
mark=s.place_marker((944.081, 975.913, -1302.25), (0.19403, 0, 0.80597), 541.355)
if "particle_27 geometry" not in marker_sets:
  s=new_marker_set('particle_27 geometry')
  marker_sets["particle_27 geometry"]=s
s= marker_sets["particle_27 geometry"]
mark=s.place_marker((2234.34, 344.681, -1438.66), (0.201493, 0, 0.798507), 598.376)
if "particle_28 geometry" not in marker_sets:
  s=new_marker_set('particle_28 geometry')
  marker_sets["particle_28 geometry"]=s
s= marker_sets["particle_28 geometry"]
mark=s.place_marker((1623.59, -438.656, -1043.72), (0.208955, 0, 0.791045), 431.841)
if "particle_29 geometry" not in marker_sets:
  s=new_marker_set('particle_29 geometry')
  marker_sets["particle_29 geometry"]=s
s= marker_sets["particle_29 geometry"]
mark=s.place_marker((782.19, -316.043, -1038.39), (0.216418, 0, 0.783582), 259.595)
if "particle_30 geometry" not in marker_sets:
  s=new_marker_set('particle_30 geometry')
  marker_sets["particle_30 geometry"]=s
s= marker_sets["particle_30 geometry"]
mark=s.place_marker((589.392, 278.75, -405.265), (0.223881, 0, 0.776119), 479.217)
if "particle_31 geometry" not in marker_sets:
  s=new_marker_set('particle_31 geometry')
  marker_sets["particle_31 geometry"]=s
s= marker_sets["particle_31 geometry"]
mark=s.place_marker((1667.26, 312.773, -9.87542), (0.231343, 0, 0.768657), 437.382)
if "particle_32 geometry" not in marker_sets:
  s=new_marker_set('particle_32 geometry')
  marker_sets["particle_32 geometry"]=s
s= marker_sets["particle_32 geometry"]
mark=s.place_marker((2179.68, 762.993, -291.834), (0.238806, 0, 0.761194), 459.04)
if "particle_33 geometry" not in marker_sets:
  s=new_marker_set('particle_33 geometry')
  marker_sets["particle_33 geometry"]=s
s= marker_sets["particle_33 geometry"]
mark=s.place_marker((1563.45, 303.96, 19.0928), (0.246269, 0, 0.753731), 493.345)
if "particle_34 geometry" not in marker_sets:
  s=new_marker_set('particle_34 geometry')
  marker_sets["particle_34 geometry"]=s
s= marker_sets["particle_34 geometry"]
mark=s.place_marker((2127.21, 279.086, -110.319), (0.253731, 0, 0.746269), 461.704)
if "particle_35 geometry" not in marker_sets:
  s=new_marker_set('particle_35 geometry')
  marker_sets["particle_35 geometry"]=s
s= marker_sets["particle_35 geometry"]
mark=s.place_marker((2583.68, 531.022, -689.791), (0.261194, 0, 0.738806), 297.496)
if "particle_36 geometry" not in marker_sets:
  s=new_marker_set('particle_36 geometry')
  marker_sets["particle_36 geometry"]=s
s= marker_sets["particle_36 geometry"]
mark=s.place_marker((2323.62, 166.448, -303.357), (0.268657, 0, 0.731343), 420.589)
if "particle_37 geometry" not in marker_sets:
  s=new_marker_set('particle_37 geometry')
  marker_sets["particle_37 geometry"]=s
s= marker_sets["particle_37 geometry"]
mark=s.place_marker((1453.65, -79.7374, -83.7917), (0.276119, 0, 0.723881), 253.25)
if "particle_38 geometry" not in marker_sets:
  s=new_marker_set('particle_38 geometry')
  marker_sets["particle_38 geometry"]=s
s= marker_sets["particle_38 geometry"]
mark=s.place_marker((275.377, 267.983, -59.704), (0.283582, 0, 0.716418), 491.061)
if "particle_39 geometry" not in marker_sets:
  s=new_marker_set('particle_39 geometry')
  marker_sets["particle_39 geometry"]=s
s= marker_sets["particle_39 geometry"]
mark=s.place_marker((1128.08, 552.522, 71.289), (0.291045, 0, 0.708955), 357.224)
if "particle_40 geometry" not in marker_sets:
  s=new_marker_set('particle_40 geometry')
  marker_sets["particle_40 geometry"]=s
s= marker_sets["particle_40 geometry"]
mark=s.place_marker((2210.82, 473.706, 105.618), (0.298507, 0, 0.701493), 266.49)
if "particle_41 geometry" not in marker_sets:
  s=new_marker_set('particle_41 geometry')
  marker_sets["particle_41 geometry"]=s
s= marker_sets["particle_41 geometry"]
mark=s.place_marker((2041.32, 685.715, 475.073), (0.30597, 0, 0.69403), 313.062)
if "particle_42 geometry" not in marker_sets:
  s=new_marker_set('particle_42 geometry')
  marker_sets["particle_42 geometry"]=s
s= marker_sets["particle_42 geometry"]
mark=s.place_marker((2100.04, 858.684, 621.618), (0.313433, 0, 0.686567), 551)
if "particle_43 geometry" not in marker_sets:
  s=new_marker_set('particle_43 geometry')
  marker_sets["particle_43 geometry"]=s
s= marker_sets["particle_43 geometry"]
mark=s.place_marker((1110.56, 818.46, 387.495), (0.320896, 0, 0.679104), 395.167)
if "particle_44 geometry" not in marker_sets:
  s=new_marker_set('particle_44 geometry')
  marker_sets["particle_44 geometry"]=s
s= marker_sets["particle_44 geometry"]
mark=s.place_marker((1607.72, 1012.97, 251.238), (0.328358, 0, 0.671642), 309.044)
if "particle_45 geometry" not in marker_sets:
  s=new_marker_set('particle_45 geometry')
  marker_sets["particle_45 geometry"]=s
s= marker_sets["particle_45 geometry"]
mark=s.place_marker((1567.31, 2066.64, -434.308), (1, 0.7, 0), 495.206)
if "particle_46 geometry" not in marker_sets:
  s=new_marker_set('particle_46 geometry')
  marker_sets["particle_46 geometry"]=s
s= marker_sets["particle_46 geometry"]
mark=s.place_marker((1952.43, 1652.13, 182.467), (0.343284, 0, 0.656716), 480.993)
if "particle_47 geometry" not in marker_sets:
  s=new_marker_set('particle_47 geometry')
  marker_sets["particle_47 geometry"]=s
s= marker_sets["particle_47 geometry"]
mark=s.place_marker((1858.26, 1217.29, 953.144), (0.350746, 0, 0.649254), 340.092)
if "particle_48 geometry" not in marker_sets:
  s=new_marker_set('particle_48 geometry')
  marker_sets["particle_48 geometry"]=s
s= marker_sets["particle_48 geometry"]
mark=s.place_marker((1666.16, 860.946, 1391.91), (0.358209, 0, 0.641791), 321.649)
if "particle_49 geometry" not in marker_sets:
  s=new_marker_set('particle_49 geometry')
  marker_sets["particle_49 geometry"]=s
s= marker_sets["particle_49 geometry"]
mark=s.place_marker((1515.38, 665.12, 698.327), (0.365672, 0, 0.634328), 374.905)
if "particle_50 geometry" not in marker_sets:
  s=new_marker_set('particle_50 geometry')
  marker_sets["particle_50 geometry"]=s
s= marker_sets["particle_50 geometry"]
mark=s.place_marker((1586.47, 794.464, 814.279), (0.373134, 0, 0.626866), 493.726)
if "particle_51 geometry" not in marker_sets:
  s=new_marker_set('particle_51 geometry')
  marker_sets["particle_51 geometry"]=s
s= marker_sets["particle_51 geometry"]
mark=s.place_marker((1361.76, 677.593, 1858.32), (0.380597, 0, 0.619403), 454.936)
if "particle_52 geometry" not in marker_sets:
  s=new_marker_set('particle_52 geometry')
  marker_sets["particle_52 geometry"]=s
s= marker_sets["particle_52 geometry"]
mark=s.place_marker((1277.01, 1246.22, 1249.76), (0.38806, 0, 0.61194), 471.941)
if "particle_53 geometry" not in marker_sets:
  s=new_marker_set('particle_53 geometry')
  marker_sets["particle_53 geometry"]=s
s= marker_sets["particle_53 geometry"]
mark=s.place_marker((357.897, 1577.3, 1054.42), (0.395522, 0, 0.604478), 465.173)
if "particle_54 geometry" not in marker_sets:
  s=new_marker_set('particle_54 geometry')
  marker_sets["particle_54 geometry"]=s
s= marker_sets["particle_54 geometry"]
mark=s.place_marker((887.41, 1136.26, 1128.4), (0.402985, 0, 0.597015), 452.568)
if "particle_55 geometry" not in marker_sets:
  s=new_marker_set('particle_55 geometry')
  marker_sets["particle_55 geometry"]=s
s= marker_sets["particle_55 geometry"]
mark=s.place_marker((1532.4, 821.004, 896.305), (0.410448, 0, 0.589552), 539.959)
if "particle_56 geometry" not in marker_sets:
  s=new_marker_set('particle_56 geometry')
  marker_sets["particle_56 geometry"]=s
s= marker_sets["particle_56 geometry"]
mark=s.place_marker((1398.64, 1038.43, 752.856), (0.41791, 0, 0.58209), 239.968)
if "particle_57 geometry" not in marker_sets:
  s=new_marker_set('particle_57 geometry')
  marker_sets["particle_57 geometry"]=s
s= marker_sets["particle_57 geometry"]
mark=s.place_marker((965.889, 1069.76, 489.989), (0.425373, 0, 0.574627), 579.764)
if "particle_58 geometry" not in marker_sets:
  s=new_marker_set('particle_58 geometry')
  marker_sets["particle_58 geometry"]=s
s= marker_sets["particle_58 geometry"]
mark=s.place_marker((1601.72, 965.783, 356.346), (0.432836, 0, 0.567164), 590.635)
if "particle_59 geometry" not in marker_sets:
  s=new_marker_set('particle_59 geometry')
  marker_sets["particle_59 geometry"]=s
s= marker_sets["particle_59 geometry"]
mark=s.place_marker((1967.47, 1255.76, 1358.05), (0.440299, 0, 0.559701), 456.417)
if "particle_60 geometry" not in marker_sets:
  s=new_marker_set('particle_60 geometry')
  marker_sets["particle_60 geometry"]=s
s= marker_sets["particle_60 geometry"]
mark=s.place_marker((1853.42, 1757.81, 2044.89), (0.447761, 0, 0.552239), 264.883)
if "particle_61 geometry" not in marker_sets:
  s=new_marker_set('particle_61 geometry')
  marker_sets["particle_61 geometry"]=s
s= marker_sets["particle_61 geometry"]
mark=s.place_marker((1451.71, 1745.3, 982.238), (0.455224, 0, 0.544776), 365.218)
if "particle_62 geometry" not in marker_sets:
  s=new_marker_set('particle_62 geometry')
  marker_sets["particle_62 geometry"]=s
s= marker_sets["particle_62 geometry"]
mark=s.place_marker((1792.99, 1124.28, 1358.72), (0.462687, 0, 0.537313), 469.615)
if "particle_63 geometry" not in marker_sets:
  s=new_marker_set('particle_63 geometry')
  marker_sets["particle_63 geometry"]=s
s= marker_sets["particle_63 geometry"]
mark=s.place_marker((1738.12, 724.59, 2019.99), (0.470149, 0, 0.529851), 545.881)
if "particle_64 geometry" not in marker_sets:
  s=new_marker_set('particle_64 geometry')
  marker_sets["particle_64 geometry"]=s
s= marker_sets["particle_64 geometry"]
mark=s.place_marker((2124.12, 954.115, 1406.2), (0.477612, 0, 0.522388), 388.695)
if "particle_65 geometry" not in marker_sets:
  s=new_marker_set('particle_65 geometry')
  marker_sets["particle_65 geometry"]=s
s= marker_sets["particle_65 geometry"]
mark=s.place_marker((1632.94, 911.122, 2103.99), (0.485075, 0, 0.514925), 398.254)
if "particle_66 geometry" not in marker_sets:
  s=new_marker_set('particle_66 geometry')
  marker_sets["particle_66 geometry"]=s
s= marker_sets["particle_66 geometry"]
mark=s.place_marker((857.787, 871.78, 2496.84), (0.492537, 0, 0.507463), 332.605)
if "particle_67 geometry" not in marker_sets:
  s=new_marker_set('particle_67 geometry')
  marker_sets["particle_67 geometry"]=s
s= marker_sets["particle_67 geometry"]
mark=s.place_marker((1489.58, 903.612, 2885.14), (0.5, 0, 0.5), 301.853)
if "particle_68 geometry" not in marker_sets:
  s=new_marker_set('particle_68 geometry')
  marker_sets["particle_68 geometry"]=s
s= marker_sets["particle_68 geometry"]
mark=s.place_marker((1397.55, 1148.7, 1376.73), (0.507463, 0, 0.492537), 441.908)
if "particle_69 geometry" not in marker_sets:
  s=new_marker_set('particle_69 geometry')
  marker_sets["particle_69 geometry"]=s
s= marker_sets["particle_69 geometry"]
mark=s.place_marker((1751.05, 1410.16, 770.761), (0.514925, 0, 0.485075), 371.605)
if "particle_70 geometry" not in marker_sets:
  s=new_marker_set('particle_70 geometry')
  marker_sets["particle_70 geometry"]=s
s= marker_sets["particle_70 geometry"]
mark=s.place_marker((1259.94, 1749.73, 1187.36), (0.522388, 0, 0.477612), 444.065)
if "particle_71 geometry" not in marker_sets:
  s=new_marker_set('particle_71 geometry')
  marker_sets["particle_71 geometry"]=s
s= marker_sets["particle_71 geometry"]
mark=s.place_marker((1020.95, 1891.52, 2178.06), (0.529851, 0, 0.470149), 510.476)
if "particle_72 geometry" not in marker_sets:
  s=new_marker_set('particle_72 geometry')
  marker_sets["particle_72 geometry"]=s
s= marker_sets["particle_72 geometry"]
mark=s.place_marker((1824.95, 1533.46, 1828.8), (0.537313, 0, 0.462687), 355.362)
if "particle_73 geometry" not in marker_sets:
  s=new_marker_set('particle_73 geometry')
  marker_sets["particle_73 geometry"]=s
s= marker_sets["particle_73 geometry"]
mark=s.place_marker((1660.83, 2756.68, 1815.53), (0.544776, 0, 0.455224), 402.654)
if "particle_74 geometry" not in marker_sets:
  s=new_marker_set('particle_74 geometry')
  marker_sets["particle_74 geometry"]=s
s= marker_sets["particle_74 geometry"]
mark=s.place_marker((1743.99, 1765.05, 1756.01), (0.552239, 0, 0.447761), 345.464)
if "particle_75 geometry" not in marker_sets:
  s=new_marker_set('particle_75 geometry')
  marker_sets["particle_75 geometry"]=s
s= marker_sets["particle_75 geometry"]
mark=s.place_marker((1874.22, 1968.26, 1457.78), (0.559701, 0, 0.440299), 504.131)
if "particle_76 geometry" not in marker_sets:
  s=new_marker_set('particle_76 geometry')
  marker_sets["particle_76 geometry"]=s
s= marker_sets["particle_76 geometry"]
mark=s.place_marker((961.513, 1809.03, 837.335), (0.567164, 0, 0.432836), 527.566)
if "particle_77 geometry" not in marker_sets:
  s=new_marker_set('particle_77 geometry')
  marker_sets["particle_77 geometry"]=s
s= marker_sets["particle_77 geometry"]
mark=s.place_marker((1282.47, 2137.89, 431.249), (1, 0.7, 0), 268.732)
if "particle_78 geometry" not in marker_sets:
  s=new_marker_set('particle_78 geometry')
  marker_sets["particle_78 geometry"]=s
s= marker_sets["particle_78 geometry"]
mark=s.place_marker((1720.12, 1098.4, 951.649), (0.58209, 0, 0.41791), 355.828)
if "particle_79 geometry" not in marker_sets:
  s=new_marker_set('particle_79 geometry')
  marker_sets["particle_79 geometry"]=s
s= marker_sets["particle_79 geometry"]
mark=s.place_marker((918.053, 1098.55, 1170.13), (0.589552, 0, 0.410448), 430.868)
if "particle_80 geometry" not in marker_sets:
  s=new_marker_set('particle_80 geometry')
  marker_sets["particle_80 geometry"]=s
s= marker_sets["particle_80 geometry"]
mark=s.place_marker((770.255, 898.583, 764.759), (0.597015, 0, 0.402985), 469.868)
if "particle_81 geometry" not in marker_sets:
  s=new_marker_set('particle_81 geometry')
  marker_sets["particle_81 geometry"]=s
s= marker_sets["particle_81 geometry"]
mark=s.place_marker((1616.3, 623.254, 1193.92), (0.604478, 0, 0.395522), 484.462)
if "particle_82 geometry" not in marker_sets:
  s=new_marker_set('particle_82 geometry')
  marker_sets["particle_82 geometry"]=s
s= marker_sets["particle_82 geometry"]
mark=s.place_marker((1600.49, -57.0253, 2091.57), (0.61194, 0, 0.38806), 296.142)
if "particle_83 geometry" not in marker_sets:
  s=new_marker_set('particle_83 geometry')
  marker_sets["particle_83 geometry"]=s
s= marker_sets["particle_83 geometry"]
mark=s.place_marker((1838.97, -95.7418, 2234.55), (0.619403, 0, 0.380597), 615.846)
if "particle_84 geometry" not in marker_sets:
  s=new_marker_set('particle_84 geometry')
  marker_sets["particle_84 geometry"]=s
s= marker_sets["particle_84 geometry"]
mark=s.place_marker((1422.33, 408.325, 2101.13), (0.626866, 0, 0.373134), 350.244)
if "particle_85 geometry" not in marker_sets:
  s=new_marker_set('particle_85 geometry')
  marker_sets["particle_85 geometry"]=s
s= marker_sets["particle_85 geometry"]
mark=s.place_marker((805.918, 71.5635, 2424.42), (0.634328, 0, 0.365672), 428.837)
if "particle_86 geometry" not in marker_sets:
  s=new_marker_set('particle_86 geometry')
  marker_sets["particle_86 geometry"]=s
s= marker_sets["particle_86 geometry"]
mark=s.place_marker((910.685, -790.284, 3079.25), (0.641791, 0, 0.358209), 383.576)
if "particle_87 geometry" not in marker_sets:
  s=new_marker_set('particle_87 geometry')
  marker_sets["particle_87 geometry"]=s
s= marker_sets["particle_87 geometry"]
mark=s.place_marker((387.103, 110.773, 1856.94), (0.649254, 0, 0.350746), 626.421)
if "particle_88 geometry" not in marker_sets:
  s=new_marker_set('particle_88 geometry')
  marker_sets["particle_88 geometry"]=s
s= marker_sets["particle_88 geometry"]
mark=s.place_marker((371.965, 908.391, 1269.83), (0.656716, 0, 0.343284), 320.338)
if "particle_89 geometry" not in marker_sets:
  s=new_marker_set('particle_89 geometry')
  marker_sets["particle_89 geometry"]=s
s= marker_sets["particle_89 geometry"]
mark=s.place_marker((772.148, 741.712, 1955.3), (0.664179, 0, 0.335821), 441.02)
if "particle_90 geometry" not in marker_sets:
  s=new_marker_set('particle_90 geometry')
  marker_sets["particle_90 geometry"]=s
s= marker_sets["particle_90 geometry"]
mark=s.place_marker((1454.02, 384.274, 2376.33), (0.671642, 0, 0.328358), 417.374)
if "particle_91 geometry" not in marker_sets:
  s=new_marker_set('particle_91 geometry')
  marker_sets["particle_91 geometry"]=s
s= marker_sets["particle_91 geometry"]
mark=s.place_marker((939.697, 800.625, 2795.27), (0.679104, 0, 0.320896), 318.477)
if "particle_92 geometry" not in marker_sets:
  s=new_marker_set('particle_92 geometry')
  marker_sets["particle_92 geometry"]=s
s= marker_sets["particle_92 geometry"]
mark=s.place_marker((641.573, 194.105, 3162.1), (0.686567, 0, 0.313433), 326.091)
if "particle_93 geometry" not in marker_sets:
  s=new_marker_set('particle_93 geometry')
  marker_sets["particle_93 geometry"]=s
s= marker_sets["particle_93 geometry"]
mark=s.place_marker((760.374, -590.542, 3489.34), (0.69403, 0, 0.30597), 209.512)
if "particle_94 geometry" not in marker_sets:
  s=new_marker_set('particle_94 geometry')
  marker_sets["particle_94 geometry"]=s
s= marker_sets["particle_94 geometry"]
mark=s.place_marker((1023.79, 247.903, 2552.06), (0.701493, 0, 0.298507), 535.814)
if "particle_95 geometry" not in marker_sets:
  s=new_marker_set('particle_95 geometry')
  marker_sets["particle_95 geometry"]=s
s= marker_sets["particle_95 geometry"]
mark=s.place_marker((714.571, 1267.85, 2414.53), (0.708955, 0, 0.291045), 301.472)
if "particle_96 geometry" not in marker_sets:
  s=new_marker_set('particle_96 geometry')
  marker_sets["particle_96 geometry"]=s
s= marker_sets["particle_96 geometry"]
mark=s.place_marker((387.776, 896.878, 1680.07), (0.716418, 0, 0.283582), 384.507)
if "particle_97 geometry" not in marker_sets:
  s=new_marker_set('particle_97 geometry')
  marker_sets["particle_97 geometry"]=s
s= marker_sets["particle_97 geometry"]
mark=s.place_marker((-214.228, 984.749, 897.563), (0.723881, 0, 0.276119), 486.915)
if "particle_98 geometry" not in marker_sets:
  s=new_marker_set('particle_98 geometry')
  marker_sets["particle_98 geometry"]=s
s= marker_sets["particle_98 geometry"]
mark=s.place_marker((-861.699, 1154.12, 1228.96), (0.731343, 0, 0.268657), 524.901)
if "particle_99 geometry" not in marker_sets:
  s=new_marker_set('particle_99 geometry')
  marker_sets["particle_99 geometry"]=s
s= marker_sets["particle_99 geometry"]
mark=s.place_marker((-794.702, 1100.52, 2660.9), (0.738806, 0, 0.261194), 319.619)
if "particle_100 geometry" not in marker_sets:
  s=new_marker_set('particle_100 geometry')
  marker_sets["particle_100 geometry"]=s
s= marker_sets["particle_100 geometry"]
mark=s.place_marker((140.821, 432.833, 2860.11), (0.746269, 0, 0.253731), 270.974)
if "particle_101 geometry" not in marker_sets:
  s=new_marker_set('particle_101 geometry')
  marker_sets["particle_101 geometry"]=s
s= marker_sets["particle_101 geometry"]
mark=s.place_marker((120.194, 798.242, 1362.62), (0.753731, 0, 0.246269), 325.118)
if "particle_102 geometry" not in marker_sets:
  s=new_marker_set('particle_102 geometry')
  marker_sets["particle_102 geometry"]=s
s= marker_sets["particle_102 geometry"]
mark=s.place_marker((-353.951, 1649.56, 124.408), (0.761194, 0, 0.238806), 780.35)
if "particle_103 geometry" not in marker_sets:
  s=new_marker_set('particle_103 geometry')
  marker_sets["particle_103 geometry"]=s
s= marker_sets["particle_103 geometry"]
mark=s.place_marker((-281.592, 2015.69, -453.687), (0.768657, 0, 0.231343), 635.431)
if "particle_104 geometry" not in marker_sets:
  s=new_marker_set('particle_104 geometry')
  marker_sets["particle_104 geometry"]=s
s= marker_sets["particle_104 geometry"]
mark=s.place_marker((-367.067, 1692.42, -431.548), (0.776119, 0, 0.223881), 388.568)
if "particle_105 geometry" not in marker_sets:
  s=new_marker_set('particle_105 geometry')
  marker_sets["particle_105 geometry"]=s
s= marker_sets["particle_105 geometry"]
mark=s.place_marker((-210.235, 2365.8, -171.349), (0.783582, 0, 0.216418), 480.063)
if "particle_106 geometry" not in marker_sets:
  s=new_marker_set('particle_106 geometry')
  marker_sets["particle_106 geometry"]=s
s= marker_sets["particle_106 geometry"]
mark=s.place_marker((143.866, 2777.7, -965.412), (0.791045, 0, 0.208955), 311.201)
if "particle_107 geometry" not in marker_sets:
  s=new_marker_set('particle_107 geometry')
  marker_sets["particle_107 geometry"]=s
s= marker_sets["particle_107 geometry"]
mark=s.place_marker((-183.511, 3294.06, -1296.66), (0.798507, 0, 0.201493), 400.327)
if "particle_108 geometry" not in marker_sets:
  s=new_marker_set('particle_108 geometry')
  marker_sets["particle_108 geometry"]=s
s= marker_sets["particle_108 geometry"]
mark=s.place_marker((-822.965, 3617.09, -1528.91), (0.80597, 0, 0.19403), 148.304)
if "particle_109 geometry" not in marker_sets:
  s=new_marker_set('particle_109 geometry')
  marker_sets["particle_109 geometry"]=s
s= marker_sets["particle_109 geometry"]
mark=s.place_marker((-1053.51, 2548.72, -1492.7), (0.813433, 0, 0.186567), 578.156)
if "particle_110 geometry" not in marker_sets:
  s=new_marker_set('particle_110 geometry')
  marker_sets["particle_110 geometry"]=s
s= marker_sets["particle_110 geometry"]
mark=s.place_marker((-932.132, 2574.08, -1079.29), (0, 1, 0), 379.812)
if "particle_111 geometry" not in marker_sets:
  s=new_marker_set('particle_111 geometry')
  marker_sets["particle_111 geometry"]=s
s= marker_sets["particle_111 geometry"]
mark=s.place_marker((-787.24, 2471.32, -352.169), (0.828358, 0, 0.171642), 615.253)
if "particle_112 geometry" not in marker_sets:
  s=new_marker_set('particle_112 geometry')
  marker_sets["particle_112 geometry"]=s
s= marker_sets["particle_112 geometry"]
mark=s.place_marker((-1526.26, 2899.11, 1188.93), (0.835821, 0, 0.164179), 447.238)
if "particle_113 geometry" not in marker_sets:
  s=new_marker_set('particle_113 geometry')
  marker_sets["particle_113 geometry"]=s
s= marker_sets["particle_113 geometry"]
mark=s.place_marker((-1491.74, 2593.3, 2336.49), (0.843284, 0, 0.156716), 592.623)
if "particle_114 geometry" not in marker_sets:
  s=new_marker_set('particle_114 geometry')
  marker_sets["particle_114 geometry"]=s
s= marker_sets["particle_114 geometry"]
mark=s.place_marker((-2152.78, 1846.13, 1530.9), (0.850746, 0, 0.149254), 286.752)
if "particle_115 geometry" not in marker_sets:
  s=new_marker_set('particle_115 geometry')
  marker_sets["particle_115 geometry"]=s
s= marker_sets["particle_115 geometry"]
mark=s.place_marker((-2073.39, 1369.89, 668.911), (0.858209, 0, 0.141791), 456.205)
if "particle_116 geometry" not in marker_sets:
  s=new_marker_set('particle_116 geometry')
  marker_sets["particle_116 geometry"]=s
s= marker_sets["particle_116 geometry"]
mark=s.place_marker((-1811.54, 786.62, 100.657), (0.865672, 0, 0.134328), 350.286)
if "particle_117 geometry" not in marker_sets:
  s=new_marker_set('particle_117 geometry')
  marker_sets["particle_117 geometry"]=s
s= marker_sets["particle_117 geometry"]
mark=s.place_marker((-2150.71, 1008.94, -521.493), (0.873134, 0, 0.126866), 491.103)
if "particle_118 geometry" not in marker_sets:
  s=new_marker_set('particle_118 geometry')
  marker_sets["particle_118 geometry"]=s
s= marker_sets["particle_118 geometry"]
mark=s.place_marker((-2760.32, 839.706, 301.187), (0.880597, 0, 0.119403), 543.343)
if "particle_119 geometry" not in marker_sets:
  s=new_marker_set('particle_119 geometry')
  marker_sets["particle_119 geometry"]=s
s= marker_sets["particle_119 geometry"]
mark=s.place_marker((-2915.73, 797.152, -544.366), (0, 1, 0), 329.305)
if "particle_120 geometry" not in marker_sets:
  s=new_marker_set('particle_120 geometry')
  marker_sets["particle_120 geometry"]=s
s= marker_sets["particle_120 geometry"]
mark=s.place_marker((-3128.15, 614.863, -380.69), (0.895522, 0, 0.104478), 544.189)
if "particle_121 geometry" not in marker_sets:
  s=new_marker_set('particle_121 geometry')
  marker_sets["particle_121 geometry"]=s
s= marker_sets["particle_121 geometry"]
mark=s.place_marker((-2862.54, 202.299, 605.064), (0.902985, 0, 0.0970149), 537.887)
if "particle_122 geometry" not in marker_sets:
  s=new_marker_set('particle_122 geometry')
  marker_sets["particle_122 geometry"]=s
s= marker_sets["particle_122 geometry"]
mark=s.place_marker((-3662.09, -380.332, 508.247), (0.910448, 0, 0.0895522), 363.103)
if "particle_123 geometry" not in marker_sets:
  s=new_marker_set('particle_123 geometry')
  marker_sets["particle_123 geometry"]=s
s= marker_sets["particle_123 geometry"]
mark=s.place_marker((-3946.27, -1098.83, 1018.42), (0.91791, 0, 0.0820896), 344.703)
if "particle_124 geometry" not in marker_sets:
  s=new_marker_set('particle_124 geometry')
  marker_sets["particle_124 geometry"]=s
s= marker_sets["particle_124 geometry"]
mark=s.place_marker((-3261.47, -1073.01, 1132.07), (0.925373, 0, 0.0746269), 333.747)
if "particle_125 geometry" not in marker_sets:
  s=new_marker_set('particle_125 geometry')
  marker_sets["particle_125 geometry"]=s
s= marker_sets["particle_125 geometry"]
mark=s.place_marker((-3247.89, -225.714, 1001.21), (0.932836, 0, 0.0671642), 489.792)
if "particle_126 geometry" not in marker_sets:
  s=new_marker_set('particle_126 geometry')
  marker_sets["particle_126 geometry"]=s
s= marker_sets["particle_126 geometry"]
mark=s.place_marker((-2498.13, -311.545, 1426.41), (0.940299, 0, 0.0597015), 349.609)
if "particle_127 geometry" not in marker_sets:
  s=new_marker_set('particle_127 geometry')
  marker_sets["particle_127 geometry"]=s
s= marker_sets["particle_127 geometry"]
mark=s.place_marker((-2224.41, -767.291, 757.614), (0.947761, 0, 0.0522388), 499.774)
if "particle_128 geometry" not in marker_sets:
  s=new_marker_set('particle_128 geometry')
  marker_sets["particle_128 geometry"]=s
s= marker_sets["particle_128 geometry"]
mark=s.place_marker((-2980.52, -360.919, 563.543), (0.955224, 0, 0.0447761), 494.995)
if "particle_129 geometry" not in marker_sets:
  s=new_marker_set('particle_129 geometry')
  marker_sets["particle_129 geometry"]=s
s= marker_sets["particle_129 geometry"]
mark=s.place_marker((-2684.93, -185.093, 1221.96), (0.962687, 0, 0.0373134), 382.35)
if "particle_130 geometry" not in marker_sets:
  s=new_marker_set('particle_130 geometry')
  marker_sets["particle_130 geometry"]=s
s= marker_sets["particle_130 geometry"]
mark=s.place_marker((-3176.49, -86.6327, 728.719), (0.970149, 0, 0.0298507), 295.127)
if "particle_131 geometry" not in marker_sets:
  s=new_marker_set('particle_131 geometry')
  marker_sets["particle_131 geometry"]=s
s= marker_sets["particle_131 geometry"]
mark=s.place_marker((-3268.55, 212.853, 81.1734), (0.977612, 0, 0.0223881), 320.803)
if "particle_132 geometry" not in marker_sets:
  s=new_marker_set('particle_132 geometry')
  marker_sets["particle_132 geometry"]=s
s= marker_sets["particle_132 geometry"]
mark=s.place_marker((-3608.31, -129.293, 58.6564), (0.985075, 0, 0.0149254), 326.218)
if "particle_133 geometry" not in marker_sets:
  s=new_marker_set('particle_133 geometry')
  marker_sets["particle_133 geometry"]=s
s= marker_sets["particle_133 geometry"]
mark=s.place_marker((-3409.36, 446.167, 380.427), (0.992537, 0, 0.00746269), 368.644)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
