import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for ele in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, ele)
            elif ele > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, ele)
        return minheap[0]

        