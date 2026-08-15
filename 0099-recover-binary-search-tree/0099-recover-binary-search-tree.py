# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.temp = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            self.temp.append(root)
            dfs(root.right)
        dfs(root)
        first = second = None 
        for i in range(1,len(self.temp)):
            if self.temp[i-1].val > self.temp[i].val:
                if not first:
                    first = self.temp[i-1]
                second = self.temp[i]
        first.val,second.val = second.val,first.val
        