class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        target = n-1
        for i in range(n-1,-1,-1):
            maxJump = nums[i]
            if i+maxJump >= target:
                target = i
            
        return target ==0 
        