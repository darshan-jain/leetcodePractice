# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float("-inf")
    def helper(self,root):
        if root is None:
            return 0 
        left = self.helper(root.left)
        right = self.helper(root.right)
        left = max(0,left)
        right = max(0,right)
        pathSum = left+right + root.val
        self.max_sum = max(self.max_sum , pathSum)
        return max(left,right) + root.val
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.max_sum
        