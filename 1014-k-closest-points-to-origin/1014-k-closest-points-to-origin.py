import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getdist(x,y):
            return sqrt((x*x) + (y*y))
        minheap = []
        res = []
        for x,y in points:
            dist = getdist(x,y)
            heapq.heappush(minheap, (dist, x,y))

        while k>0:
            dist,x,y = heapq.heappop(minheap)
            vals = [x,y]
            res.append(vals)
            k-=1
        return res
        
        