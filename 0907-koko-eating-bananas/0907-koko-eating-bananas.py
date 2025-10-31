class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = max(piles)
        if len(piles)==h:
            return max(piles)
        l = 1
        r = n 
        minhrs = float("inf")
        ans = 0 
        while l< r:
            m = (l+r)//2
            hrs = 0 
            for item in piles:
                print(item,m)
                hrs+=ceil(item/m)
            
            if hrs<=h and hrs < minhrs:
                ans = m 
                r = m                 
            elif hrs > h : 
                l = m+1
            else:
                r=m
        return ans

        