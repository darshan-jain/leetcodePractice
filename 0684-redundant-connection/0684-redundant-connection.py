from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        res = []
        

        def dfs(node, par):
            if vis[node]==1:
                return True
            vis[node]=1
            for nei in graph[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    return True
            return False


        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            vis = [0 for _ in range(n+1)]

            if dfs(a,-1):
                return [a,b]
        return []



