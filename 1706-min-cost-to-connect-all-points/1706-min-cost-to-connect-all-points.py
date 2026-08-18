import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = []
        #cost,index
        heapq.heappush(minheap, (0,0))
        def dist(x1,y1,x2,y2):
            return abs(x2-x1) + abs(y2-y1)
        totcost = 0 
        visited= set()
        while minheap:
            cost,idx = heapq.heappop(minheap)
            if idx in visited:
                continue
            if idx not in visited:
                totcost+=cost
            visited.add(idx)
            
            for i in range(len(points)):
                if i not in visited:
                    cc = dist(points[idx][0], points[idx][1], points[i][0], points[i][1])
                    heapq.heappush(minheap, (cc,i))
        return totcost


                

        