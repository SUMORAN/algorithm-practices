# -*- coding:utf-8 -*-
'''
《树的子结构》
题目描述：
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''

'''
解题思路：
先在树A中找到与树B子节点相等的节点，然后再判断该节点下左右节点是否与B树一致
都一致时返回true，不一致时继续遍历A树，找下一个与B树根节点相等的节点
1、通过递归法比较节点是否相等，思路大致同leetcode题目965. Univalued Binary Tree.py
2、
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
这里代码不简洁，下面有化简的
不过这里虽然代码更凌乱一些，但执行时会比下方简化过后的代码稍微少几次left和right的运算，时间上会稍微快一点点点点点点点点点点点点点点点点点点
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # 首先排除树为空的情况
        def isSubtress(pRoot1, pRoot2):
            if not pRoot2 or not pRoot1:
                return False
            if pRoot1.val != pRoot2.val:
                return isSubtress(pRoot1.left, pRoot2) or isSubtress(pRoot1.right, pRoot2)
            else: # 当前节点相等
                if pRoot2.left and pRoot2.right: # 如果两边都不为空，左右子树都要判断，且都为true时结构为true
                    if isSubtress(pRoot1.left, pRoot2.left) and isSubtress(pRoot1.right, pRoot2.right): # 如果符合，说明最终结果符合
                        return True
                    else: # 如果在当前节点相等的情况下不符合，就继续寻找下一个相等的节点
                        return isSubtress(pRoot1.left, pRoot2) or isSubtress(pRoot1.right, pRoot2)
                elif pRoot2.left and not pRoot2.right: # 如果左边不为空右边为空，说明右侧已经符合了，判断左侧是否符合
                    if isSubtress(pRoot1.left, pRoot2.left):
                        return True
                    else:
                        return isSubtress(pRoot1.left, pRoot2) and isSubtress(pRoot1.right, pRoot2)
                elif not pRoot2.left and pRoot2.right: # 如果左边为空右边不为空，说明左侧已经符合了，判断右侧是否符合
                    if isSubtress(pRoot1.right, pRoot2.right):
                        return True
                    else:
                        return isSubtress(pRoot1.left, pRoot2) and isSubtress(pRoot1.right, pRoot2)
                elif not pRoot2.left and not pRoot2.right: # 如果两边都为空，在当前节点符合的情况下，说明最终结果符合
                    return True
        return isSubtress(pRoot1, pRoot2)
'''

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # 定义函数
        def isSubtress(pRoot1, pRoot2):
            if not pRoot2:
                return True
            elif not pRoot1:
                return False
            if pRoot1.val != pRoot2.val: # 当前节点不等
                return isSubtress(pRoot1.left, pRoot2) or isSubtress(pRoot1.right, pRoot2)
            else: # 当前节点相等
                if isSubtress(pRoot1.left, pRoot2.left) and isSubtress(pRoot1.right, pRoot2.right): # 如果符合，说明最终结果符合
                    return True
                else: # 如果在当前节点相等的情况下不符合，就继续寻找下一个相等的节点，如果找到最后都没找到，就会按照上方的if判断返回false
                    return isSubtress(pRoot1.left, pRoot2) or isSubtress(pRoot1.right, pRoot2)
        
        # 首先排除树为空的情况
        if not pRoot2 or not pRoot1:
            return False
        return isSubtress(pRoot1, pRoot2)