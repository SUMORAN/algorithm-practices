# -*- coding:utf-8 -*-
"""序列化二叉树
    题目描述
    请实现两个函数，分别用来序列化和反序列化二叉树

    所谓序列化指的是遍历二叉树为字符串；所谓反序列化指的是依据字符串重新构造成二叉树。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.index = 0

    def Serialize(self, root):
        
        if not root:
            return "#"
        # 递归
        res = []
        res.append(str(root.val))
        if root.left:
            res.append(self.Serialize(root.left))
        if root.right:
            res.append(self.Serialize(root.right))
        return ','.join(res)

    def Deserialize(self, s):
        s = s.split(',')
        if len(s)==1 and s[0]=="#":
            return None
        tree = self.deserialize(s)
        return tree
    
    def deserialize(self, s): # 一个一个的构建节点
        # if self.index >= len(s):
        #     return None
        # if s[self.index] == "#":
        #     self.index += 1
        #     return None
        # node = TreeNode(int(s[self.index]))
        # self.index += 1
        # node.left = self.deserialize(s)
        # node.right = self.deserialize(s)
        # return node   
        if self.index >= len(s):
            return None
        t = s[self.index]
        if t.isdigit():
            root = TreeNode(int(t))
            self.index +=1
            left = self.deserialize(s)
            right = self.deserialize(s)
            root.left = left
            root.right = right
            return root
        elif t =="#":
            self.index+=1
            return None
        