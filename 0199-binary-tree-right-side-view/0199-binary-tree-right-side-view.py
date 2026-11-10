# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        q = [root]
        ans = []
        while q:
            res = []
            next_level = []
            for item in q:
                res.append(item.val)
                if item.left:
                    next_level.append(item.left)
                if item.right:
                    next_level.append(item.right)
            ans.append(res[-1])
            q = next_level
        return ans
        