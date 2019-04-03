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
 依然有问题，，，，我觉得我写的是对的啊 T-T
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        
        left = pRootOfTree
        right = pRootOfTree
        if pRootOfTree.left:
            left = self.Convert(pRootOfTree.left)
            
        if pRootOfTree.right:
            right = self.Convert(pRootOfTree.right)
            
        while left.right:
                left = left.right   #对根左边的找到最右节点
        
        p = left
        if p:
            p.right = pRootOfTree
            pRootOfTree.p = p
            
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right

        return p

def main():
    pRoot = TreeNode(10)
    pRoot.left = TreeNode(6)
    pRoot.right = TreeNode(14)
    pRoot.left.left =TreeNode(4)
    pRoot.left.right = TreeNode(8)
    pRoot.right.left = TreeNode(12)
    pRoot.right.right = TreeNode(16)

    res = Solution().Convert(pRoot)
    print('1111111111')
    while not res:
        print('1111111111')
        print(res.val)
        res = res.right
    

if __name__=='__main__':
    main()