# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        res = []
        while q:
            next_level = []
            for node in q:
                if node is None:
                    continue
                if node.left:
                    next_level.append(node.left)
                else:
                    next_level.append(None)
                if node.right:
                    next_level.append(node.right)
                else:
                    next_level.append(None)
            res.append(q)
            q = next_level
        h = len(res[:-1])
        for level in range(h-1):
            for node in res[level]:
                if node is None:
                    return False
        nullflag = False
        for node in res[h-1]:
            if node == None:
                nullflag = True
            
            if nullflag and node is not None:
                return False 
        return True



        