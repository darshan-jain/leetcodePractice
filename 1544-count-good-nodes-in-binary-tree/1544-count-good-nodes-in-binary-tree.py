# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        count = 0 
       
    
        def dfs(root, maxval):
            if root is None:
                return 
            # if root.left and root.right is None:
            #     return 1
            nonlocal count
            if root.val >= maxval:
                count+=1
                maxval = root.val
            if root.left:
                left  = dfs(root.left,maxval )
            if root.right:
                right = dfs(root.right, maxval)
            return
            


        dfs(root, root.val)
        return count

        