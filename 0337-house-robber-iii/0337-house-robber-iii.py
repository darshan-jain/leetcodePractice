# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(root):
            if root is None:
                return [0,0]
            if root.left is None and root.right is None:
                return [0,root.val]
            left = dfs(root.left)
            right = dfs(root.right)
            # val1 = left[1] + right[1]
            val2 = root.val + left[0] + right[0]
            return [max(left) + max(right),val2]
        
        final = dfs(root)
        return max(final)
        

        