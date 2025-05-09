class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minbuy = prices[0]
        maxProfit = 0 
        for num in prices[1:]:
            minbuy = min(minbuy, num)
            maxProfit = max(maxProfit, num - minbuy )
        return maxProfit
        