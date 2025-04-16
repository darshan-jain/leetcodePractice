# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        ans = 0 
        def dfs(root,no):
            if root is None:
                return 
            nonlocal ans
            if root.left is None and root.right is None:
                no = (no*10) + root.val
                ans+=no
                return 
            no = (no*10) + root.val
            dfs(root.left,no)
            dfs(root.right,no)
        
        dfs(root,0)
        return ans
        