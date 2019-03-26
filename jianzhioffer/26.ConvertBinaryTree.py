# -*- coding:utf-8 -*-
'''
《二叉搜索树与双向链表》
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

'''
解题思路：
 明天再调，现在的有点问题
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
    
        
        if pRootOfTree.left:
            left = self.Convert(pRootOfTree.left)
            while left.right:
                left = left.right   #对根左边的找到最右节点
            pRootOfTree.left = left
        if pRootOfTree.right:
            right = self.Convert(pRootOfTree.right)
            while right.left:
                right = right.left  #对根右边的找到最左节点
            pRootOfTree.right = right
        
        res = pRootOfTree
        while res.left:
            res = res.left
        
        return res