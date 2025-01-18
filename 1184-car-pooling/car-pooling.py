class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        #O(n)

        arr = [0] * 1001
        for t in trips:
            numPass,start,end = t
            arr[start]+=numPass
            arr[end]-=numPass
        curPass =0 
        for i in range(len(arr)):
            curPass+=arr[i]
            if curPass > capacity:
                return False
        return True


        #O(nlogn Approach)
        #trips - [numPass, start,end]
        # trips.sort(key = lambda t:t[1])
        # minHeap = []  # [end, numPass]
        # curPass = 0 
        # for t in trips:
        #     numPass, start,end = t
        #     while minHeap and minHeap[0][0] <= start:
        #         curPass-=minHeap[0][1]
        #         heapq.heappop(minHeap)


        #     curPass+=numPass
        #     if curPass > capacity:
        #         return False
        #     heapq.heappush(minHeap, [end,numPass])
        # return True