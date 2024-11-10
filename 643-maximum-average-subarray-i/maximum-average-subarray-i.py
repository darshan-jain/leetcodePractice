class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_max = max_sum = sum(nums[:k])
        for i  in range(len(nums)-k):
            curr_max += nums[i+k] - nums[i]
            max_sum = max(curr_max,max_sum)        
        return float(max_sum)/k