# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return None
        result = []
        q = [root]
        next_level = []
        level = []
        while q:
            for node in q:
                level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(level)
            q = next_level
            level = [] 
            next_level= []
        
        val = result[-1]
        return val[0]
        