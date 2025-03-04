# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        lst1 = self.inorder(root1)
        lst2 = self.inorder(root2)
        
        lst3 = lst1 + lst2
        lst3.sort()
        return lst3

        