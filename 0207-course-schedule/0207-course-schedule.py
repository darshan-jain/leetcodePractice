
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        seen = set()
        #this fnc returns True if cycle exits, False otherwise
        def cycle(course,seen):
            if course in seen:
                return True
            seen.add(course)
            for c in graph[course]:
                if cycle(c,seen):
                    return True
            seen.remove(course)
            graph[course] = []
            return False

        for n in range(numCourses):
            if cycle(n,seen):
                return False
        return True

        