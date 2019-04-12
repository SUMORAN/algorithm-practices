# -*- coding:utf-8 -*-
'''
《二叉树中和为某一值的路径》
题目描述
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''

'''
解题思路：
深度优先搜索
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        if expectNumber < root.val:
            return []
        
        res = []
        sum_now = 0
        list_now = []
        
        def DfsSum(root, expectNumber, sum_now, list_now):
            isLeaf = root.left==None and root.right==None

            list_now.append(root)
            sum_now = sum_now + root.val

            if sum_now == expectNumber and isLeaf:
                print(root.val)
                print(list_now)

                onePath = []
                for node in list_now:
                    onePath.append(node.val)
                res.append(onePath)
                print(res)

            elif sum_now < expectNumber:
                if root.left:
                    DfsSum(root.left, expectNumber, sum_now, list_now)
                if root.right:
                    DfsSum(root.right, expectNumber, sum_now, list_now)
            # 如果加上当前节点之后大于期望值或者等于期望值但钱钱节点不是叶子节点，就将这些这个点弹出去不保存，求和也不算它了，
            # 此路不通
            list_now.pop()
            sum_now = sum_now - root.val

                
        
        DfsSum(root, expectNumber, sum_now, list_now)
        
        res.sort(key = lambda x: len(x), reverse=True)
                    
        return res

def makeListNode(numbers):
    dummyRoot = TreeNode(0)
    ptr = dummyRoot
    
    for num in numbers:
        ptr.next = TreeNode(num)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def main():
    root = makeListNode([10,5,12,4,7])
    expectNumber = 22

    result = Solution().FindPath(root, expectNumber)
    print(result)
   

if __name__=='__main__':
    main()