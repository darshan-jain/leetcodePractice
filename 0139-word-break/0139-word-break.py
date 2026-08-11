# leetcode
# 01234567

#   i
# T F F F T F F F T
# 0 1 2 3 4 5 6 7 8



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]
        