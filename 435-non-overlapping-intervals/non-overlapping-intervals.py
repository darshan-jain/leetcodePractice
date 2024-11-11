class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        total = len(intervals)
        count = 1
        intervals.sort(key=lambda x:x[1])
        freetime = intervals[0][1]


        for pairs in intervals[1:]:
            if freetime <= pairs[0]:
                count+=1
                freetime = pairs[1]
            
        return total-count
        