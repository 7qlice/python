"""
Author: Mr. Luo
Date: 2019-09-14
"""
def action(fn):
    def run(*c):
        print("龙可以飞!")
        x = fn(*c)
        return x
    return run
@action
def eat(e, b):
    print("求出最大值\n",max(e, b))
    print("求和\n",e + b)
eat(9,7)
print("\n",eat)
"""
函数action装饰函数eat的过程如下：
1.将被装饰的函数eat作为参数传给@符号引用的函数action()
2.eat函数被替换成action装饰器的返回值
"""
