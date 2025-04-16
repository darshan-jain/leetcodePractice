# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if root is None:
        #     return None
        # def inorder(root):
        #     if root is None:
        #         return []
        #     return inorder(root.left) + [root.val] + inorder(root.right)
        
        # val = inorder(root)
        # print(val)
        # return val[k-1]
        
        #Better Approach 
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1
            if k==0:
                return root.val
            root = root.right