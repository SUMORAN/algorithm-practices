# -*- coding:utf-8 -*-
"""二叉树的下一个结点
    题目描述
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
    注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
    
    解题思路：
    以下依次判断
    1、树为空，返回空
    2、当前节点既没有父节点也没有右节点（就是既是根节点又没有右子节点），返回空
    3、当当前节点有右子节点时，返回右子节点的左子节点的左子节点的左子节点，一直到最后一个
    4、当当前节点没有右子树时，找第一个当前节点是父节点的左子树的节点的父节点

"""
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        elif not pNode.right and not pNode.next:
            return None
        elif pNode.right:   # 有右子树，找右子树的最左节点
            tmp = pNode.right
            while tmp.left:
                tmp = tmp.left
            return tmp
        while pNode.next: # 没右子树，找第一个当前节点是父节点左孩子的节点的父节点
            if pNode.next.left==pNode:
                return pNode.next
            else:
                pNode = pNode.next
        return None
