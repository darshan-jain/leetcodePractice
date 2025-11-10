from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        def cycle(course,seen):
            if course in seen:
                return True
            seen.add(course)
            for nei in graph[course]:
                if cycle(nei,seen):
                    return True
            seen.remove(course)
            graph[course]=[]
            return False
        

        seen = set()
        for i in range(numCourses):
            if cycle(i,seen):
                return False 
        return True
        