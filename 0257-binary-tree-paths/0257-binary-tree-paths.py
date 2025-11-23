# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root,curr):
            if root is None:
                return 
            if root.left is None and root.right is None:
                ans.append(''.join(curr) + str(root.val))
            curr.append(str(root.val)+'->')
            dfs(root.left,curr )
            dfs(root.right, curr)
            curr.pop()
        
        if root is None:
            return ans
        dfs(root,[])
        return ans
        