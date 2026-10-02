import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minheap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = x**2 + y**2
            heapq.heappush(minheap, (dist, x,y))
        res = []
        while k>0:
            _,xx,yy = heapq.heappop(minheap)
            res.append([xx,yy])
            k-=1
        return res

        