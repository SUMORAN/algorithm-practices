# -*- coding:utf-8 -*-
"""对称的二叉树
    题目描述
    请实现一个函数，用来判断一颗二叉树是不是对称的。
    注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

    解题思路：
    递归:
    在当前节点的左子节点和右子节点相同的情况下，继续判断左子节点的右子节点是不是等于右子节点的左子节点以及左子节点的左子节点是不是等于右子节点的右子节点

    不递归：
    一层一层读出来，保存在list中，看list反转之后是不是跟原来相等，以及数量是不是正常的
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return  True
        return self.isSame(pRoot.left, pRoot.right)
        
    def isSame(self, left, right):
        if not left and not right:
            return True
        elif left and right:
            return left.val==right.val and self.isSame(left.left, right.right) and self.isSame(left.right, right.left)
        else:
            return False

