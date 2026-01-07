class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or 1 not in nums:
            return 1 
        
        for i,num in enumerate(nums):
            if num <=0 or num > len(nums):
                nums[i] = 1
        
        for i,num in enumerate(nums):
            tochange = abs(num)-1
            if nums[tochange] > 0:
                nums[tochange]*=-1
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1
        