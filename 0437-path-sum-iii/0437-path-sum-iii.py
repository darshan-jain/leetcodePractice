# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count  = 0 
        self.freq = {0:1}
        def dfs(root,ps):
            if not root:
                return 
            cs = ps + root.val
            x = cs - targetSum
            if x in self.freq:
                self.count+=self.freq[x]
            if cs in self.freq:
                self.freq[cs]+=1
            else:
                self.freq[cs]=1
            dfs(root.left, ps+root.val)
            dfs(root.right, ps+root.val)
            self.freq[cs]-=1
        dfs(root,0)
        return self.count
        