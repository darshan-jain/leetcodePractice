class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        dp = [[0]*(height+1) for _ in range(height+1)]
        for level in range(height-1, -1, -1):
            for i in range(0,level+1):
                dp[level][i] = triangle[level][i] + min(dp[level+1][i], dp[level+1][i+1])
        
        return dp[0][0]
        