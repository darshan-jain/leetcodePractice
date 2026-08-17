# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 

        ans = 0         
        q = [(root,1)]
        while q:
            next_level = []
            for node, lvl in q:
                if node.left:
                    next_level.append((node.left, 2*lvl))
                if node.right:
                    next_level.append((node.right, 2*lvl + 1))
            ans = max(ans, q[-1][1] - q[0][1]+1)
            q = next_level
        return ans
        