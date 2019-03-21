# -*- coding:utf-8 -*-
'''
《从上往下打印二叉树》
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

'''
解题思路：
用栈保存下来每层节点，输出值，同时一个一个去找下一层节点，形成新的栈
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        res = []
        nodelist = []
        if root:
            nodelist.append(root)
        
        while nodelist:
            newnode = []
            for node in nodelist:
                res.append(node.val)
                if node.left:
                    newnode.append(node.left)
                if node.right:
                    newnode.append(node.right)
            nodelist = newnode
            
        return res
        
        