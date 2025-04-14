class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def longestCommonSubseq(word1, word2):
            dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
            for row in range(1,len(word1)+1):
                for col in range(1,len(word2)+1):
                    if word1[row-1]==word2[col-1]:
                        dp[row][col] = dp[row-1][col-1]+1
                    else:
                        dp[row][col] = max(dp[row-1][col],dp[row][col-1])
            return dp[-1][-1]
        
        return longestCommonSubseq(s,s[::-1])
        