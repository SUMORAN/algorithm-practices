# -*- coding:utf-8 -*-
'''
《数组中出现次数超过一半的数字》
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。
'''

'''
解题思路：
解法一：
先排序，如果出现次数大于一半的数字存在，数字最中间那个肯定是，接下来就数一数最中间这个数字出现次数是不是真的大于一半，是的话返回这个数字，不是的话返回0
本方法会先对数组进行了顺序的调整（排序）
排序用快排就可以，不需要稳定排序

解法二：
这个方法不用调整数组
从头到尾遍历数组，对第一个数，设置count=1，下一个数如果跟这个相同，count+1，如果不同，count-1；
当count为0了，下一个数时count再设置为1，
因为超过一半的数存在的话，这样与剩下不足一半的数抵消之后最终结果肯定大于0
这个数字就是最后一次count被设置为1时的数字

以上两种算法时间复杂度都是O(n)
'''
# 解法一
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0

        nums = sorted(numbers)
        L = len(nums)
        mid = int(L/2)
        num = nums[mid]
        count = 0
        for item in nums:
            if item == num:
                count += 1
            if count > mid:
                return num
        return 0


# [1,2,3,2,4,2,5,2,3]
# 解法二
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0

        L = len(numbers)
        count = 1
        num = numbers[0]
        for i in range(1, L):
            if numbers[i] == num:
                count += 1
            elif count > 0:
                count -= 1
            else:
                count = 1
                num = numbers[i]
        
        mid = int(L/2)
        if count > 0:
            cnt = 0
            for item in numbers:
                if item == num:
                    cnt += 1
                if cnt > mid:
                    return num  
        return 0