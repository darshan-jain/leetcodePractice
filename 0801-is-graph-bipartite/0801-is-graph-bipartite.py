from collections import deque
class Solution:
    def check(self, start, V, graph, color):
        q = deque()
        q.append(start)
        color[start] = 0
        while q:
            node = q.popleft()
            for vals in graph[node]:
                if color[vals]==-1:
                    color[vals] = 1-color[node]
                    q.append(vals)
                elif color[vals]==color[node]:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        for i in range(len(graph)):
            if color[i]==-1:
                if self.check(i,len(graph), graph, color)==False:
                    return False
        return True

        
        



        