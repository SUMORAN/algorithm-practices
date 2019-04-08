# -*- coding:utf-8 -*-
'''
《第一个只出现一次的字符》
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
'''
'''
解题思路：
遍历字符串两遍，
第一遍将字母和对应出现次数存在哈希表里
第二遍找出来第一个出现一次的字母
O(n)
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        if len(s) == 1:
            return s
        s = list(s)
        dic = dict.fromkeys(s, 0)
        for item in s:
            dic[item] =  dic[item]+1
        
        for index, item in enumerate(s):
            if dic[item] == 1:
                return index