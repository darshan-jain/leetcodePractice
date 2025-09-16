from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build the graph - adj list 
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        #detect cycle 
        def cycle(course, seen):
            if course in seen:
                return True
            seen.add(course)
            for c in graph[course]:
                if cycle(c,seen):
                    return True
            seen.remove(course)
            graph[course] = []
            return False

        seen = set()
        for i in range(numCourses):
            for course in graph[i]:
                if cycle(course,seen):
                    return False
        return True


        