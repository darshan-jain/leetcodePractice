class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)

        UNVISITED = 0 
        VISITING = 1 
        VISITED = 2 
        res = []
        state = [UNVISITED for _ in range(numCourses)]

        def dfs(course):
            if state[course]==VISITED:
                return True
            if state[course]==VISITING:
                return False 
            state[course] = VISITING
            for nei in graph[course]:
                if dfs(nei)==False:
                    return False
            state[course] = VISITED
            res.append(course)
            return True
        
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return res

        
        