import numpy as np
from decimal import Decimal

def dec2bin(n):
    b = []
    if n >= 1:
        while True: 
            s = n // 2  
            y = n % 2
            b = b + [y]
            if s == 0:
                break
            n = s
        b.reverse()
        return b       
    elif n < 1:
        n -= int(n)        
        while n:
            n *= 2
            b.append(1 if n>=1. else 0)
            n -= int(n) 
        return b

def bin2dec(b):
  d = 0
  for i, x in enumerate(b):
    d += 2**(-i-1)*x
  return d

'''双精度浮点数转二进制'''
def realNum2bin(x):
    # 将实数拆分成整数和小数两部分
    regInt, regFloat = int(abs(x)), float(abs(x) - int(abs(x)))
    # 将整数和小数部分分别转为二进制
    regInt_bin, regFloat_bin = dec2bin(regInt)[1:], dec2bin(regFloat)
    # 根据IEEE754标准，将双精度浮点数转换成二进制
    S = int(np.floor(1/2 - np.sign(x)/2)) # 符号位
    e = int(np.floor(np.log2(abs(x))) + 1023) 
    E = dec2bin(e) # 指数位
    M = regInt_bin + regFloat_bin + [0] * (52 - len(regInt_bin) - len(regFloat_bin)) # 小数位
    x_b = (E + M)
    x_b.insert(0, S)
    return x_b

'''二进制浮点数转十进制浮点数'''
def bin2realNum(x):
    S = x[0]
    E = int(''.join([str(i) for i in x[1:12]]), 2)
    e = E - 1023
    M = x[12:]
    regInt_bin, regFloat_bin = [1] + M[0:e], M[e:]
    regInt = int(''.join([str(i) for i in regInt_bin]), 2)
    # regFloat = float('0.' + ''.join([str(i) for i in regFloat_bin]))
    regFloat = bin2dec(regFloat_bin)
    x_d = regInt + regFloat
    if S == 0:
        x_d = x_d
    elif S == 1:
        x_d = -x_d
    return x_d

# x = 238273.738921738973
# # x= 58.625
# x_to_bin = realNum2bin(x)
# b = [ str(i) for i in x_to_bin]
# print (x, '的二进制是', ''.join(b))
# d = bin2realNum(x_to_bin)
# print(''.join(b), '的十进制是', d)
