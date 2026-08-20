class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i,tot):
            if i==len(nums):
                if tot == target:
                    return 1
                else:
                    return 0 
            if (i,tot) in dp:
                return dp[(i,tot)]
            dp[(i,tot)]= dfs(i+1, tot + nums[i]) + dfs(i+1, tot-nums[i])
            return dp[(i,tot)]


        return dfs(0,0)
        