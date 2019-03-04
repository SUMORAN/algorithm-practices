# -*- coding:utf-8 -*-
'''
《跳台阶》
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
'''
解题思路：
假设有n级台阶，如果第一次跳1阶，就还剩n-1阶；如果第一次跳2阶，就还剩n-2阶。
因此对于n阶来说，跳法f(n)=f(n-1)+f(n-2)
也就是一个斐波那契数列
'''
class Solution:
    def jumpFloor(self, number):
        res = [0,1,2,3,5]
        if number<=0:
            return 0
        elif number==1:
            return 1
        elif  number==2:
            return 2
        else:
            while len(res)<=number:
                res.append(res[-1]+res[-2])
            return res[number+1]