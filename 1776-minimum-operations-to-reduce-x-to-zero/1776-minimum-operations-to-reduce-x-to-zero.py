class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums)-x 
        if x > sum(nums):
            return -1
        resLen=-1
        l = 0 
        r = 0 
        curr_val = 0 
        while r<len(nums):
            curr_val+=nums[r]
            while curr_val>target:
                curr_val-=nums[l]
                l+=1
            if curr_val==target:
                if resLen < (r-l+1):
                    resLen = (r-l+1)

            r+=1
        if resLen==-1:
            return -1 
        return n-resLen

        