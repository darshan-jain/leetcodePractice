# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder)==0:
            return None
        idx = -1 
        for i in range(len(inorder)):
            if preorder[0]==inorder[i]:
                idx=i
                break
        node = TreeNode(preorder[0])
        node.left = self.buildTree(preorder[1:idx+1], inorder[:idx+1])
        node.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return node
        