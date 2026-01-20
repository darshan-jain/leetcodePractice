class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        i=0
        for a,b in equations:
            val = values[i]
            graph[a].append((b,val))
            graph[b].append((a,1/val))
            i+=1
        
        nodes = set()
        for k in graph.keys():
            nodes.add(k)
        
        und = -1
        same = 1
        res = []

        for a,c in queries:
            visited = set()
            visited.add(a)
            if a==c and a in nodes:
                res.append(same)
                continue
            if a not in nodes or c not in nodes:
                res.append(und)
                continue
            queue = deque([(a,1)])
            while queue:
                node,val = queue.popleft()
                if node ==c:
                    res.append(val)
                    break
                for nei in graph[node]:
                    if nei[0] not in visited:
                        queue.append((nei[0],val*nei[1]))
                    visited.add(nei[0])
            
            if c not in visited:
                res.append(und)
        return res





            




        