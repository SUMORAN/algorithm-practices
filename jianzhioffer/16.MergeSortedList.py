# -*- coding:utf-8 -*-
"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
"""
解题思路：
1、递归方法，每次取出小的节点之后，剩下的部分和另一个链表一起再进行计算，结算作为当前节点的next
2、非递归方法， 用while代替递归方法中的递归过程
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    '''
    # 这个方法存在问题
    def Merge(self, pHead1, pHead2):
        # write code here
        dummyRoot = ListNode(0)
        res = dummyRoot
        print("res的id：",id(res))
        result = res
        print("result的id：",id(result))
        def mergeList(result, pHead1, pHead2):
            if pHead1 is None:
                result.next = pHead2
                return result
            if pHead2 is None:
                result.next = pHead1
                return result
            if pHead1.val < pHead2.val or pHead1.val == pHead2.val:
                result.next = pHead1
                result = result.next
                mergeList(result, pHead1.next, pHead2)
            if pHead1.val > pHead2.val:
                result.next = pHead2
                result = result.next
                mergeList(result, pHead1, pHead2.next)
        
        result = mergeList(result, pHead1, pHead2)
        print("res的id：",id(res))
        print("result的id：",id(result))
        return res.next
    '''
    # 递归方法
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1

        elif pHead1.val < pHead2.val or pHead1.val == pHead2.val:
           pHead1.next = self.Merge(pHead1.next, pHead2)
           return pHead1
        elif pHead1.val > pHead2.val:
           pHead2.next = self.Merge(pHead1, pHead2.next)
           return pHead2

    # 非递归方法
    def Merge(self, pHead1, pHead2):
        # write code here
        dummyRoot = ListNode(0)
        res = dummyRoot
        result = res
        # 下面关于result的修改，都会影响的res的next，使res作为最终结果串的开头
        # 上面的递归被这里的while循环代替
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val or pHead1.val == pHead2.val:
                result.next = pHead1
                pHead1 = pHead1.next # 这种情况下修改pHead1不会影响result.next
                result = result.next
            else:
                result.next = pHead2
                pHead2 = pHead2.next
                result = result.next
        
        if pHead1 is None:
            result.next = pHead2 # 这种情况下修改resul的next，res的next也会跟着改
        elif pHead2 is None:
            result.next = pHead1

        return res.next
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
    pHead1 = makeListNode([4,7,13])
    pHead2 = makeListNode([5,6,12])
    result = Solution().Merge(pHead1, pHead2)
    print('结果------------')
    while result is not None:
        print(result.val)
        result = result.next

if __name__=='__main__':
    main()