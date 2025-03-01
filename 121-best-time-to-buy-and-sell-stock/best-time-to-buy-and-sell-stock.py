class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0 
        for num in prices:
            min_buy = min(min_buy,num)
            max_profit= max(max_profit, num - min_buy)
        return max_profit
        