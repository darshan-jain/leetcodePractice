# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder)==0:
            return None
        root = postorder[-1]
        index = -1
        for i in range(len(inorder)):
            if inorder[i]==root:
                index=i
                break
        node = TreeNode(root)
        node.left = self.buildTree(inorder[0:index] , postorder[0:index])
        node.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return node
        