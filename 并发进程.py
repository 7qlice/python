"""
Author: Mr. Luo
Date: 2019-09-14
"""
from time import sleep
import numpy as np
class people:
    """
    并发进程
    """
    i = 1
    j = 1
    def dance(self):
        for i in range(5):
            print("the computer is dancing!%i" %i)
            self.sing()
            sleep(1)#停顿1s，在开始下边的
        return 0

    def sing(self):
        for i in range(5):
            print("the comupter is singing!!!!%i" %i)
            sleep(1)
        return 0
luo = people()
luo.sing()
luo.dance()

