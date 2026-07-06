class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(m):
            val = 0 
            for pile in piles:
                val+=math.ceil(pile/m)
            return val<=h
        l = 1
        r = max(piles)
        k = max(piles)
        while l<=r:
            m = (l+r)//2
            if canEat(m):
                k = min(k,m)
                r = m-1
            else:
                l = m+1
        return k
        