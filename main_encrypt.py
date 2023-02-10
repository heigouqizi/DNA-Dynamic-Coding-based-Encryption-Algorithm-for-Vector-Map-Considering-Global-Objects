import os
import numpy as np
from vector_file_operation import Get_XY_fromshp
from vector_file_operation import write_encrytpion_shp
from dna_encoding import dna_encrypt
from dna_encoding import dna_decrypt
from Double_Random_PP import DRPP
from IDouble_Random_PP import IDRPP

if __name__ == '__main__': 
    os.chdir(r'D:\2021\04. 空间数据安全组\10. DNA加密稿子\05. Test data\test data zizhi')
    '''数据A'''
    # ori_shp = 'polyline_A.shp'
    # en_shp, de_shp = 'results/en_polyline_A.shp', 'results/de_polyline_A_key2.shp'
    '''数据B'''
    ori_shp = 'New_Shapefile.shp'
    drpp_shp, en_shp, de_shp = 'DRPP_New_Shapefile.shp', 'DNA_New_Shapefile.shp', 'IDNA_New_Shapefile.shp'
    '''数据C'''
    # ori_shp = 'polygon_B.shp'
    # en_shp, de_shp = 'results/en_polygon_B.shp', 'results/de_polygon_B_key2.shp'

    feature_num, Points = Get_XY_fromshp(ori_shp)
    DRPP_Points = DRPP(ori_shp, user_key="cdxy2020")
    E_Points = []
    vertice_num = 0
    En_X, En_Y = [], []
    # 加密方法1：要素内加密
    for i in range(len(DRPP_Points)):
        X, Y = [], []
        for j in range(len(DRPP_Points[i])):
            X.append(DRPP_Points[i][j][0])
            Y.append(DRPP_Points[i][j][1])
            vertice_num += 1    
        E_X = dna_encrypt(X,user_key='cdxy2020')
        E_Y = dna_encrypt(Y,user_key='cdxy2020')
        e_point = [(E_X[k], E_Y[k]) for k in range(len(E_X))]
        E_Points.append(e_point)        
    # print('要素数量：',feature_num)  
    # print('顶点数量：',vertice_num)  
    write_encrytpion_shp(ori_shp, en_shp, E_Points)    
    # 解密
    feature_num, En_Points = Get_XY_fromshp(en_shp)
    # En_Points = E_Points
    De_Points = []
    De_X, De_Y = [], []
    for i in range(len(En_Points)):
        En_X, En_Y = [], []
        for j in range(len(En_Points[i])):
            En_X.append(En_Points[i][j][0]) 
            En_Y.append(En_Points[i][j][1])  
        D_X = dna_decrypt(En_X,user_key='cdxy2020')
        D_Y = dna_decrypt(En_Y,user_key='cdxy2020')
        de_point = [(D_X[k], D_Y[k]) for k in range(len(En_X))]
        De_Points.append(de_point)

    write_encrytpion_shp(ori_shp, drpp_shp, De_Points)
    IDRPP_Points = IDRPP(drpp_shp, user_key='cdxy2020')
    # print(Points)
    # print(IDRPP_Points)
    write_encrytpion_shp(ori_shp, de_shp, IDRPP_Points)
    print('完成加解密！')