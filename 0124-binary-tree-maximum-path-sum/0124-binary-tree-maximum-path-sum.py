# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxval = float("-inf")
        if root is None:
            return 0 
        def helper(root):
            if root is None:
                return 0 
            left = helper(root.left)
            right = helper(root.right)
            val = max(left, 0) + max(right,0) + root.val
            nonlocal maxval
            maxval = max(maxval, val)
            return max(left,right,0) + root.val
        helper(root)
        return maxval
        