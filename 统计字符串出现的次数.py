"""
Date: 2019-09-10
Author: Mr. Luo
"""
# age = int(input("please input your age"))
# print("your age > 30") if age > 30 else print("your age = 30")if age  == 30 else print("your age <30")
#支持嵌套，三目运算
a = ['ic',1,'abc','def','ic','7','Mr. Luo','ic']
b = input("please input your string\n")
t =0
#判断输入的字符串在列表中是否存在
if b in a:
    print("字符串%s在给定的列表中\n"%b)
else:
    print("给定的列表中元素如下：\n")
    for ele in a:
        print(ele, end = '，')
#统计输入字符串在列表中出现的次数
for i in range(len(a)):
    if b == a[i-1]:
        t += 1
print("\n输入字符串在给定字符串中出现的次数为：\n",t)
