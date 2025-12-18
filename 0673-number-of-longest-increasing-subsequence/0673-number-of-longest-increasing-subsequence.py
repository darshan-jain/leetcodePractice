class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        # nums = [1,3,5,4,7]

        # lenLis = [4,3,2,2,1]
        # count =  [2,2,1,1,1]

        dp = {} #index -> length of LIS, count 
        lenLis, res = 0,0

        for i in range(len(nums)-1,-1,-1):
            maxLen, maxCount = 1,1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length+1 > maxLen:
                        maxLen, maxCount = length+1, count
                    elif length+1==maxLen:
                        maxCount+=count
            if lenLis < maxLen:
                lenLis = maxLen
                res = maxCount
            elif lenLis==maxLen:
                res+=maxCount
            dp[i] = maxLen, maxCount
        return res
