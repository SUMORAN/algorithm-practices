# -*- coding:utf-8 -*-

#########这题要重做，重新思考


'''
《复杂链表的复制》
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

'''

'''
解题思路：
复制之后拆分出来
'''
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
'''
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        res = RandomListNode(pHead.label)
        res.next = self.Clone(pHead.next)
        res.random = pHead.random # 这里存疑，为什么指向pHead链表中的内容会没有问题
        return res
'''
