# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = float('-inf')
    def helper(self,node):
        if node is None:
            return 0 
        left = self.helper(node.left)
        right = self.helper(node.right)
        left = max(0,left)
        right = max(0,right)
        pathSum = left+right + node.val
        self.ans = max(self.ans, pathSum)
        return max(left,right) + node.val
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.ans
        