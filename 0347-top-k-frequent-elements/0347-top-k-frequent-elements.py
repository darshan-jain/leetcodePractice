import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  =Counter(nums)
        maxheap = []
        for a,v in count.items():
            heapq.heappush(maxheap, (-v,a))
        
        res = []
        while k>0:
            freq, val = heapq.heappop(maxheap)
            res.append(val)
            k-=1
        return res
        