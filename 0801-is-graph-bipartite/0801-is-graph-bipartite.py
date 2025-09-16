from collections import deque
class Solution:
    def check(self,start,V,graph, color):
        q = deque()
        q.append(start)
        color[start] = 0 
        while q:
            node = q.popleft()
            for val in graph[node]:
                if color[val]==-1:
                    color[val] = 1-color[node]
                    q.append(val)
                elif color[val]==color[node]:
                    return False
        return True
            

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1 for _ in range(V)]
        for i in range(V):
            if color[i]==-1:
                if self.check(i,V,graph, color)==False:
                    return False
        return True
        