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
        level = []
        result = []
        ans = []
        queue = [root]
        next_level = []

        while queue:
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_level.append(root.left)
                if root.right:
                    next_level.append(root.right)
            result.append(level)
            queue = next_level
            next_level = []
            level = []

        for res in result:
            ans.append(res[-1])

        return ans

        