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
        q = [root]
        res = []
        while q:
            next_level = []
            temp = []
            for node in q:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            for item in q:
                temp.append(item.val)
            res.append(temp)
            q = next_level
        return res
        