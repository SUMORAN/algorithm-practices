# -*- coding:utf-8 -*-

"""《调整数组顺序使奇数位于偶数前面》
    题目描述：
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
    使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
    并保证奇数和奇数，偶数和偶数之间的相对位置不变。

    解题思路：
    1、冒泡排序
    2、使用deque,双端队列（deque，全名double-ended queue）是一种具有队列和栈性质的抽象数据类型。 
    双端队列中的元素可以从两端弹出，插入和删除操作限定在队列的两邊进行。
    方法有pop(), popleft(), append(), appendleft()
from collections import deque
"""

'''
class Solution:
    def reOrderArray(self, array):
        odd = []
        even = []
        for num in array:
            if num & 1:
                odd.append(num)
            else:
                even.append(num)
        return odd + even
'''
'''
class Solution:
    def reOrderArray(self, array):
        for i in range(len(array)-1): # 冒泡排序次数
            for j in range(len(array)-i-1): #j表示列表下标
                if array[j+1]&1 and not array[j]&1:
                    array[j], array[j+1] = array[j+1], array[j]
        return array
'''
from collections import deque
class Solution:
    def reOrderArray(self, array):
        result = deque()
        length = len(array)
        for i in range(length):
            if array[length-i-1]&1: #奇数倒着数
                result.appendleft(array[length-i-1])
            if not array[i]&1: # 偶数正着数
                result.append(array[i])
        return result

