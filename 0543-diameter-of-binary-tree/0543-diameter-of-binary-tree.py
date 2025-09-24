# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0 
        if root is None:
            return max_dia 
        
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            dia = left+right 
            nonlocal max_dia 
            max_dia = max(max_dia, dia)
            return max(left,right)+1

        dfs(root)
        return max_dia
        