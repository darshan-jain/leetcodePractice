# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None 
        idx = len(preorder)
        for i in range(1,len(preorder)):
            if preorder[i]>preorder[0]:
                idx = i 
                break
        node = TreeNode(preorder[0])
        node.left = self.bstFromPreorder(preorder[1:idx])
        node.right = self.bstFromPreorder(preorder[idx:])
        return node

