"""
Author: Mr. Luo
Date: 2019-09-21
"""
import numpy as np
x = int(input("My lord，请输入矩阵维度：\n"))
y = int(input("My lord，请输入矩阵维度：\n"))
a = []
for i in range(x):
    a.append([])
    for j in range(y):
        a[i].append(int(input("please input your number:\n")))
print("My Lord，您输入的矩阵是：\n", a)
b = np.array(a)
print("My lord，mission is accomplished!转置后的矩阵显示如下：\n", b.T)