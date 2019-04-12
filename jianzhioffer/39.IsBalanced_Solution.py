# -*- coding:utf-8 -*-
"""平衡二叉树
    题目描述
    输入一棵二叉树，判断该二叉树是否是平衡二叉树。
    
    解题思路：
    平衡二叉树，左节点小于根节点小于右节点
    左右子树深度差不大于1
    -1 <= 左子树深度 - 右子树深度 <= 1


"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot: # 树为空时不是平衡二叉树
            return True
        if not pRoot.left and not pRoot.right: # 树只有根节点时是平衡二叉树
            return 1
        return self.IsBalanced(pRoot)

    def IsBalanced(self, pRoot):
            if not pRoot: # 树为空时深度为0
                return -1    # 这里不能用0表示，要不然下面判断时会被当作False，所以就多了一步迂回，大概会有更好的解决方式的
            if not pRoot.left and not pRoot.right: # 树只有根节点深度为1
                return 1

            left = self.IsBalanced(pRoot.left)
            right = self.IsBalanced(pRoot.right)
            if left==False or right==False:
                return False
            
            if left == -1:
                left += 1
            if right == -1:
                right += 1
            # 如果左右子树深度相等或者相差1，返回深度较大的那个值+1，+1是为了将当前root算在内
            if left - right == 1 or left - right == 0: 
                return left + 1
            elif left - right == -1:
                return right + 1
            else:
                return False