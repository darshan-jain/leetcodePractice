# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # node = TreeNode(val)
        # if root is None:
        #     return node
        # def dfs(par,root):
        #     if par is not None and root is None:
        #         if par.val > val:
        #             par.left = node 
        #         else:
        #             par.right = node 
        #         return 
        #     if root.val < val:
        #         return dfs(root,root.right)
        #     else:
        #         return dfs(root,root.left)
        # dfs(None, root)
        # return root
        
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right,val)
        else:
            root.left = self.insertIntoBST(root.left,val)
        return root