class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m*k:
            return -1 
        
        def canMake(waitingDay):
            boneeded = 0 
            flowerreq = k 
            for day in bloomDay:
                if day > waitingDay:
                    flowerreq = k 
                else:
                    flowerreq-=1
                    if flowerreq==0:
                        boneeded+=1
                        flowerreq=k
            return boneeded >= m
        
        l = 1 
        r = max(bloomDay)
        res = float("inf")
        while l<=r:
            mid = (l+r)//2
            if canMake(mid):
                res = min(res, mid)
                r = mid-1
            else:
                l = mid+1
        return res
        