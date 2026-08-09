class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        nodes = set()
        for i in range(len(equations)):
            start = equations[i][0]
            end = equations[i][1]
            val = values[i]
            graph[start].append((end, val))
            graph[end].append((start, 1/val))
            nodes.add(start)
            nodes.add(end)
        
        
        def bfs(start, end,visited):
            if start == end:
                return 1 
            q = deque([(start, 1)])
            while q:
                node, dist = q.popleft()
                if node == end:
                    return dist
                visited.add(node)
                for nei,vv in graph[node]:
                    if nei not in visited:
                        q.append((nei, dist*vv))
            return -1



        res = []
        for q in queries:
            start = q[0]
            end = q[1]
            if start not in nodes or end not in nodes:
                res.append(-1)
            else:
                visited = set()
                val = bfs(start, end,visited)
                res.append(val)
        return res



        