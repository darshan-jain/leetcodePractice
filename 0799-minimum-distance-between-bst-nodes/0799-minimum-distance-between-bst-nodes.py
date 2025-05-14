# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        if root is None:
            return 0
        vals = inorder(root)
        res = float("inf")
        for a,b in pairwise(vals):
            res = min(res,b-a)
        return res
        