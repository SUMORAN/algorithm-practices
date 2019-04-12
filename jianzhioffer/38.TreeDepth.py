# -*- coding:utf-8 -*-
"""二叉树的深度
    题目描述
    输入一棵二叉树，求该树的深度。
    从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

    解题思路：
        相当于返回的是左右子树中深度较大的子树的深度+1
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot: # 树为空时深度为0
            return 0
        if not pRoot.left and not pRoot.right: # 只有根节点的树深度为1
            return 1
        # 如果树有左子树和右子树，就分别求，递归
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1