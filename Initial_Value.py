import numpy as np
import os,math,hashlib,re
import Read_Vector_File
# import Read_Vector_Polygon


def gene_hashkey(user_key):
    # 密钥K的生成
    sha = hashlib.sha512()
    sha.update(user_key.encode('utf-8'))
    Devide_64_8bits = \
        np.array(re.findall(r'.{2}', hashlib.sha512().hexdigest()))
    Devide_4_16group = Devide_64_8bits.reshape((16,4))
    return Devide_4_16group

def SHA512_File(path):
    global start, end  # 声明全局变量
    size = os.path.getsize(path)  # 获取文件大小，单位是字节（byte）
    with open(path, 'rb') as f:  # 以二进制模式读取文件
        while size >= 1024 * 1024:  # 当文件大于1MB时将文件分块读取
            hashlib.sha512().update(f.read(1024 * 1024))
            size -= 1024 * 1024
        hashlib.sha512().update(f.read())
    Devide_64_8bits = \
        re.findall(r'.{2}', hashlib.sha512().hexdigest())

    # print(Devide_64_8bits)
    # print(int('0b'.upper(),16))
    return Devide_64_8bits

def Hex_int(path, user_key):
    Int_64_8bits, Int_16group = [], []
    Devide_64_8bits = SHA512_File(path)
    Devide_4_16group = gene_hashkey(user_key)
    # print(Devide_64_8bits)
    # print(len(Devide_64_8bits))
    for hex_int in Devide_64_8bits:
        Int_64_8bits.append(int(hex_int,16))
    # print(Int_64_8bits)
    # print(len(Int_64_8bits))
    for group in Devide_4_16group[:16]:
        for hex_int in group:
            Int_16group.append(int(hex_int,16))

    Int_16group = np.array(Int_16group).reshape((16,4))
    # print(Int_16group)
    return Int_64_8bits,Int_16group


def Initial_Parmeter(path, user_key):
    global u1,u2
    Int_64_8bits, Int_16group = Hex_int(path, user_key)
    # L = Read_Vector_File.feature_num
    L, X, Y = Read_Vector_File.Get_XY_fromshp(path)
    L_num = 0
    for i in range(len(X)):
        L_num += len(X[i])
    # print(L_num)
    Int_64_8bits_array = np.array(Int_64_8bits)
    k01_16,k17_32,k33_48,k49_64 = \
        Int_64_8bits_array[:16],Int_64_8bits_array[16:32],\
        Int_64_8bits_array[32:48],Int_64_8bits_array[48:64]
    k01_16xor,k17_32xor,k33_48xor,k49_64xor = \
        k01_16[0],k17_32[0],k33_48[0],k49_64[0]

    Uk_Sum = np.sum(Int_16group)
    Uk_Index = Uk_Sum % 16 +1

    H_sum = np.sum(Int_64_8bits_array)
    Hx_Index = H_sum % 6 + 1


    e1, e2, e3, e4 = \
        Int_16group[Uk_Index-1][0], Int_16group[Uk_Index-1][1], \
        Int_16group[Uk_Index-1][2], Int_16group[Uk_Index-1][3]

    for i in range(1,len(k01_16)):
        k01_16xor = k01_16xor ^ k01_16[i]
        k17_32xor = k17_32xor ^ k17_32[i]
        k33_48xor = k33_48xor ^ k33_48[i]
        k49_64xor = k49_64xor ^ k49_64[i]
    k17_32sum = np.sum(k17_32)
    k17_32max = np.max(k17_32)

    p1 = e1 + (k01_16xor + k17_32xor) / L_num
    p2 = e2 + (k33_48xor + k49_64xor) / L_num
    p3 = e3 + (k01_16xor + k17_32sum) / L_num
    p4 = (e4 * k17_32sum / k17_32max) * L_num

    u1 = (((p1 + p2 +p3 ) * 10**5) % 512) / 512
    u2 = (((p2 + p3 + p4) * 10 ** 5) % 512) / 512
    x1 = (((p1 + p2 + p3 + p4) * 10 ** 5) % 512) / 512
    x2 = (((p1 + p4) * 10 ** 5) % 512) / 512

    Hy_Index = math.floor((((p1 + p2 + p3 + p4) / 4) * 10**6) % 6 + 1)

    # print(u1,u2,x1,x2)
    # print(Hy_Index)
    return u1, u2, x1, x2, Hx_Index,Hy_Index,L_num

# 0.724609375


'''
    十六进制转二进制  并将其划分为64个8位
    Hex_Bin = bin(int(algorithm.hexdigest(),16))[2:].zfill(512)

    Devide_8bit = re.findall(r'.{8}',Hex_Bin)
    print(Devide_8bit)


    print()
    print(Hex_Bin)
    print(len(Hex_Bin))
'''




#
# if __name__=='__main__':
# # #
# # #
#    path = r'D:\2020\09. 混沌加密算法稿子\05. Test data\test data zizhi\gis_osm_railways_free_1.shp'
# #    # SHA_File(path,hashlib.sha512())
# #    # Hex_int(path, 'hashlib.sha512()')
#    Initial_Parmeter(path, 'user_key')
#    # gene_hashkey('user_key')





