# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = [root]
        
        while q:
            level = []
            next_level = []
            for elem in q:
                level.append(elem.val)
                if elem.left:
                    next_level.append(elem.left)
                if elem.right:
                    next_level.append(elem.right)
            res.append(level)
            q = next_level
        return res[::-1]
        