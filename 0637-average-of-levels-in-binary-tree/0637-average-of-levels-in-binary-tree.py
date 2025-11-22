# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        res = []
        while q:
            next_level = []
            level = []
            for item in q:
                level.append(item.val)
                if item.left:
                    next_level.append(item.left)
                if item.right:
                    next_level.append(item.right)
            res.append(sum(level)/len(level))
            q = next_level
        return res
        