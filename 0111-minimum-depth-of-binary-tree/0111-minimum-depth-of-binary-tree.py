# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        def dfs(root):
            if root is None:
                return 0 
            if not root.left:
                return dfs(root.right)+1
            if not root.right:
                return dfs(root.left)+1
            depth = min(dfs(root.left), dfs(root.right))+1
            return depth
        return dfs(root)
        