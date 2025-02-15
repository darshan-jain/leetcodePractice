# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,value):
        if root is None:
            return 0 
        value = (value*10)+root.val
        if root.left is None and root.right is None:
            return value
        return self.helper(root.left,value) + self.helper(root.right,value)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root,0)
        