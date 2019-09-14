"""
Author: Mr. Luo
Date: 2019-09-14
"""
import random
NUM = 15
result = []
for i in range(NUM):
    n = random.randint(65, 91)
    result.append(chr(n))
print(result)