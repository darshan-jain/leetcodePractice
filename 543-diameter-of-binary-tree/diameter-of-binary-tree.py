# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 

        def height(root):
            if root is None:
                return 0 
            leftD = height(root.left)
            rightD = height(root.right)
            dia = leftD+rightD
            self.res = max(self.res,dia)
            return max(leftD,rightD)+1
        
        height(root)
        return self.res
            
        