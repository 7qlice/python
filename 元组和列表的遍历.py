"""
Author: Mr. Luo
Date: 2019-09-14
"""
import random
print("生成列表")
l_list = [random.randint(20,78) for i in range(12)]
print(l_list)
print("遍历列表")
for ele in l_list:
    print(ele,end=' ')
print("\n列表转元组")
y_list = tuple(l_list)
print(y_list)
print("遍历元组")
for ele0 in y_list:
    print(ele0, end=' ')
