import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return x*x + y*y
        heap = []
        for point in points:
            x,y = point[0], point[1]
            d = dist(x,y)
            heapq.heappush(heap,(d,x,y))
        res = []
        while k>0:
            d,x,y = heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res

        