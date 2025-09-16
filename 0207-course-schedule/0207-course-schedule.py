from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq = defaultdict(list)
        for p,c in prerequisites:
            prereq[c].append(p)
        
        def cycle(course, seen):
            if course in seen:
                return True
            seen.add(course)
            for c in prereq[course]:
                if cycle(c,seen):
                    return True
            prereq[course] = []
            seen.remove(course)
            return False
            

        
        seen = set()  # set to keep track of courses done so far
        for course in range(numCourses):
            if cycle(course, seen):
                return False
        return True
        