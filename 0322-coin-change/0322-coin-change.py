class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins)==0:
            return 0 
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            if i!=amount+1:
                for c in coins:
                    if (i+c)<len(dp):
                        dp[i+c] = min(dp[i+c],dp[i]+1 )
        return dp[-1] if dp[-1]!=amount+1 else -1
                    
        
        