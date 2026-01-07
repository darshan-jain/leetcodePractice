import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for ke,v in count.items():
            heapq.heappush(heap, (-v,ke))
        ans = []
        while k>0:
            freq, val = heapq.heappop(heap)
            ans.append(val)
            k-=1

        return ans

        