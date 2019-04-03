# -*- coding:utf-8 -*-
'''
《字符串的排列》
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
'''
解题思路：
每次将字符串当作一个字符和剩余字符两部分，递归
'''
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        res = []

        if len(ss)==1:
            return ss
        
        ss = list(ss)

        for i in range(len(ss)):
            tmp = []
            
            tmp.append(ss[i])
            tmp.append(' ')
            if i > 0:
                ss[0], ss[i] = ss[i], ss[0]
            subTemp = self.Permutation(ss[1:])
            for item in subTemp:
                tmp[1] = ''.join(item)
                temp = ''.join(tmp)
                res.append(temp)
            
        res = list(set(res))
        res = sorted(res)
        return res

res = Solution().Permutation('aab')
print(res)