# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        # if root1 is None and root2 is None:
        #     return True
        # if root1 is None or root2 is None:
        #     return False

        # def levelorder(root):
        #     result = []
        #     q = [root]
        #     level = []
        #     next_level = []
        #     while q:
        #         for node in q:
        #             level.append(node.val)
        #             if node.left:
        #                 next_level.append(node.left)
        #             if node.right:
        #                 next_level.append(node.right)
        #         result.append(level)
        #         q = next_level
        #         level = []
        #         next_level = []
        #     return result
        
        # arr1 = levelorder(root1)
        # arr2 = levelorder(root2)

        # for item1, item2 in zip(arr1,arr2):
        #     if sorted(item1)!=sorted(item2):
        #         return False
        # return True

        if not r1 or not r2:
            return not r1 and not r2
        if r1.val!=r2.val:
            return False
        
        a = self.flipEquiv(r1.left,r2.left) and self.flipEquiv(r1.right,r2.right)
        return a or self.flipEquiv(r1.left,r2.right) and self.flipEquiv(r1.right, r2.left)
        