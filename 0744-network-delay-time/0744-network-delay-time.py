from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        mintime = {}
        minheap = [(0,k)]  #time, node

        while minheap:
            time_k_i , i = heapq.heappop(minheap)
            if i in mintime:
                continue
            mintime[i] = time_k_i 
            for nei, nei_time in graph[i]:
                if nei not in mintime:
                    heapq.heappush(minheap, (time_k_i+nei_time, nei))
        if len(mintime)==n:
            return max(mintime.values())
        else:
            return -1

        