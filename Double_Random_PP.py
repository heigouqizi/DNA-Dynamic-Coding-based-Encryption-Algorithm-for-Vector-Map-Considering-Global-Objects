from Index_Choice import Index_Sort
# import Read_Vector_File,math
# import Read_Vector_Polygon
import numpy as np
from vector_file_operation import Get_XY_fromshp

def DRPP(path,user_key):
    Hx_Index_Sequence,Hy_Index_Sequence,Track_L = Index_Sort(path,user_key)
    '''# print(Hx_Index_Sequence[:,0],'\n','=============================','\n',Hx_Index_Sequence[:,1])
    print(Hy_Index_Sequence[:,0],'\n','=============================','\n',Hy_Index_Sequence[:,1])'''

    L, Points = Get_XY_fromshp(path)
    # print(X)
    # print(Y)
    # print(Points)

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
    for x,y in zip(XX,YY):
        a += len(x)
        XY_num.append(a)
        # print(XY_num)
        for xx,yy in zip(x,y):
            X_All.append(xx)
            Y_All.append(yy)
    # print(X_All)
    # print(Y_All)

    C_x = [X_All[i] for i in Hx_Index_Sequence[:,0]]
    S_x = [C_x[j] for j in Hx_Index_Sequence[:,1]]
    C_y = [Y_All[i] for i in Hx_Index_Sequence[:,0]]
    S_y = [C_y[j] for j in Hx_Index_Sequence[:, 1]]

    '''I_Sx, I_Cx = [None] * len(Hx_Index_Sequence), [None] * len(Hx_Index_Sequence)
    I_Sy, I_Cy = [None] * len(Hx_Index_Sequence), [None] * len(Hx_Index_Sequence)
    m = 0
    for i in Hx_Index_Sequence[:, 1]:
        I_Sx[i] = S_x[m]
        I_Sy[i] = S_y[m]
        m += 1

    # print(I_Sx)
    # print(I_Sy)

    n = 0
    for i in Hx_Index_Sequence[:, 0]:
        I_Cx[i] = I_Sx[n]
        I_Cy[i] = I_Sy[n]
        n += 1
        # 这是双随机位置换的反运算。

    print(I_Cx)
    # print(X_All)
    print(I_Cy)
    # print(Y_All)'''

    DRPP_X, DRPP_Y = [], []
    DRPP_Points = []
    for i in range(len(XY_num)):
        if i == 0:
            DRPP_X.append(S_x[0:XY_num[i]])
            DRPP_Y.append(S_y[0:XY_num[i]])
        else:
            DRPP_X.append(S_x[XY_num[i - 1]:XY_num[i]])
            DRPP_Y.append(S_y[XY_num[i - 1]:XY_num[i]])

    for i in range(len(DRPP_X)):
        drpp_point = [(DRPP_X[i][k], DRPP_Y[i][k]) for k in range(len(DRPP_X[i]))]
        DRPP_Points.append(drpp_point)

    # print(DRPP_X)
    # print(DRPP_Y)
    # print(DRPP_Points)
    return DRPP_Points


#
# path = r'D:\2020\09. 混沌加密算法稿子\05. Test data\test data zizhi\Test_Polygon_MUltToPolygon.shp'
# DRPP(path,'user_key')
# DNA_Encryption(path,'user_key')


