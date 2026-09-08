import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num: int) -> None:
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap,-num)
        else:
            heapq.heappush(self.minheap, num)
        
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        if len(self.maxheap) > len(self.minheap)+1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
         
        

    def findMedian(self) -> float:
        le = len(self.minheap) + len(self.maxheap)
        
        if le%2==0:
            v1 = self.minheap[0]
            v2 = -self.maxheap[0]
            return (v1+v2)/2
        else:
            return -self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()