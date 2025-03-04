# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root,targetSum ,path):
            if root is None:
                return 
            if root.left is None and root.right is None and targetSum == root.val:
                ans.append(path + [root.val])
                return 
            path.append(root.val)
            dfs(root.left, targetSum - root.val, path)
            dfs(root.right,targetSum - root.val,path)
            path.pop()
        dfs(root,targetSum, [])
        return ans
        