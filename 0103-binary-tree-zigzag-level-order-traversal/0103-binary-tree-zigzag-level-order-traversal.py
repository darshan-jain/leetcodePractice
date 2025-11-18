# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = [root]
        turn = 0 
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
            if turn%2==0:
                res.append(level)
            else:
                res.append(level[::-1])
            turn+=1
            q = next_level
        return res

        