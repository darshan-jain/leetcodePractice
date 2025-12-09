class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = [0]*n 
        dp = [0]*n 
        dp[0] = prices[0]
        for i in range(1,len(prices)):
            price = prices[i]
            minbuy = min(price, dp[i-1])
            dp[i] = minbuy
            profit[i] = price - minbuy
        return max(profit)
        