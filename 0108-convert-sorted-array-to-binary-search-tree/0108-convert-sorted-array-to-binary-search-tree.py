# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        val = nums[len(nums)//2]
        ind = len(nums)//2
        node = TreeNode(val)
        node.left = self.sortedArrayToBST(nums[0:ind])
        node.right = self.sortedArrayToBST(nums[ind+1:])
        return node
        