import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxheap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(maxheap, -1*matrix[i][j])
                if len(maxheap) > k:
                    heapq.heappop(maxheap)
        return -1*maxheap[0]

        