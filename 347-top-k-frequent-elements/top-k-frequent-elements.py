import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(list)
        for ele in nums:
            hm[ele]=1 + hm.get(ele,0)
        

        maxHeap = []
        res = []
        for val, freq in hm.items():
            heapq.heappush(maxHeap, (-freq,val))
        
        while  k>0:
            freq,val = heapq.heappop(maxHeap)
            res.append(val)
            k-=1
        
        return res

        