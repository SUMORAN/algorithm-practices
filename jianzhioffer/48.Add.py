# -*- coding:utf-8 -*-
"""不用加减乘除做加法
    题目描述
    写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

    解题思路：
    两个数异或，相当于两个数按位相加不考虑进位
    两个数相与并左移一位，相当于求进位
    把进位和不考虑进位的相加就是和
    python需要检查溢出，
    对于负数，需要考虑符号位
"""
class Solution:
    def Add(self, num1, num2):
        a = (num1 ^ num2) & 0xFFFFFFFF
        b = ((num1 & num2)<<1) & 0xFFFFFFFF
        if b:
            return self.Add(a, b)
        else:
            return a if a <= 0x7FFFFFFF else ~(a^0xFFFFFFFF)