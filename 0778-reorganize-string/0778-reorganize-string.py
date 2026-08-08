import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        maxheap = []
        for k,v in cnt.items():
            heapq.heappush(maxheap, (-v,k))
        res = ""
        while len(maxheap)>1:
            topcnt, topchar = heapq.heappop(maxheap)
            nextcnt, nextchar = heapq.heappop(maxheap)
            if topcnt+1:
                heapq.heappush(maxheap, (topcnt+1, topchar))
            if nextcnt+1:
                heapq.heappush(maxheap, (nextcnt+1, nextchar))
            res+=topchar
            res+=nextchar
        
        if maxheap:
            cnt, val = heapq.heappop(maxheap)
            cnt*=-1
            if cnt>1 or(res and val==res[-1]):
                return ""
            res+=val
        return res
    

        