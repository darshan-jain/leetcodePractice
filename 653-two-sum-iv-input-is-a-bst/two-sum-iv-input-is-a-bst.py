# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        lst = inorder(root)
        print(lst)

        
        seen = {}
        for ind in range(len(lst)):
            num = lst[ind]
            if k - num in seen:
                val =  [ind,seen[k-num]]
                print(val)
                return True

            seen[num] = ind

        return False
        