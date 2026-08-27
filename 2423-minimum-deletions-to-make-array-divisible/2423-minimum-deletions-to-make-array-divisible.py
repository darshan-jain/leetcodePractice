class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        cnt = Counter(nums)
        minheap = []

        def divisible(num):
            seen = set()
            for val in numsDivide:
                if val in seen:
                    continue
                if val%num!=0:
                    return False
                seen.add(val)
            return True

        for k,v in cnt.items():
            heapq.heappush(minheap, (k,v))
        ans = 0 
        
        numsDivide.sort(reverse = True)


        while minheap:
            num, freq = heapq.heappop(minheap)
            print(freq)
            if divisible(num):
                return ans
            else:
                ans+=freq
        return -1
        