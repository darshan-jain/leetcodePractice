import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        currmax = float("-inf")
        for i in range(len(nums)):
            val = nums[i][0]
            heapq.heappush(heap, (val,i,0))
            currmax  = max(currmax, val)
        bleft,bright = float("-inf"), float("inf")

        while heap:
            val, listidx,elemidx = heapq.heappop(heap)
            if currmax - val < bright - bleft:
                bleft,bright = val, currmax 
            if elemidx+1>=len(nums[listidx]):
                break
            nextval = nums[listidx][elemidx+1]
            heapq.heappush(heap, (nextval, listidx, elemidx+1))
            currmax = max(currmax, nextval)
        return [bleft,bright]
        