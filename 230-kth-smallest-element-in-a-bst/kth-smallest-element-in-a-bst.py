# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count = 0 
    def helper(self,root,k):
        if root is None:
            return None
        left = self.helper(root.left,k)
        if left is not None:
            return left 
        self.count+=1
        if self.count==k:
            return root
        return self.helper(root.right,k)
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        node =  self.helper(root,k)
        return node.val
        

        