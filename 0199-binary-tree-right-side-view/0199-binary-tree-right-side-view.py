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
        result = []
        q = [root]
        level = []
        next_level = []
        while len(q)!=0:
            for node in q:
                level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(level)
            q= next_level
            level = []
            next_level = []
        
        #result 
        final_res = []
        for item in result:
            final_res.append(item[-1])
        return final_res
        