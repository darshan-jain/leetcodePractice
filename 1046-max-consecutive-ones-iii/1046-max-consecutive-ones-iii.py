class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = float("-inf")
        l = 0 
        r = 0 
        c1 = 0 
        while r<len(nums):
            if nums[r]==1:
                c1+=1
            while l<=r and (r-l+1) > c1+k:
                if nums[l]==1:
                    c1-=1
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res

        