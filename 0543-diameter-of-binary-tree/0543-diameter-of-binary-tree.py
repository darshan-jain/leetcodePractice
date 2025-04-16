# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        max_dia = 0 
        def dfs(root):
            if root is None:
                return 0 
            left = dfs(root.left)
            right = dfs(root.right)
            dia = left+right
            nonlocal max_dia
            max_dia = max(dia, max_dia)
            return max(left,right)+1
        dfs(root)
        return max_dia

        