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
        queue = [root]
        level = []
        next_level = []
        i =0 
        result = []

        while queue:
            
            for root in queue:
                level.append(root.val)
                
                if root.left:
                    next_level.append(root.left)
                if root.right:
                    next_level.append(root.right)
                
            if i%2==0:
                result.append(level)
            else:
                result.append(level[::-1])
            i+=1
            queue = next_level
            level = []
            next_level = []

        return result
        