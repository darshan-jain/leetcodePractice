# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        level = []
        next_level = []
        queue = [root]

        while queue:
            for root in queue:
                if root:
                    level.append(root.val)
                if root.left:
                    next_level.append(root.left)
                if root.right:
                    next_level.append(root.right)
            result.append(level)
            level = []
            queue = next_level
            next_level = []
        return result