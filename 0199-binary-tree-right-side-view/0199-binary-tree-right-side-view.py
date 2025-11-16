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
        res = []
        q = [root]
        while q:
            next_level = []
            res.append(q[-1].val)
            for elem in q:
                if elem.left:
                    next_level.append(elem.left)
                if elem.right:
                    next_level.append(elem.right)
            q= next_level
        return res
        
        