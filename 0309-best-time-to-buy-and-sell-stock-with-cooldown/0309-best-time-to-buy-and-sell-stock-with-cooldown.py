class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #state diagram solution - techdose 
        # n = len(prices)
        # nostock = [0]*n
        # inhand = [0]*n
        # sold = [0]*n
        # inhand[0]=-prices[0]
        # for i in range(1,n):
        #     nostock[i] = max(nostock[i-1], sold[i-1])
        #     inhand[i] = max(inhand[i-1], nostock[i-1]-prices[i])
        #     sold[i] = inhand[i-1]+prices[i]
        # return max(nostock[-1], sold[-1])
        
        #recursive solution - based on combination sum - memoized
        n = len(prices)
        mem = [-1]*(n+1)
        def findmax(prices, curr, n):
            #base case 
            if curr>=n:
                return 0 
            if mem[curr]!=-1:
                return mem[curr]
            maxval = 0
            for i in range(curr+1,n):
                if prices[i] > prices[curr]:
                    maxval = max(maxval , prices[i]-prices[curr]+ findmax(prices,i+2, n))
            maxval = max(maxval, findmax(prices, curr+1,n))
            mem[curr] = maxval
            return maxval

        return findmax(prices,0, n)