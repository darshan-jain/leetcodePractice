import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        #take 2 elements at a time 
        hm = Counter(s)

        heap = [(-count,char) for char,count in hm.items()]
        heapq.heapify(heap)
        res = []

        while len(heap)>=2:
            topcount ,topchar = heapq.heappop(heap)
            nextcount,nextchar  = heapq.heappop(heap)
            res.append(topchar)
            res.append(nextchar)

            if topcount+1:
                heapq.heappush(heap, (topcount+1, topchar))
            if nextcount+1:
                heapq.heappush(heap,(nextcount+1, nextchar))
        
        if heap:
            topcount, topchar = heapq.heappop(heap)
            if topcount!=-1 or (res and topchar==res[-1]) :
                return ""
            else:
                res.append(topchar)
        return "".join(res)
        