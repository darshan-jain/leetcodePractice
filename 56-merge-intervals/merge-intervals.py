class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        res =  [intervals[0]]
        for item in intervals[1:]:
            if res[-1][1] >= item[0]:
                res[-1][1] = max(res[-1][1],item[1])
            else:
                res.append(item)
        
        return res

        