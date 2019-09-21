"""
Author: Mr. Luo
Date: 2019-09-21
"""
import numpy as np
a = np.array([[12,3,8],[4,5,6],[7,8,9],[10,2,3]])
print("矩阵的转置\n",a.T)
x = a.reshape(-1,1)
print("转换成一维矩阵\n",x)
y = a.shape
print("矩阵的大小\n",y)