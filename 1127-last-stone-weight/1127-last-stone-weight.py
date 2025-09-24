import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        maxheap = []
        for vals in stones:
            heapq.heappush(maxheap, -1*vals)
        
        while len(maxheap)>1:
            y = heapq.heappop(maxheap)
            y = y*(-1)
            x = heapq.heappop(maxheap)
            x = x*(-1)
            if x!=y:
                heapq.heappush(maxheap, -1*(y-x))
            if len(maxheap)==1:
                return -1*maxheap[0]
            if len(maxheap)==0:
                return 0


        