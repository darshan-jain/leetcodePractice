class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        res = 0 
        end = intervals[0][0]
        for time in intervals:
            start = time[0]
            if start < end:
                res+=1
            else:
                end = time[1]
        return res
        