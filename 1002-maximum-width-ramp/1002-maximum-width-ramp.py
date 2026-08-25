class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        s = []
        res = 0 
        for i,num in enumerate(nums):
            if not s or nums[s[-1]] > num:
                s.append(i)
        for j in range(len(nums)-1,-1,-1):
            while s and nums[j]>=nums[s[-1]]:
                res = max(res, j-s.pop())
        return res
        