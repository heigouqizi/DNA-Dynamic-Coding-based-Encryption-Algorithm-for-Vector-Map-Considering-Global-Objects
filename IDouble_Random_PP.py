from Index_Choice import Index_Sort
# import Read_Vector_File,math,Read_Vector_Polygon
import numpy as np
from vector_file_operation import Get_XY_fromshp

def IDRPP(path,user_key):
    Hx_Index_Sequence,Hy_Index_Sequence,Track_L = Index_Sort(path,user_key)
    '''# print(Hx_Index_Sequence[:,0],'\n','=============================','\n',Hx_Index_Sequence[:,1])
    print(Hy_Index_Sequence[:,0],'\n','=============================','\n',Hy_Index_Sequence[:,1])'''

    L, Points = Get_XY_fromshp(path)
    # print(X)
    # print(Y)

    # X_All, Y_All, XY_num = [], [], []
    # a = 0
    # for x,y in zip(X,Y):
    #     a += len(x)
    #     XY_num.append(a)
    #     # print(XY_num)
    #     for xx,yy in zip(x,y):
    #         X_All.append(xx)
    #         Y_All.append(yy)

    XX, YY = [], []
    for i in range(len(Points)):
        X, Y = [], []
        for j in range(len(Points[i])):
            X.append(Points[i][j][0])
            Y.append(Points[i][j][1])
        XX.append(X)
        YY.append(Y)
    # print(XX)
    # print(YY)

    X_All, Y_All, XY_num = [], [], []
    a = 0
    for x, y in zip(XX, YY):
        a += len(x)
        XY_num.append(a)
        # print(XY_num)
        for xx, yy in zip(x, y):
            X_All.append(xx)
            Y_All.append(yy)
    # print(X_All)
    # print(Y_All)

    # print(X_All)
    # print(Y_All)

    # C_x = [X_All[i] for i in Hx_Index_Sequence[:,0]]
    # S_x = [C_x[j] for j in Hx_Index_Sequence[:,1]]
    # C_y = [Y_All[i] for i in Hx_Index_Sequence[:,0]]
    # S_y = [C_y[j] for j in Hx_Index_Sequence[:, 1]]

    # print(S_x)
    # print(S_y)
    # print(Y_All)

    I_Sx, I_Cx = [None] * len(Hx_Index_Sequence), [None] * len(Hx_Index_Sequence)
    I_Sy, I_Cy = [None] * len(Hx_Index_Sequence), [None] * len(Hx_Index_Sequence)
    m = 0
    for i in Hx_Index_Sequence[:, 1]:
        I_Sx[i] = X_All[m]
        I_Sy[i] = Y_All[m]
        m += 1

    # print(I_Sx)
    # print(I_Sy)

    n = 0
    for i in Hx_Index_Sequence[:, 0]:
        I_Cx[i] = I_Sx[n]
        I_Cy[i] = I_Sy[n]
        n += 1
    # 这是双随机位置换的反运算。

    # print(I_Cx)
    # print(I_Cy)

    IDRPP_X, IDRPP_Y = [], []
    IDRPP_Points = []
    for i in range(len(XY_num)):
        if i == 0:
            IDRPP_X.append(I_Cx[0:XY_num[i]])
            IDRPP_Y.append(I_Cy[0:XY_num[i]])
        else:
            IDRPP_X.append(I_Cx[XY_num[i - 1]:XY_num[i]])
            IDRPP_Y.append(I_Cy[XY_num[i - 1]:XY_num[i]])

    for i in range(len(IDRPP_X)):
        drpp_point = [(IDRPP_X[i][k], IDRPP_Y[i][k]) for k in range(len(IDRPP_X[i]))]
        IDRPP_Points.append(drpp_point)
    # print(I_Cx)
    # print(IDRPP_X)
    # print(IDRPP_Y)
    # print(IDRPP_Points)

    return IDRPP_Points


#
# path = r'D:\2020\09. 混沌加密算法稿子\05. Test data\test data zizhi\DRPP_Test_Polygon_MUltToPolygon.shp'
# IDRPP(path,'user_key')
# L, X, Y = \
#         Read_Vector_Polygon.Get_XY_fromshp(r'D:\2020\09. 混沌加密算法稿子\05. Test data\test data zizhi\Test_Polygon_MUltToPolygon.shp')
# print(X)
# print(Y)
# DNA_Encryption(path,'user_key')

# [[-295577030292.45, -298718672094.516, -295436073215.765], [-435062819868.663, -502591654504.766, -586725940280.893, -349821504016.533], [-179338872312.273, -334323082952.509, -401851917588.612, -298718672094.516, -295577030292.45, -295436073215.765, -240374473176.952], [-240374473176.952, -435062819868.663, -187088082844.285], [-566799398912.863, -287827819760.438, -295436073215.765, -298718672094.516, -477129962756.727, -454989361236.693, -490414323668.747], [-261259097936.398, -532481466556.811, -677502406513.032, -585618910204.892]]
# [[23801146634.0367, 24050179215.9078, 25996049685.2703], [226387650542.345, -93544041422.1425, -91329981270.1391, 199818928718.304], [-30443327090.0463, -84687800814.1289, -37085507546.0564, 24050179215.9078, 23801146634.0367, 25996049685.2703, 58635657955.701], [58635657955.701, 226387650542.345, 90222951194.1376], [53690958686.0816, 144467424918.22, 25996049685.2703, 24050179215.9078, 38192537622.0581, 167715056514.255, -9409755646.01413], [89115921118.1357, 146681485070.224, 176571297122.269, 293916485178.448]]
