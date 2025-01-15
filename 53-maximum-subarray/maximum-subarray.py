class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0 
        max_sum = nums[0]
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum,curr_sum)
        return max_sum
        