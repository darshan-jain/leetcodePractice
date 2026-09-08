# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        toDelete = set(to_delete)

        def dfs(root, isRoot):
            if not root:
                return None 
            deleted = root.val in toDelete
            if isRoot and not deleted:
                ans.append(root)
            root.left = dfs(root.left, deleted)
            root.right = dfs(root.right, deleted)
            return None if deleted else root


        dfs(root,True)
        return ans
        