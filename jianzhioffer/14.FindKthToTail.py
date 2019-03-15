# -*- coding:utf-8 -*-
"""
题目描述：
输入一个链表，输出该链表中倒数第k个结点。
"""

"""
解题思路：
设置两个指针p1和p2，p1比p2先走k步，然后两个一起向后移动，当p1指向最后一个数时，p2指向的就是倒数第一个数
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 注意，本题要求返回的是节点，不是节点值
'''
class Solution:
    def FindKthToTail(self, head, k):
        numbers = []
        while head is not None:
            numbers.append(head)
            head = head.next
        if k <= len(numbers) and k > 0:
            return numbers[-k]
        else:
            return 
'''

class Solution:
    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return
        
        p1 = head
        p2 = head
        num = 0
        while num < k-1:
            if p1.next is not None:
                p1 = p1.next
                num += 1
            else: # k超过链表范围
                return
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next
  
        return p2
        