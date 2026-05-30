# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        level = 1
        anslevel = 0

        q = [root]
        while q:
            next_level = []
            res = []
            for item in q:
                res.append(item.val)
                if item.left:
                    next_level.append(item.left)
                if item.right:
                    next_level.append(item.right)
            if sum(res) > ans:
                ans = sum(res)
                anslevel = level


            q = next_level
            level+=1
        return anslevel

        