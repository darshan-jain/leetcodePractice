# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # def inorder(root):
        #     if not root:
        #         return [] 
        #     return inorder(root.left) + [root.val] + inorder(root.right)
        
        # lst = inorder(root)
        # min_dist = math.inf
        # for i in range(1,len(lst)):
        #     dist = lst[i]-lst[i-1]
        #     min_dist = min(min_dist, dist)
        
        # return min_dist

        self.min_diff = float("inf")
        self.prev_val = None
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff,abs(self.prev_val - root.val))
            self.prev_val = root.val
            dfs(root.right)
        dfs(root)
        return self.min_diff
                