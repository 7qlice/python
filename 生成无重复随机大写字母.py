"""
Author: Mr. Luo
Date: 2019-09-14
"""
import random
NUM = 20
result = []
t_list = []
for i in range(NUM):
    n = random.randint(65, 91)
    result.append(chr(n))
print(result)
for ele in result:
    if ele not in t_list:
        t_list.append(ele)
print("去掉重复生成的字母，新列表如下")
print(t_list)
