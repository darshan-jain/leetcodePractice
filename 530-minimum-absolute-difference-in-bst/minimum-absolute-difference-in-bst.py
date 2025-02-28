# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if not root:
                return [] 
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        lst = inorder(root)
        min_dist = math.inf
        for i in range(1,len(lst)):
            dist = lst[i]-lst[i-1]
            min_dist = min(min_dist, dist)
        
        return min_dist
        