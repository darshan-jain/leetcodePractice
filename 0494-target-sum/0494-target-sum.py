class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(idx, val):
            if idx == len(nums):
                if val == target:
                    return 1 
                else:
                    return 0 
            if (idx, val) in dp :
                return dp[(idx,val)]
            dp[(idx,val)] =  dfs(idx+1,val+nums[idx]) + dfs(idx+1, val-nums[idx])
            return dp[(idx,val)]
        


        return dfs(0,0)