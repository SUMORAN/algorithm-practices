# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
# 方法一
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        # 深度优先遍历，把树的值遍历保存在list中
        # 对list取set判断set的长度是否为1

        vals = []
        
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        return len(set(vals))==1
'''

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        # 判断新的节点值是否跟上一个节点值相等

        def isUnival(root, lastVal):
            if not root: # 判断是否遍历完
                return True
            if root.val != lastVal: # 如果出现不等的就在递归的过程中跳出
                return False
            return isUnival(root.left, root.val) and isUnival(root.right, root.val)

        return isUnival(root, root.val if root else None)
        
