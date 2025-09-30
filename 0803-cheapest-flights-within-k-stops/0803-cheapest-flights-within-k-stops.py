from collections import defaultdict,deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src ==dst:
            return 0
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        
        price = [float("inf") for _ in range(n)]

        q = deque([(src,0,0)])
        price[src] = 0 
        
        while q:
            node, cost, stops = q.popleft()
            if stops>k:
                continue
            for nei, wt in graph[node]:
                if price[nei] > cost + wt:
                    price[nei] = cost + wt
                    q.append((nei, price[nei] , stops+1))

        
        
        if price[dst]!=float("inf"):
            return price[dst]
        return -1



        