class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #recursive soln is exhaustive 
        if m==n==1:
            return 1 
        dp = [[0]*n]*m
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
        