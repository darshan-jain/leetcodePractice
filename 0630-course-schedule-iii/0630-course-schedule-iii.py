import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        courses.sort(key = lambda x : x[1])

        max_time = 0 
        heap = []
        for dur,endtime in courses:
            max_time+=dur
            heapq.heappush(heap,-dur)
            if max_time > endtime:
                big_time = heapq.heappop(heap)
                max_time += big_time # + here since in maxheap we store -dur
        return len(heap)

        