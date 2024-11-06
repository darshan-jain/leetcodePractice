class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        maxp = 0 
        for price in prices:
            buy = min(buy,price)
            maxp = max(maxp,price-buy)
        return maxp
        