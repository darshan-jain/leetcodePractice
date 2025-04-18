# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return True
        def sameTree(p,q):
            if p is None or q is None:
                return p==q
            return p.val==q.val and sameTree(p.left,q.left) and sameTree(p.right, q.right)
        
        return sameTree(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        