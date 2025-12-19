# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        #base case
        if len(nums)==0:
            return None
        #find max val and maxValIdx
        maxVal=float("-inf")
        maxValIdx=-1
        for i in range(len(nums)):
            if nums[i] > maxVal:
                maxVal = nums[i]
                maxValIdx = i 
        node = TreeNode(val=maxVal)
        node.left = self.constructMaximumBinaryTree(nums[0:maxValIdx])
        node.right = self.constructMaximumBinaryTree(nums[maxValIdx+1:])
        return node