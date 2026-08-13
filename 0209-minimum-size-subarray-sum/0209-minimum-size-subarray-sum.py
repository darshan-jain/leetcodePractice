class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0 
        l = 0 
        r = 0 
        minLen = len(nums)
        curr_sum = 0 
        while r<len(nums):
            curr_sum+=nums[r]
            while curr_sum >= target:
                minLen = min(minLen, r-l+1)  
                curr_sum-=nums[l]
                l+=1
            r+=1
        return minLen



        