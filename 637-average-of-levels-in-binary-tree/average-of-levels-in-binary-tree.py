# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        level = []
        next_level = []
        ans = []
        while queue:
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_level.append(root.left)
                if root.right:
                    next_level.append(root.right)
            
            ans.append(sum(level)/len(level))
            queue = next_level
            next_level = []
            level = []
        return ans
        