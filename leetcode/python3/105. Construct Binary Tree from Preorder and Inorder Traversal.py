# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
105. Construct Binary Tree from Preorder and Inorder Traversal
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def buildNode(preorder,inorder):
            if len(preorder) == 0:
                return None
            
            # 前序遍历的第一个元素是根
            rootVal = preorder[0]
            root = TreeNode(rootVal)
            
            # 中序遍历中根左边的为左子树部分，根右边的为右子树部分
            '''
            preorder = [3,9,20,15,7]
            inorder = [9,3,15,20,7]
            '''
            rootIndex = inorder.index(rootVal)

            preorderLeft = preorder[1:rootIndex+1] # 根右侧数字中表示左子树部分的几个
            inorderLeft = inorder[0:rootIndex] # 根左侧数字表示左子树部分

            preorderRight = preorder[rootIndex+1:] # 根右侧数字中表示右子树部分的几个
            inorderRight = inorder[rootIndex+1:]# 根右侧数字表示右子树部分

            # 左右子树部分具体求法同上
            root.left = buildNode(preorderLeft,inorderLeft)
            root.right = buildNode(preorderRight,inorderRight)
            
            return root
        
        return buildNode(preorder,inorder)
            