# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        if root is None:
            return 0 
        def helper(root,maxx):
            if root is None:
                return
            if root.val >= maxx:
                nonlocal cnt
                cnt+=1
                maxx = root.val
            helper(root.left, maxx)
            helper(root.right, maxx)

        
        helper(root,root.val)
        return cnt
        