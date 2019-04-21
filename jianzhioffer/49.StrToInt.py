# -*- coding:utf-8 -*-
"""把字符串转换成整数
    题目描述
    将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
    输入描述:
    输入一个字符串,包括数字字母符号,可以为空
    输出描述:
    如果是合法的数值表达则返回该数字，否则返回0
"""
class Solution:
    def StrToInt(self, s):
        numlist = ['0','1','2','3','4','5','6','7','8','9']
        num = 0
        label = 1 # 标记正负数
        if not s:
            return 0
        if s[0] == '+':
            label = 1
        elif s[0] == '-':
            label = 0
        elif s[0] in numlist:
            num = numlist.index(s[0])
        
        for i in range(1, len(s)):
            if s[i] in numlist:
                num = num * 10 + numlist.index(s[i])
            else:
                return 0
        
        if label == 1:
            return num
        else:
            return -num

def main():
    s = '123'
    res = Solution().StrToInt(s)
    print(res)

if __name__=='__main__':
    main()