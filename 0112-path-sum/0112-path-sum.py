# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,target):
            if root is None:
                return 
            if root.left is None and root.right is None and target-root.val==0:
                return True
            return dfs(root.left, target-root.val) or dfs(root.right, target-root.val)
            
            
        if root is None:
            return False
        if dfs(root,targetSum):
            return True
        return False
        