import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap  = [] 
        for elem in nums:
            if len(minheap) < k : 
                heapq.heappush(minheap, elem)
            elif elem > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap,elem)
        return minheap[0]
        