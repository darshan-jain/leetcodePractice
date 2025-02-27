import heapq
class Solution:
    def calcdist(self,x,y):
        return x**2 + y**2
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            dist = self.calcdist(point[0],point[1])
            heapq.heappush(minHeap, (dist,point[0],point[1]))
        
        res = []
        while k > 0:
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        
        return res

        