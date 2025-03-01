# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float("inf")
        self.prev_val = None
        def dfs(root):
            if root is None:
                return 
            dfs(root.left)
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, abs(self.prev_val - root.val))
            self.prev_val = root.val
            dfs(root.right)
        dfs(root)
        return self.min_diff
        