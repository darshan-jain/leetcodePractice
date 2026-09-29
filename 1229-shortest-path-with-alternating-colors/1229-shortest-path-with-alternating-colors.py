class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for edge in redEdges:
            u = edge[0]
            v = edge[1]
            graph[u].append((v,"r"))
        for edge in blueEdges:
            a = edge[0]
            b = edge[1]
            graph[a].append((b,"b"))
        for i in range(n):
            if i not in graph:
                graph[i] = []
        
        def bfs(s,e,c):
            q = deque([(s,c,0)]) #start, color, dist
            visit = set()
            while q:
                node, color, dist = q.popleft()
                if node == e:
                    return dist
                if (node,color) in visit:
                    continue
                visit.add((node,color))
                for nei,cc in graph[node]:
                    if cc!=color:
                        q.append((nei, cc,dist+1))
            return float("inf")




        res = []
        for i in range(n):
            dist1 = bfs(0,i,"r")
            dist2 = bfs(0,i,"b")
            if dist1==float("inf") and dist2==float("inf"):
                res.append(-1)
            elif dist1<=dist2:
                res.append(dist1)
            else:
                res.append(dist2)
        return res
        