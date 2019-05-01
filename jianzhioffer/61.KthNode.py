# -*- coding:utf-8 -*-
"""二叉搜索树的第k个结点
    题目描述
    给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

    解题思路：
    中序遍历
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        self.res = []
        self.midOrder(pRoot)
        if k < 1 or k > len(self.res):
            return None
        return self.res[k-1]

    def midOrder(self, pRoot):
        if not pRoot:
            return
        if pRoot.left:
            self.midOrder(pRoot.left)
        self.res.append(pRoot)
        if pRoot.right:
            self.midOrder(pRoot.right)


# 用例:
# {8,6,10,5,7,9,11},1
def main():
    p = TreeNode(8)
    p.left = TreeNode(6)
    p.right = TreeNode(10)
    p.left.left = TreeNode(5)
    p.left.right = TreeNode(7)
    p.right.left = TreeNode(9)
    p.right.right = TreeNode(11)
    re = Solution().KthNode(p, 1)
    print(re)


main()