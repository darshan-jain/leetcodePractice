# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = [root]
        level = []
        next_level = []
        res = []
        while q:
            for elem in q:
                if elem.left:
                    next_level.append(elem.left)
                if elem.right:
                    next_level.append(elem.right)
            res.append(q[-1].val)
            q = next_level
            next_level = []
        return res
            

        