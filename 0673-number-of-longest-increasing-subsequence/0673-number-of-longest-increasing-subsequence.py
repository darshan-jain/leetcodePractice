class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        lenLIS , res = 0,0 

        for i in range(n-1,-1,-1):
            maxLen, maxCnt = 1,1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length+1>maxLen:
                        maxLen,maxCnt = 1+length, count
                    elif length+1==maxLen:
                        maxCnt+=count 
            
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt 
            elif maxLen==lenLIS:
                res+=maxCnt
            dp[i] = maxLen, maxCnt
        return res


        