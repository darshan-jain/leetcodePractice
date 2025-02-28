# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,targetSum):
            
            if root is None:
                return False
            if root.left is None and root.right is None and root.val==targetSum:
                return True
            return dfs(root.left,targetSum-root.val) or dfs(root.right, targetSum - root.val)
        
        return dfs(root,targetSum)
        