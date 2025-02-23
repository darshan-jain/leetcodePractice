# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxval):
            if node is None:
                return 
            nonlocal ans
            if maxval<=node.val:
                ans+=1
                maxval = node.val
            dfs(node.left,maxval)
            dfs(node.right,maxval)



        ans = 0 
        dfs(root,float("-inf"))
        return ans
        