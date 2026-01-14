import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mink = float("inf")
        while l<=r:
            m = (l+r)//2
            totalh = 0
            for val in piles:
                totalh+= math.ceil(val/m)
            if totalh <=h:
                mink = min(mink,m)
                r= m-1
            elif totalh > h:
                l = m+1
        return mink



        