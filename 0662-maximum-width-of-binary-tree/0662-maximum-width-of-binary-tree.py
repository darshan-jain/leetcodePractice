# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        q = [(root,1)]
        ans = 1
        while q:
            next_level = []
            for elem, pos in q:
                if elem.left:
                    next_level.append([elem.left,2*pos])
                if elem.right:
                    next_level.append([elem.right, 2*pos+1])
            if next_level:
                ans = max(ans, next_level[-1][1] - next_level[0][1]+1)
            q = next_level
        return ans 



        