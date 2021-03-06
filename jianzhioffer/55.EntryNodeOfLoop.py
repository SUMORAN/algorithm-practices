# -*- coding:utf-8 -*-
"""链表中环的入口结点
    题目描述
    给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

    解题思路：
    顺着走一遍，将走过的节点保存在list里
    每访问下一个节点时都看看这个点是不是已经在list里了
    如果在，就说明到环的位置了
    这个在list里的点，就是环的起点

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return None
        lis = []
        p1 = pHead
        while pHead not in lis: # 顺着访问，把访问过的保存在list中
            lis.append(pHead)
            if pHead.next:
                pHead = pHead.next
            if not pHead.next:
                return None
        num = lis.index(pHead)
        for i in range(num):
            p1 = p1.next

        return p1


# 构建listNode
def makeListNode(numbers):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    
    for num in numbers:
        ptr.next = ListNode(num)
        ptr = ptr.next


    p_begin = dummyRoot.next.next.next
    ptr.next = p_begin

    ptr = dummyRoot.next
    return ptr

def main():
    pHead = makeListNode([1,2,3,4,5,6,7,8,9])
    res = Solution().EntryNodeOfLoop(pHead)
    if res:
        print(res.val)
    else:
        print("None")

if __name__=='__main__':
    main()