class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #state diagram solution - techdose 
        n = len(prices)
        nostock = [0]*n
        inhand = [0]*n
        sold = [0]*n
        inhand[0]=-prices[0]
        for i in range(1,n):
            nostock[i] = max(nostock[i-1], sold[i-1])
            inhand[i] = max(inhand[i-1], nostock[i-1]-prices[i])
            sold[i] = inhand[i-1]+prices[i]
        return max(nostock[-1], sold[-1])
        