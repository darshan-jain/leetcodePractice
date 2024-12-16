class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==n==1:
            return 1
        dp = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(1)
            dp.append(row)
        for row in range(1,len(dp)):
            for col in range(1,len(dp[row])):
                dp[row][col] = dp[row-1][col]+dp[row][col-1]
        return dp[-1][-1]

        