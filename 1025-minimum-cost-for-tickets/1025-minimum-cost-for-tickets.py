class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

        #top down approach
        dp = {}

        def dfs(i):
            if i == len(days):
                return 0 
            if i in dp:
                return dp[i]
            res = float("inf")
            j = i 
            for cost,duration in zip(costs,[1,7,30]):
                while j < len(days) and days[j] < days[i]+duration:
                    j+=1
                res = min(res, cost + dfs(j))
            dp[i] = res
            return res
        return dfs(0)