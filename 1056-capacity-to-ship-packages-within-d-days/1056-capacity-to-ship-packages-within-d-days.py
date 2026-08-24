class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = float("inf")
        l = max(weights)
        r = sum(weights)

        def canShip(cap):
            day=1
            curr = 0 
            for w in weights:
                if curr+w <=cap:
                    curr+=w
                else:
                    day+=1
                    curr = w
            return day<=days

        while l<=r:
            m = (l+r)//2
            if canShip(m):
                res = min(res,m)
                r = m-1
            else:
                l = m+1
        return res
        