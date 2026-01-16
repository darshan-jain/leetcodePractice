# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        
        maxpathSum = float("-inf")
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(0,left)
            right = max(0,right)
            pathSum = root.val + left+right
            nonlocal maxpathSum
            maxpathSum = max(maxpathSum, pathSum)
            return root.val + max(left, right)
        
        dfs(root)
        return maxpathSum
        