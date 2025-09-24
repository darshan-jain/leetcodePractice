import heapq
class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.large)> len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small , - val)
        if len(self.small) > len(self.large)+1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -val)
        

    def findMedian(self) -> float:
        if len(self.small)== len(self.large):
            return (-1*(self.small[0]) + self.large[0])/2
        else:
            if len(self.small) > len(self.large):
                return self.small[0]*-1
            else:
                return self.large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()