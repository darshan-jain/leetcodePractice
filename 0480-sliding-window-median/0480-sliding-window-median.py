import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxheap = []
        minheap = []
        res = []
        heap_dict = defaultdict(int)
        for i in range(k):
            heapq.heappush(maxheap, -nums[i])
            heapq.heappush(minheap, -heapq.heappop(maxheap))

            if len(minheap)>len(maxheap):
                heapq.heappush(maxheap, -heapq.heappop(minheap))
        if k%2==1:
            median = -maxheap[0]
            res.append(median)
        else:
            median = (-maxheap[0] + minheap[0])/2
            res.append(median)
        
        for i in range(k,len(nums)):
            prev_num = nums[i-k]
            heap_dict[prev_num]+=1

            bal = -1 if prev_num<=median else 1 

            if nums[i]<=median:
                bal+=1
                heapq.heappush(maxheap, -nums[i])
            else:
                bal-=1
                heapq.heappush(minheap, nums[i])
            
            if bal<0:
                heapq.heappush(maxheap, -heapq.heappop(minheap))
            elif bal>0:
                heapq.heappush(minheap, -heapq.heappop(maxheap))
            
            while maxheap and heap_dict[-maxheap[0]]>0:
                heap_dict[-maxheap[0]]-=1
                heapq.heappop(maxheap)
            while minheap and heap_dict[minheap[0]]>0:
                heap_dict[minheap[0]]-=1
                heapq.heappop(minheap)
            if k%2==1:
                median = -maxheap[0]
                res.append(median)
            else:
                median = (-maxheap[0] + minheap[0])/2
                res.append(median)
        return res
            

        