import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        minheap = [(0,0)]
        total_cost = 0 
        n = len(points)

        while minheap:
            dist,i = heapq.heappop(minheap)
            if i in seen:
                continue
            total_cost+=dist 
            seen.add(i)
            xi,yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj,yj = points[j]
                    val = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(minheap, (val, j))
        return total_cost
                    
        