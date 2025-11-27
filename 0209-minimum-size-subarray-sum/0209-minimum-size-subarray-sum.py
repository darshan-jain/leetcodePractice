class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        left=0 
        right = 0 
        minLen = float("inf")
        curr_val = 0 


        while right<len(nums):
            curr_val+=nums[right]
            right+=1

            while curr_val>=target:
                winSize = right - left
                minLen = min(minLen, winSize)
                curr_val-=nums[left]
                left+=1
            
        return max(0,minLen)