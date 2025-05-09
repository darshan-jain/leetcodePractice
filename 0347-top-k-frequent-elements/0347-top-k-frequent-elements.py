import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            d[num] = 1+ d.get(num,0)
        
        maxHeap = []
        for val, count in d.items():
            heapq.heappush(maxHeap, (-count,val))
        res= []
        while k >0:
            count,val1 = heapq.heappop(maxHeap)
            res.append(val1)
            k-=1
        return res
