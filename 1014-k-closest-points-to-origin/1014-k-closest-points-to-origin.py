import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return x*x + y*y
        n = len(points)
        minheap = []
        for i in range(n):
            x,y = points[i][0], points[i][1]
            d=dist(x,y)
            heapq.heappush(minheap, (d,x,y))
        
        res = []
        while k>0:
            d,x,y = heapq.heappop(minheap)
            res.append([x,y])
            k-=1
        return res

        