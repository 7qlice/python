"""
Author: Mr. Luo
Date: 2019-10-12
"""
import random
def bubble_sort(alist):
    """
    冒泡排序算法的运作如下：
    比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    针对所有的元素重复以上的步骤，除了最后一个。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
    最坏时间复杂度：O(n2)
    稳定性：稳定
    :param alist: 输入的列表
    :return:
    """
    for j in range(len(alist) - 1, 0, -1):
        #range(start, stop, step)计数开始，计数结束，步长
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
#列表推导式生成列表
luo = [i for i in range(50) if i%4==0]
#利用random.shuffle()方法将原列表的次序打乱
random.shuffle(luo)
print("*"*20,"打乱后的列表","*"*20)
print(luo)
bubble_sort(luo)
print("*"*20,"冒泡后的列表","*"*20)
print(luo)
"""
Author: Mr. Luo
Date: 2019-10-12
"""
import random
def selection_sort(alist):
    """
    选择排序（Selection sort）是一种简单直观的排序算法。
    它的工作原理如下：
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    然后，再从剩余未排序元素中继续寻找最小（大）元素，
    然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
    最优时间复杂度：O(n2)
    最坏时间复杂度：O(n2)
    稳定性：不稳定（考虑升序每次选择最大的情况）
    :param alist: 生成的列表
    :return:
    """
    n = len(alist)
    # 需要进行n-1次选择操作
    for i in range(n - 1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]
#生成列表
alist = [x*x for x in range(50,90) if x%5 == 0]
#打乱列表
random.shuffle(alist)
print("*"*10,"排序前","*"*10)
print(alist)
selection_sort(alist)
print("*"*10,"选择排序后","*"*10)
print(alist)
"""
Author: Mr. Luo
Date: 2019-10-12
"""
import random
def insert_sort(alist):
    """
    插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
    它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，
    找到相应位置并插入。插入排序在实现上，在从后向前扫描过程中，
    需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
    最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
    最坏时间复杂度：O(n2)
    稳定性：稳定
    :param alist:
    :return:
    """
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
alist = [x*x for x in range(50,90) if x%6 == 0]
#打乱列表
random.shuffle(alist)
print("*"*10, "排序前", "*"*10)
print(alist)
insert_sort(alist)
print("*"*10, "排序后", "*"*10)
print(alist)
列表是可变对象，列表元素交换，
t = [1,2,3,4]
print("交换前：",t)
t[0],t[1] = t[1],t[0]
print("交换后：",t)
"""
Author: Mr. Luo
Date: 2019-10-12
"""
import random
def quick_sort(alist, start, end):
    """快速排序步骤为：
    从数列中挑出一个元素，称为"基准"（pivot），
    重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
    递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
    最优时间复杂度：O(nlogn)
    最坏时间复杂度：O(n2)
    稳定性：不稳定
    """
    # 递归的退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end
    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)

alist = [x*x for x in range(50,77) if x%3 == 0]
#打乱列表
random.shuffle(alist)
print("*"*10, "排序前", "*"*10)
print(alist)
quick_sort(alist, 0, len(alist) - 1)
print("*"*10, "排序后", "*"*10)
print(alist)
"""
Author: Mr. Luo
Date: 2019-10-12
"""
import random
def shell_sort(alist):
    """
    希尔排序的基本思想是：
    将数组列在一个表中并对列分别进行插入排序，重复这过程，
    不过每次用更长的列（步长更长了，列数更少了）来进行。
    最后整个表就只有一列了。
    将数组转换至表是为了更好地理解这算法，
    算法本身还是使用数组进行排序。
    最优时间复杂度：根据步长序列的不同而不同
    最坏时间复杂度：O(n2)
    稳定想：不稳定
    :param alist:
    :return:
    """
    n = len(alist)
    # 初始步长
    gap = n / 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(int(gap), n):
            j = i
            # 插入排序
            while j >= int(gap) and alist[j - int(gap)] > alist[j]:
                alist[j - int(gap)], alist[j] = alist[j], alist[j - int(gap)]
                j -= int(gap)
        # 得到新的步长
        gap = gap / 2
alist = [x*x for x in range(50,77) if x%3 == 0]
#打乱列表
random.shuffle(alist)
print("*"*10, "排序前", "*"*10)
print(alist)
shell_sort(alist)
print("*"*10, "排序后", "*"*10)
print(alist)
