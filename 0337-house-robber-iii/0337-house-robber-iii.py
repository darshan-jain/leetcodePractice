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
                return [root.val,0]
            left = dfs(root.left)
            right = dfs(root.right)
            return [root.val + left[1]+right[1], max(left[0],left[1])+ max(right[0], right[1])]
        val= dfs(root)
        return max(val[0],val[1])
