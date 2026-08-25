class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            if manager[i]==-1:
                continue
            graph[manager[i]].append((i,informTime[i]))
        
        
        q = deque([(headID, informTime[headID])]) #id, time
        dist = [float("inf")]*n
        dist[headID] = informTime[headID]
        visit = set()
        while q:
            id,time = q.popleft()
            if id in visit:
                continue
            if dist[id]>=time:
                dist[id] = time
                       
            visit.add(id)
            for nei,tt in graph[id]:
                if nei not in visit:
                    q.append((nei, time+tt))
        return max(dist)
        
            

        