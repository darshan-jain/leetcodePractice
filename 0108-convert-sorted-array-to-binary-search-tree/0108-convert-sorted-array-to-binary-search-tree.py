# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) ==0 :
            return None
        val = nums[len(nums)//2]
        root = TreeNode(val)
        root.left = self.sortedArrayToBST(nums[0:len(nums)//2])
        root.right = self.sortedArrayToBST(nums[len(nums)//2+1:])
        return root
        