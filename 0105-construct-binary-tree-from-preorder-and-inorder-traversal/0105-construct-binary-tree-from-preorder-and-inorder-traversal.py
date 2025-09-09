# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        root = preorder[0]
        index = -1
        for i in range(len(inorder)):
            if inorder[i]==root:
                index = i
                break
        node = TreeNode(root)
        node.left = self.buildTree(preorder[1:index+1], inorder[:index+1])
        node.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return node
        