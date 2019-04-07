# -*- coding:utf-8 -*-
'''
《丑数》
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

'''
解题思路：
能被2除就除以2，能被3除就除以3，能被5除就除以5，除外这3个之后等1的话，就说明这个数是丑数
'''
class Solution:
    # def isUglyNum(self, number):
    #     while number&1==0:
    #         number /= 2
    #     while number % 3 == 0:
    #         number /= 3
    #     while number % 5 == 0:
    #         number /= 5
    #     if number == 1:
    #         return True
    #     else:
    #         return False

    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        if index == 1:
            return 1
        UglyNumbers = [1]
        p2 = 0
        p3 = 0
        p5 = 0

        while(len(UglyNumbers)<index):
            Min = min(UglyNumbers[p2]*2, UglyNumbers[p3]*3, UglyNumbers[p5]*5)
            UglyNumbers.append(Min)

            while(UglyNumbers[p2]*2 <= UglyNumbers[-1]):
                p2 += 1
            while(UglyNumbers[p3]*3 <= UglyNumbers[-1]):
                p3 += 1
            while(UglyNumbers[p5]*5 <= UglyNumbers[-1]):
                p5 += 1

        return UglyNumbers[-1]