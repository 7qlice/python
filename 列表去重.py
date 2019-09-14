"""
Author: Mr. Luo
Date: 2019-09-14
"""
import random
a_list = [random.randint(2, 9) for i in range(25)]
print("生成的列表如下\n",a_list)
b_list = []#生成空列表备用
for ele in a_list:
    if ele not in b_list:
        b_list.append(ele)
print("去重后\n",b_list)
