class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:x[1])

        remove = 0 
        end = intervals[0][0]
        for times in intervals:
            start = times[0]
            if start < end:
                remove+=1
            else:
                end = times[1]
        return remove