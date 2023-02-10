from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from Initial_Value import Initial_Parmeter
from D4_hyper_chaotic import D4_Hyper_Chaotic


def Index_Sort(path,user_key):

    u1, u2, x1, x2, Hx_Index,Hy_Index,L_num = \
        Initial_Parmeter(path,user_key)
    global Track_L
    # L =  Read_Vector_File.feature_num
    # print(u1,u2,x1,x2)


    t = np.arange(0, 100+L_num, 1)
    '''t = np.arange(0, 50+L, 1)   程序调试完成需要继续修改'''
    track1 = odeint(D4_Hyper_Chaotic, (u1,u2,x1,x2), t, args=(10,28,8/3,1,16))
    # print(track1)
    # print(type(track1))
    # print(len(track1[1000:]))
    # print(track1[1000:])
    Track_L = track1[100:]
    ''' Track_L = track1[50:]  程序调试完成需要继续修改    '''
    # print(Track_L,'\n')

    Track_Sort = np.sort(Track_L,axis=0)
    # print(Track_Sort,'\n')

    Track_Sort_Index = np.argsort(Track_L,axis=0)
    # print(Track_Sort_Index)
    # print(Track_Sort_Index[:,0])

    A1,A2,A3,A4,A5,A6 = \
        Track_Sort_Index[:,[0,1]],Track_Sort_Index[:,[0,2]],Track_Sort_Index[:,[0,3]],\
        Track_Sort_Index[:,[1,2]],Track_Sort_Index[:,[1,3]],Track_Sort_Index[:,[2,3]]

    if Hx_Index == 1:
        Hx_Index_Sequence = A1
    elif Hx_Index == 2:
        Hx_Index_Sequence = A2
    elif Hx_Index == 3:
        Hx_Index_Sequence = A3
    elif Hx_Index == 4:
        Hx_Index_Sequence = A4
    elif Hx_Index == 5:
        Hx_Index_Sequence = A5
    elif Hx_Index == 6:
        Hx_Index_Sequence = A6
    if Hy_Index == 1:
        Hy_Index_Sequence = A1
    elif Hy_Index == 2:
        Hy_Index_Sequence = A2
    elif Hy_Index == 3:
        Hy_Index_Sequence = A3
    elif Hy_Index == 4:
        Hy_Index_Sequence = A4
    elif Hy_Index == 5:
        Hy_Index_Sequence = A5
    elif Hy_Index == 6:
        Hy_Index_Sequence = A6

    # print(Hx_Index_Sequence)
    # print(Hy_Index_Sequence)
    # print(Track_L)
    return Hx_Index_Sequence,Hy_Index_Sequence,Track_L
# print(A1)
# print(Track_Sort_Index[:,[0,2]])
# print(H_Index)
# Time_Start = time.time()
# path = r'D:\2020\09. 混沌加密算法稿子\05. Test data\test data zizhi\DNA_New_Shapefile.shp'
# Index_Sort(path,'user_key')
# Time_End = time.time()

# print(Time_End-Time_Start)



