# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def dfs(root):
            if root is None:
                return [0,True]
            left = dfs(root.left)
            right = dfs(root.right)
            isBal = left[1] and right[1] and abs(left[0] - right[0])<=1
            depth = max(left[0], right[0]) + 1
            return [depth , isBal]

            #returns depth and isBalanced ? 
        
        val = dfs(root)
        return val[1]

        
        