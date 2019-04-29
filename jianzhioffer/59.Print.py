# -*- coding:utf-8 -*-
"""按之字形顺序打印二叉树
    题目描述
    请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        else:
            FLAG = True # False表示偶数行,从右到左
            tmp = []
            tmp.append(pRoot)
            res = []
            while tmp:
                if FLAG:
                    tmp_res = []
                    for i in range(len(tmp)):
                        tmp_res.append(tmp[i].val)
                    FLAG = False
                else:
                    tmp_res = []
                    for i in range(1, len(tmp)+1):
                        tmp_res.append(tmp[-i].val)
                    FLAG = True
                    
                res.append(tmp_res)
                temp = self.toList(tmp)
                tmp = temp
        return res


    def toList(self, array):
        tmp = []
        if not array:
            return tmp
        for i in array:
            if i.left:
                tmp.append(i.left)
            if i.right:    
                tmp.append(i.right)
        return tmp
