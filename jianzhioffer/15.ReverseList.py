# -*- coding:utf-8 -*-
"""
《反转链表》
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""

"""
解题思路：
注意深拷贝与浅拷贝
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return
        if pHead.next is None:
            return pHead
        # 链表长度大于1
        last = None
        while pHead:
            tmp = pHead
            print('tmp的id是：',id(tmp))
            print('pHead的id是：',id(pHead))
            pHead = pHead.next
            print('tmp的id是：',id(tmp))
            print('pHead的id是：',id(pHead))
            tmp.next = last
            print('tmp的id是：',id(tmp))
            print('pHead的id是：',id(pHead))
            last = tmp
            # pHead = pHead.next  # 这句话在下不在上时，tmp.next = last一句会影响到pHead使其next也为last
            print('tmp的id是：',id(tmp))
            print('pHead的id是：',id(pHead))
        return last


# 构建listNode
def makeListNode(numbers):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    
    for num in numbers:
        ptr.next = ListNode(num)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def main():
    pHead = makeListNode([1,2,3,4,5])
    Solution().ReverseList(pHead)

if __name__=='__main__':
    main()
