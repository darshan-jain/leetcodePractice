import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -1*stone)
        
        print(maxHeap)

        while len(maxHeap) > 1:
            x = -1* heapq.heappop(maxHeap)
            y = -1*heapq.heappop(maxHeap)
            if x==y:
                continue
            else:
                new_weight = abs(x-y)
                heapq.heappush(maxHeap, -1*new_weight)

        if len(maxHeap) == 1:
            return -1*heapq.heappop(maxHeap)
        else:
            return 0 

        