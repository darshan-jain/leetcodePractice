class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        dp =  [[1]*m]*n
        for row in range(1,len(dp)):
            for col in range(1,len(dp[0])):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[-1][-1]
        
        #Recursive Soln  - TLE 
        # if m==1 or n==1:
        #     return 1
        # return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)