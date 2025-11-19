# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def dfs(self,root ,path, target):
        if root is None:
            return
        if root.left is None and root.right is None and target-root.val==0:
            path.append(root.val)
            self.res.append(path)
            return 
        return self.dfs(root.left, path + [root.val], target-root.val) or self.dfs(root.right, path + [root.val], target-root.val)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.dfs(root, [], targetSum)
        return self.res
        