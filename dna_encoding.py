import hashlib
import numpy as np
from dfloat_to_bin import dec2bin
from dfloat_to_bin import realNum2bin
from dfloat_to_bin import bin2realNum

'''利用SHA-512方法生成长度为128的哈希序列'''
def gene_hashkey(user_code):
    sha = hashlib.sha512()
    sha.update(user_code.encode('utf-8'))
    hash_key = sha.hexdigest()
    key_lst = [int(i, 16) for i in list(hash_key)]
    return key_lst

'''生成用于加密的二进制密钥流，将哈希序列二进制化并拼接，'''
def gene_keystream(user_code):    
    key_lst = gene_hashkey(user_code)
    key_bin_lst = [dec2bin(key_lst[i]) for i in key_lst]
    keyStr_lst = [0]*len(key_bin_lst)
    for i in range(len(key_bin_lst)):
        keyStr_lst[i] = ''.join([str(j) for j in key_bin_lst[i]])
    keyStream = ''.join([str(i) for i in keyStr_lst])    
    return keyStream

def dna_encrypt(x_lst,user_key):
    user_code = user_key
    keyStream = gene_keystream(user_code)    
    # dna编码规则中的方案1(A:00 C:01 G:10 T:11)和方案7(A:11 G:01 C:10 T:00)
    dna1_dict = {'00': 'A', '01': 'G', '10': 'C', '11': 'T'} # 方案a
    dna7_dict = {'A': '11', 'G': '01', 'C': '10', 'T': '00'} # 方案b
    dna_add = {'AA': 'A', 'AG': 'G', 'AC': 'C', 'AT': 'T',
               'GA': 'G', 'GG': 'C', 'GC': 'T', 'GT': 'A',
               'CA': 'C', 'CG': 'T', 'CC': 'A', 'CT': 'G',
               'TA': 'T', 'TG': 'A', 'TC': 'G', 'TT': 'C'}    
    xe_lst = []
    # 根据每个要素上的顶点个数确定加密密钥
    k = keyStream[len(x_lst) % 52: len(x_lst) % 52 + 52]    
    for i in range(len(x_lst)):        
        # 按照dna编码规则中的方案a(a = 1)对密钥K进行编码
        k_dna = ''.join([dna1_dict[k[i] + k[i+1]] for i in range(0, len(k), 2)])
        x_b = realNum2bin(x_lst[i])
        x_S, x_E, x_M = x_b[0], x_b[1: 12], x_b[12:]
        x_dna = ''.join([dna1_dict[str(x_M[i]) + str(x_M[i+1])] for i in range(0, len(x_M), 2)])
        # 按照方案a对应的加法方案进行dna加法运算
        x_add_dna = ''.join([dna_add[k_dna[i] + x_dna[i]] for i in range(len(x_dna))])        
        # 使用方案b(b = 7 != a)对x_add_dna解码，得到加密后的二进制x坐标
        xe_b = str(x_S) + ''.join([str(i) for i in x_E]) + ''.join([dna7_dict[x_add_dna[i]] for i in range(len(x_add_dna))])
        xe_d = bin2realNum(list(map(int, list(xe_b))))
        xe_lst.append(xe_d)
    return xe_lst


def dna_decrypt(xe_lst,user_key):
    user_code = user_key
    keyStream = gene_keystream(user_code)
    # dna编码规则
    dna1_dict = {'00': 'A', '01': 'G', '10': 'C', '11': 'T'} # 方案a
    dna1_dict_anti = {'A': '00', 'G': '01', 'C': '10', 'T': '11'}
    dna7_dict = {'11': 'A', '01': 'G', '10': 'C', '00': 'T'} # 方案b    
    dna_sub = {'AA': 'A', 'AG': 'T', 'AC': 'C', 'AT': 'G',
               'GA': 'G', 'GG': 'A', 'GC': 'T', 'GT': 'C',
               'CA': 'C', 'CG': 'G', 'CC': 'A', 'CT': 'T',
               'TA': 'T', 'TG': 'C', 'TC': 'G', 'TT': 'A'}
    x_lst = []
    k = keyStream[len(xe_lst) % 52: len(xe_lst) % 52 + 52]
    for i in range(len(xe_lst)):        
        # 按照dna编码规则中的方案a(a = 1)对密钥K进行编码
        k_dna = ''.join([dna1_dict[k[i] + k[i+1]] for i in range(0, len(k), 2)])
        # 按照dna编码规则中的方案b(b = 7)对xe_lst进行编码
        xe_b = realNum2bin(xe_lst[i])
        xe_S, xe_E, xe_M = xe_b[0], xe_b[1: 12], xe_b[12:]
        xe_dna = ''.join([dna7_dict[str(xe_M[i]) + str(xe_M[i+1])] for i in range(0, len(xe_M), 2)])
        # 按照方案a对应的减法方案进行dna减法运算
        x_sub_dna = ''.join([dna_sub[xe_dna[i] + k_dna[i]] for i in range(len(xe_dna))])  
        # 使用方案a(a=1)对x_sub_dna解码，得到解密后的二进制x坐标
        x_b = str(xe_S) + ''.join([str(i) for i in xe_E]) + ''.join([dna1_dict_anti[x_sub_dna[i]] for i in range(len(x_sub_dna))])
        x_d = bin2realNum(list(map(int, list(x_b))))
        x_lst.append(x_d)
    return x_lst

# # 顶点坐标
# x = [238273.738921738973, -723873.37294637464, -238743.79832743827]
# xe = dna_encrypt(x)
# print(xe)
# xd = dna_decrypt(xe)
# print(xd)



    
