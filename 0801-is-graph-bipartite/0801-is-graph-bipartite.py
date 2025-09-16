class Solution:
    def dfs(self, node, col, graph, colors):
        colors[node]= col
        for vals in graph[node]:
            if colors[vals]==-1:
                if self.dfs(vals, not col, graph, colors)== False:
                    return False
            elif colors[node]==colors[vals]:
                return False
        return True
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        colors = [-1 for _ in range(V)]
        for i in range(V):
            if colors[i]==-1:
                if self.dfs(i,0,graph, colors)==False:
                    return False
        return True
        