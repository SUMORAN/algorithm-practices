# -*- coding:utf-8 -*-
"""删除链表中重复的结点
    题目描述
    在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
    例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

    解题思路：

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 时间复杂度好像很大。。。或者是哪里写错了跳不出循环了，，，，
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return None
        if not pHead.next:
            return pHead

        pre = ListNode(0)
        pre.next = pHead
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                wait_del = pHead.next.val
                tmp_node = pHead.next.next  # 把紧接着的两个重复的都去掉
                while tmp_node: # 当不是链表尾时
                    if tmp_node.val == wait_del:
                        tmp_node = tmp_node.next
                    else:
                        break
            pHead = tmp_node
        
        return pre.next

# 这个是讨论区别人的代码，递归
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        if pHead.val == pHead.next.val:
            tmp = pHead.next
            while tmp and tmp.val == pHead.val:
                tmp = tmp.next
            return self.deleteDuplication(tmp)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead


def makeListNode(numbers):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    
    for num in numbers:
        ptr.next = ListNode(num)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def main():
    root = makeListNode([1,1,3,4,5,5,6,7])

    result = Solution().deleteDuplication(root)
    print(result)
   

if __name__=='__main__':
    main()