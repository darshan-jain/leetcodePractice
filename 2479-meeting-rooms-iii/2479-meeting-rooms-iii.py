import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        cnt = [0]*n 
        occ = []
        avail = list(range(n))
        meetings.sort()
        for s,e in meetings:

            while occ and occ[0][0]<=s:
                _,r = heapq.heappop(occ)
                heapq.heappush(avail,r)

            if avail:
                r = heapq.heappop(avail)
                heapq.heappush(occ, (e,r))
                cnt[r]+=1
            else:
                olde,r = heapq.heappop(occ)
                heapq.heappush(occ,(olde+(e-s),r))
                cnt[r]+=1
        
        res = -1
        maxVal = -1 
        for i, val in enumerate(cnt):
            if val > maxVal:
                res = i 
                maxVal = val
        return res


        