import ogr


def Get_XY_fromshp(ori_shp):

    X, Y, Fid = [], [], []

    ds = ogr.Open(ori_shp,0)
    in_layer = ds.GetLayer(0)
    global feature_num,X_Line,Y_Line
    feature_num = in_layer.GetFeatureCount()

    for in_feature in in_layer:
        # print('in_feature:',in_feature)

        geom = in_feature.geometry()
        # print(geom)
        # print(type(geom))
        wkt = geom.ExportToWkt()

        pointstring = wkt[wkt.rfind('(') + 1:wkt.find(')')].split(',')

        x, y = [],[]
        for point_value in pointstring:


            xy = point_value.split(' ')

            x += [float(xy[0]) / 10 ** 4]
            y += [float(xy[1])]
        X.append(x), Y.append(y)
            # print(x)
        # geom = in_feature.geometry()
        # print(geom)
        # if geom.GetGeometryName() != 'MULTILINESTRING':
        #     Coords = geom.GetPoints()
        #     # print(Coords)
        #     x, y = zip(*Coords)
        #     # print(x)
        #     # print(y)
        #     X.append(x), Y.append(y)
        # else:
        #     LineString = geom.GetGeometryRef(0)
        #     # mLineString = LineString.GetGeometryRef(0)
        #     Coords = LineString.GetPoints()
        #     # print(Coords)
        #     x, y = zip(*Coords)
        #     # print(x)
        #     # print(y)
        #     X.append(x), Y.append(y)


        # Fid.append(in_feature.GetField('FID'))

    X_Line,Y_Line= X,Y
    # print(len(X),feature_num)
    # print(X_Line)
    # print(Y_Line)
    ds.Destroy()
    return feature_num,X,Y

# Get_XY_fromshp(r'D:\2021\04. 空间数据安全组\10. DNA加密稿子\05. Test data\test data zizhi\DNA2_New_Shapefile.shp')
# [[-2.3518862854675622e+198, -9.483169386287282e-192, -1.0034288027524025e-119, -6.47016335307632e-07, -2.623929552377278e-175, 1.7623163258349767e+61, -6.794630209369066e-232, -5.21479449065727e+255, 5.724505711997762e+62, -4.1405483254733663e-103], [-3.012888894686321e+37, 3.4307942070623535e-99, 2.0418605394885206e+130, 9.454504117290347e-167, -4.5824116711890626e+297, -4.021153399153466e-61, -1.4757144923640834e+35, 3.000263247207457e-173, -2.374049810040157e-109, 1.7249188582491543e+180, -3.494149400243217e-13, -2.176394654470504e-281, 9.260532878041395e-101, -1.2579334052697e+180, -1.5778300938212873e+145], [1.9924766044931725e-97, -9.04546376663126e-140, 4.740513011596128e+203, 1.102371470338441e+255, 6.554837998603599e-10, 5.028444902047754e+202, 3.4878980842112485e-216, -8496023841.696965, 1.2243196330754146e+205, 6.261102523016961e+247, -5.381568311019293e-195, 3.0872137303449273e+22, 4.582321921193539e+125, -1.9113444768218848e+303, 6.49866621635052e-142], [-6.8076723394794164e+274, 5.1618533619553415e-279, -1.552244537810984e-127, 1.8773151867955568e-194, 2.65575615437262e-236, 4.449765321463122e-236, -1.1854923509694775e+137, -1.3714610317739711e-42, -3.598279040233794e+97, -8.798340106117502e+141]]
# [[-6.007712715941119e+203, -1.351543439299075e-176, 3.660397654647021e-134, -1.0025566495495426e-12, -5.323216124964334e-193, 1.6147537592716488e+74, -2.7935825797082166e-248, 3.7491867518486876e+261, -5.756724471089276e+73, -7.310897642601528e-108], [-9.28811839779767e+21, 4.4287774633225684e-113, 1.0632308648814335e+121, -9.677671640915778e-163, 4.444947458295711e+303, -4.7653224072360945e-76, -2.227557046933855e+22, -5.4326536480829355e-158, 3.7950221108169873e-104, -1.137999819966123e+188, -8.59317046948005e-07, 1.338441354778793e-277, -7.027714772402731e-116, -9.127280691992529e+185, -1.4872441330247471e+144], [1.9744462571673294e-115, -9.928721565654558e-154, -4.9869597526930624e+200, 8.58210214577636e+265, -7.227438907010577e-14, 1.2219762146371775e+202, 3.2310836610218903e-231, -124729975269.86348, 1.3219747871640996e+200, -1.6141090662316683e+233, -3.0230000432941093e-210, 1.5298538912588649e+37, 1.2053562319888895e+121, 5.759720809040194e+296, 2.4831468548892598e-148], [-6.992218004452318e+288, 2.1326050294092685e-280, 5.9994373838628625e-124, -3.863311756548409e-210, -1.9312546402643594e-249, 2.7469418730630388e-250, -1.821842761828431e+151, -6.72890753955752e-54, -7.091229968177162e+113, 7.894859659084751e+148]]

