class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLen = 0 
        for num in nums:
            curNum = num
            curLen = 1
            if curNum-1 not in nums:
                while curNum+1 in nums:
                    curLen+=1
                    curNum+=1
                    maxLen = max(maxLen, curLen)
        return maxLen

        