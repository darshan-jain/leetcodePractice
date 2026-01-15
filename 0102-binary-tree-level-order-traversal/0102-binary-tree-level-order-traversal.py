# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res= []
        while q:
            next_level = []
            for item in q:
                if item.left:
                    next_level.append(item.left)
                if item.right:
                    next_level.append(item.right)
            val = []
            for item in q:
                val.append(item.val)
            q = next_level
            res.append(val)
        return res
        
        