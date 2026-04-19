class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = [(0,0)] #dist, node 
        total_cost = 0 
        seen = set()

        while minheap:
            dist,node = heapq.heappop(minheap)
            if node in seen:
                continue
            seen.add(node)
            total_cost+=dist
            xi,yi = points[node]
            for j in range(len(points)):
                if j not in seen:
                    xj,yj = points[j]
                    val = abs(xj-xi) + abs(yj-yi)
                    heapq.heappush(minheap, (val,j ))
        return total_cost

        