class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src==dst:
            return 0 
        graph = defaultdict(list)
        for fro,to,cost in flights:
            graph[fro].append((to,cost))
        
        q = deque([(src,0,0)]) #src, stops, price 
        
        prices = [float("inf")] * n
        prices[src] = 0 
        
        while q:
            node, stops, price = q.popleft()
            if stops >k:
                continue
            for nei,pp in graph[node]:
                if price + pp < prices[nei]:
                    prices[nei] = price + pp
                    q.append((nei, stops+1, prices[nei]))
        return prices[dst] if prices[dst]!=float("inf") else -1


                
        