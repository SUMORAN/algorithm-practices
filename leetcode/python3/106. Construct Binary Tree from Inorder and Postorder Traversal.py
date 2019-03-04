# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def buildNode(inorder, postorder):
            if len(postorder) == 0:
                return None

            # 后序遍历的最后一个元素是根
            rootVal = postorder[-1]
            root = TreeNode(rootVal)

            # 中序遍历中根左边的为左子树部分，根右边的为右子树部分
            '''
            preorder = [3,9,20,15,7]
            inorder = [9,3,15,20,7]
            postorder = [9,15,7,20,3]
            '''
            rootIndex = inorder.index(rootVal)

            postorderLeft = postorder[0:rootIndex]
            inorderLeft = inorder[0:rootIndex]

            postorderRight = postorder[rootIndex:-1]
            inorderRight = inorder[rootIndex + 1:]

            # 左右子树部分具体求法同上
            root.left = buildNode(inorderLeft, postorderLeft)
            root.right = buildNode(inorderRight, postorderRight)

            return root

        return buildNode(inorder, postorder)