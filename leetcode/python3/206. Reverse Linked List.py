# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 迭代
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pre, cur = None, head
        while cur:
            n = cur.next
            cur.next = pre
            pre = cur
            cur = n
        return pre

    # 递归
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next) # 一直找到最后一个
        # 两个两个处理
        tmp = head.next
        tmp.next = head
        head.next = None
        return new_head