import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minHeap = [(0,0)]
        seen = set()
        total_cost = 0 

        while len(seen) < n:
            dist,i = heapq.heappop(minHeap)
            if i in seen:
                continue
            seen.add(i)
            total_cost+=dist
            xi,yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj,yj = points[j]
                    nei_dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(minHeap,(nei_dist,j))
        return total_cost
