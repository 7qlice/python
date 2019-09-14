"""
Author: Mr. Luo
Date: 2019-09-14
"""
a_dict = {"a":12,"b":13,"c":14,"d":15}
print("遍历键")
for ele in a_dict.keys():
    print(ele)
print("\n遍历值")
for ele1 in a_dict.values():
    print(ele1)
print("\n遍历键值对")
for key_ele, value_ele in a_dict.items():
    print(key_ele,value_ele)
