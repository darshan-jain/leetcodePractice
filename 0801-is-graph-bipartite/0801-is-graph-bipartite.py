class Solution:
    def dfs(self, node, col, graph, color):
        color[node] = col
        for val in graph[node]:
            if color[val]==-1:
                if self.dfs(val,not col, graph,color)==False:
                    return False
            elif color[val]==color[node]:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1 for _ in range(V)]
        for i in range(V):
            if color[i]==-1:
                if self.dfs(i,0,graph, color)==False:
                    return False
        return True
        