# a = [[-8797431513506206065, -8864158392275332821, -8767442837017677629, -8669914156346476965, -8866818491078076366, -8723130130382024851, -8824259692811702129, 8793563065099668096, 9208862964140272155, 8764184993859418799], [-9188593682863244274, -8699508722728171097, -8867247334707998675, -9169090833673522142, -8914531503627099266, -9009441729228541865, -8677045952058073626, -8773884263793491485, -9159891328071273858, -8730339633358897862, 9162050629201238071, -8831181195468910354, -8679576317308587357, -8794726813388322617, -8838857183685224989], [-8734844324588921118, -8925533595199481869, -8705813810699052558, -8729843477881715369, -8668447008930729990, -9043268254045097298, -8883936253779839534, -8925070511237476438, -9190420887112438426, -9165376035819725569, -9163063459534464865, -9200458198760949372, -9019844225181306062, -8682965148366641569, -8741177628800321374], [-9209195085087413590, -9197578139931998272, -8839145415086872310, -8825915063116575186, -8792322463469500269, -8889202413392515257, -8754843374360896034, -9160566396127137061, -8747134109760269194, -8724647859175423809]]
# b = [[8797640719014009322, 8866634251324161658, 8764284933596536634, 8671380203526402275, -8867166694141194954, -8720512618535324718, -8823573795095691622, -8794507318122793493, -9206016154900164286, -8767438624275252033], [9187530162477821162, 8696854037224128583, 8865081706972133905, 9167769719824417503, -8915996810527866943, -9010574360524031194, -8674961612658172590, -8783664105399341245, -9159965889638977689, -8730378831247518573, -9162516976326724613, -8830332798335197721, -8679336072858936458, -8792932296989216142, -8830604303508478142], [8732306114992975254, 8933422577729006483, -8701035429551516194, -8726178835616290222, -8672780044731443502, -9055508455407468558, -8890651417413222982, -8921986079391474675, -9203815786614370867, -9167856704297362106, -9162288353443736513, -9198350350443481461, -9024046746074886253, -8693146924743283782, -8746010845341227841], [9218817439584604839, 9188574627674850250, 8829453446009533518, 8813852768537030090, -8801746039708175481, -8895392841893355909, -8744623432841936778, -9160710707018363558, -8739333388238586386, -8735053962809047210]]

# feature_num,X,Y = Get_XY_fromshp(r'D:\2020\09. 混沌加密算法稿子\05. Test data\test data zizhi\DNA_New_Shapefile.shp')
#
# Enx = [[-518833101356.2902, -533711107237.3005, -414590122489.395, -266160666353.99194, -964173924030.6809, -935162689937.9663, -446619725769.49994, -350337695652.02814, -1055461535882.341, -137626355449.48456], [-848857836741.8881, -40494017550.65238, -1091763177579.68, -370615140805.22766, 367710327965.0476, -400382517113.0271, -817464412338.6573, -336737076904.3372, -475021227028.46674, -849300187351.6854, -108059611106602.48, -860613922192.7202, 499758652957.2768, -971869695589.1271, -274223897659.893], [-753982876702.9738, -365312823441.0015, -107911624421420.44, -978105324982.6779, -201098016731.1167, -30939748945.005398, -204611451529.1152, -664918344770.0771, -850238361931.1545, 195139307202.88144, -940484093481.5187, -543402466915.29504, -140639200578.64658, -196539116382.11804, -1024254957625.7347], [-475211379213.4081, -637755500417.8752, -691105539597.6202, -937713208401.6122, 293776191284.16, -340870832648.6494, -396873036971.2301, -992019765787.744, -39552247707.77449, -225591326220.9431]]
# Eny = [[-338190163813.35767, -344309104560.06, 373894679748.00775, -260473924988.99234, -499859962411.4269, -976280306104.9641, -423343411756.4734, 333816704453.3344, 541846162056.53644, -970209170849.498], [-5677669811.43477, -975315277087.2716, -1051654258298.3848, 345847129488.19714, -511306321164.35693, -33668758244.755398, -524525729966.7439, 526763157557.2895, 341423034389.1377, 525038211985.3812, -225681949937.54956, 385479339787.4638, -404566675512.01825, -244312685571.11417, -381589556586.2062], [-182978876197.90625, -338836688988.3317, 526253371822.08466, -400442817235.66406, 382360964222.02515, -1092791059095.7822, -20143024472.82588, -8804963146.188335, -693096645607.2325, -342088106623.18884, -877242469983.1642, -21059094358.761192, -800492710623.219, 445624258819.41266, -127028752426.87813], [-204845842140.10358, -1014200389037.9756, 216266907806.61334, 140446011421.9975, -491418521137.36945, -1059929342586.3767, -285238606034.13104, -157602703870.0907, -432928168642.49304, 508985836733.347]]
#
# for x,enx in zip(X,Enx):
#     for xx, enxx in zip(x, enx):
#         if xx == enxx: print(True)
#         else: print(False, xx, enxx)
