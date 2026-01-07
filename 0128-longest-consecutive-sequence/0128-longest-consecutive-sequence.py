class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        maxLen = 0 

        for num in nums:
            curnum = num
            curlen = 1 
            if curnum-1 not in nums:
                while curnum+1 in nums:
                    curnum = curnum+1
                    curlen+=1
                maxLen = max(maxLen, curlen)
        return maxLen
        