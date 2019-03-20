# -*- coding:utf-8 -*-
'''
《包含min函数的栈》
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''

'''
解题思路：
用另一个栈保存最小元素
'''



class Solution:
    def __init__(self):
        self.items = []
        self.mins = []
    def push(self, node):
        self.items.append(node)
        if not self.mins or node <= self.mins[-1]:
            self.mins.append(node)
    def pop(self):
        if len(self.items):
            if self.items[-1] == self.mins[-1]: # 如果最小元素出去了，那么mins中最小元素也要去掉一个
                self.mins.pop()
            return self.items.pop()
    def top(self):
        if len(self.items):
            return self.items[-1]
        else:
            return
    def min(self):
        return self.mins[-1]