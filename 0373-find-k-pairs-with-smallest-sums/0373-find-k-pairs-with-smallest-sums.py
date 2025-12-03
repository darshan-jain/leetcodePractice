import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minheap = []
        res = []
        i=0 
        j=0
        visit = set()
        heapq.heappush(minheap, (nums1[0]+nums2[0],i,j))
        visit.add((0,0))

        while k>0:
            val,index1, index2 = heapq.heappop(minheap)
            res.append([nums1[index1], nums2[index2]])
            if index1+1<len(nums1) and (index1+1,index2) not in visit:
                heapq.heappush(minheap, (nums1[index1+1]+nums2[index2], index1+1,index2 ))
                visit.add((index1+1,index2))
            if index2+1<len(nums2) and (index1, index2+1) not in visit:
                heapq.heappush(minheap, (nums1[index1]+nums2[index2+1], index1, index2+1))
                visit.add((index1,index2+1))
            k-=1
        return res
        
