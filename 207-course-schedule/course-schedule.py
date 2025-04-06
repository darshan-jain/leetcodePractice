class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prereqs = defaultdict(list)
        for p, c in prerequisites:
            prereqs[c].append(p)
        
        def cycle(course,seen):
            if course in seen:
                return True
            seen.add(course)
            for p in prereqs[course]:
                if cycle(p,seen):
                    return True
            prereqs[course] = []
            seen.remove(course)
            return False
        

        seen = set()
        for course in range(numCourses):
            if cycle(course,seen):
                return False
        return True
        