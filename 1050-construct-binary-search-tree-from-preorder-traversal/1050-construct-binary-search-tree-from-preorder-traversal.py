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
        # if len(preorder)==1:
        #     return TreeNode(preorder[0])
        root = preorder[0]
        idx = len(preorder)
        for i in range(len(preorder)):
            if preorder[i] > root:
                idx = i
                break
        
        node = TreeNode(root)
        if len(preorder)>1:
            node.left = self.bstFromPreorder(preorder[1:idx])
            node.right = self.bstFromPreorder(preorder[idx:])
        return node
        