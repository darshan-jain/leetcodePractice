# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            next_level = []
            for item in q:
                if item.left:
                    next_level.append(item.left)
                if item.right:
                    next_level.append(item.right)
            res.append(q[-1].val)
            q = next_level
        return res
        