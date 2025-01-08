class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currsum =0 
        maxsum  = nums[0]
        for num in nums:
            currsum = max(currsum+num,num)
            maxsum = max(maxsum,currsum)
        return maxsum
        