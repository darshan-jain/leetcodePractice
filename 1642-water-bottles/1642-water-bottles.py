class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        full = numBottles 
        ans = 0 
        empty = 0 
        while full>0:
            ans+=full
            empty+=full
            full = empty//numExchange
            empty = empty%numExchange 
        return ans