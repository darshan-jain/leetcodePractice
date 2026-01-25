class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word2)+1
        cols = len(word1)+1

        dp = [[0]*cols for _ in range(rows)]

        for i in range(rows):
            dp[i][0] = i 
        
        for j in range(cols):
            dp[0][j] = j
        
        for i in range(1,rows):
            for j in range(1,cols):
                if word1[j-1]==word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[-1][-1]
        