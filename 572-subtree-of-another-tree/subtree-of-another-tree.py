# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p,q):
            if p is None or q is None:
                return p==q
            return p.val==q.val and same(p.left,q.left) and same(p.right,q.right)
        
        if root is None:
            return False
        return same(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)

        