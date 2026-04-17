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
        def helper(root):
            if root is None:
                return [0,True]
            left = helper(root.left)
            right = helper(root.right)
            if left[1] and right[1] and abs(left[0]-right[0])<=1:
                return [max(left[0],right[0])+1, True]
            else:
                return [max(left[0],right[0])+1, False]
        return helper(root)[1]
            
            
        