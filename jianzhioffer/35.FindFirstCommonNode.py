# -*- coding:utf-8 -*-
'''
《两个链表的第一个公共结点》
题目描述
输入两个链表，找出它们的第一个公共结点。
'''
'''
解题思路：
找到公共节点的话，两个链表后半部分是一样的
所以尾巴的长度是一样的
所以先把两个链表取一样长，也就是谁长，谁就先走几步，剩跟另一个一样长了再一起往后顺着比较。
时间复杂度，应该是计算两个长度的时间，加上正常走完一遍的时间 O(m+n)
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def Mylen(self, root):
        tmp = root
        length = 0
        while root:
            length += 1
            if tmp.next:
                tmp = tmp.next
            else:
                break

        return length

    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1:
            return pHead1
        if not pHead2:
            return pHead2
        len1 = self.Mylen(pHead1)
        len2 = self.Mylen(pHead2)
        
        step = 0
        if len1 > len2:
            while step < len1-len2:
                pHead1 = pHead1.next
                step += 1
        elif len1 < len2:
            while step < len2-len1:
                pHead2 = pHead2.next
                step += 1
        
        while pHead1:
            if pHead1 == pHead2:
                return pHead1
            elif pHead1.next:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
            else: break
        return


