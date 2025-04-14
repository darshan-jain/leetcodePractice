# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root,minn,maxx):
            if root is None:
                return True
            if root.val<=minn or root.val>=maxx:
                return False
            return isValid(root.left, minn, root.val) and isValid(root.right, root.val, maxx)
        return isValid(root,float("-inf"), float("inf"))
        