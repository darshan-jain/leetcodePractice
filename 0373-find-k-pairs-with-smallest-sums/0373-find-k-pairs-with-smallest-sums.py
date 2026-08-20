import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minheap = []
        i = 0 
        j = 0 
        heapq.heappush(minheap, (nums1[i] + nums2[j], i,j))
        visit = set()
        visit.add((0,0))
        res = []

        while k>0:
            val, x,y = heapq.heappop(minheap)
            res.append([nums1[x],nums2[y]])
            if x+1<len(nums1) and (x+1,y) not in visit:
                visit.add((x+1,y))
                heapq.heappush(minheap, (nums1[x+1]+ nums2[y], x+1,y))
            if y+1<len(nums2) and (x,y+1) not in visit:
                visit.add((x,y+1))
                heapq.heappush(minheap, (nums1[x] + nums2[y+1], x, y+1))
            k-=1
        return res

        