# -*- coding:utf-8 -*-
"""求1+2+3+...+n
    题目描述
    求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

    解题思路：
    && 逻辑与，逻辑与有短路特点，当前面为假时，后面直接不进行计算了
    递归，通过逻辑与代替掉if判断
    C中逻辑与运算符是&&
    python中and运算符， a and b，a为False时，直接返回a，后面的就不算了，a为True时，计算b，与上述逻辑与相同
"""
class Solution:
    def Sum_Solution(self, n):
        ans = n
        return (ans and ans+self.Sum_Solution(n-1))