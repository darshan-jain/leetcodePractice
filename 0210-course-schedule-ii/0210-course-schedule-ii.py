from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        res = []
        UNVISITED = 0 
        VISITING = 1
        VISITED = 2
        state = [UNVISITED for _ in range(numCourses)]

        def dfs(node):
            if state[node] == VISITING:
                return False
            if state[node] == VISITED:
                return True
            state[node] = VISITING
            for nei in graph[node]:
                if dfs(nei) == False:
                    return False
            state[node] = VISITED
            res.append(node)
            return True

        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return res
        