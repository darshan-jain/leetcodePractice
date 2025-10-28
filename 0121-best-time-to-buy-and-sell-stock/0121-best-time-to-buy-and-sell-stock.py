class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        maxprofit = 0 
        for price in prices[1:]:
            minbuy = min(minbuy, price)
            profit = price - minbuy 
            maxprofit = max(maxprofit, profit)
        return maxprofit
        