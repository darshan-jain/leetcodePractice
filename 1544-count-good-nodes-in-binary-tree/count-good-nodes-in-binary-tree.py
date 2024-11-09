# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.good = 0 
        def dfs(root,check):
            if root.val >= check:
                self.good +=1
            if root.left:
                dfs(root.left,max(check,root.val))
            if root.right:
                dfs(root.right,max(check,root.val))
        dfs(root,root.val)
        return self.good
        