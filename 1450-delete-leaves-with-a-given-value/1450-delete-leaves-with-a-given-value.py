# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # if root is None:
        #     return None
        # if root.left is None and root.right is None and root.val==target:
        #     return None
        # def search(root):
        #     if root is None:
        #         return False 
        #     if root.left is None and root.right is None and root.val==target:
        #         return True
        #     return search(root.left) or search(root.right)
        
        # def dfs(par,root,le):
        #     if par is None and root.left is None and root.right is None and root.val ==target:
        #         return None
        #     if par is None and root is None:
        #         return
        #     if par is not None and root is None:
        #         return 
        #     if par is not None and root is not None and root.left is None and root.right is None and root.val==target:
        #         if le==1:
        #             par.left = None
        #         else:
        #             par.right = None
        #     dfs(root,root.left,1)
        #     dfs(root,root.right,0)
        #     return 5
        
        # while search(root):
        #     val = dfs(None, root,1)
        #     if val==None:
        #         root = None
        #         break

        
        # return root

        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right,target)

        if not root.left and not root.right and root.val==target:
            return None
        return root
        