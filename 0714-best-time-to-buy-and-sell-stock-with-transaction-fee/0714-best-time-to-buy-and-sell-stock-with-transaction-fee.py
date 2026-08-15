class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0 
        hold = prices[0]
        for price in prices[1:]:
            profit = max(profit, price -hold - fee)
            hold = min(hold, price - profit)
        return profit

        