# -*- coding:utf-8 -*-
"""数组中重复的数字
    题目描述
    在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
    数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
    例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

    解题思路：
    把所有数字跟与自己下标相等的位对应起来，也就是数字0对应S[0],数字1对应S[1]这样
    从前往后遍历，符合上述要求就下一个，不符合上述要求就将当前位的数字和当前位数字应该对应的位的数字交换，这样至少这个数字的位置是对的了
    直到遇到某个数字想要跟它对应位置的数字交换时，发现那个数字就是在自己应该在的位置上没有错，那就说明这个数字是重复的。
    例如，S[5]=3, 我们本想把S[5]和S[3]交换，结果发现s[3]这时就等于3，那就说明3是重复出现的
"""
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False
        for i in range(len(numbers)):
            if numbers[i] == i:
                continue
            else: # 当当前数字不在应该在的位置时，考虑它应该在的位置的数字是不是对的，不对的话交换，对的话返回
                if numbers[numbers[i]] == numbers[i]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    tmp = numbers[i]
                    numbers[i] = numbers[tmp]
                    numbers[tmp] = tmp
        return False