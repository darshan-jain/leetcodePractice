class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r 
        while l<=r:
            k = (l+r)//2
            hrs = 0 
            for item in piles:
                hrs+=math.ceil(item/k)
            
            if hrs<=h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1
        return res

        