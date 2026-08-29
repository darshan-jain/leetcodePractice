class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
       
        hm = defaultdict(list)
        for i, num in enumerate(nums):
            hm[num].append(i)
        res = []
        for q in queries:
            num = nums[q]
            lst = hm[num]
            localres = float("inf")
            idx = None 
            # for i,val in enumerate(lst):
            #     if val==q:
            #         idx=i
            #         break
            l = 0 
            r = len(lst)-1
            while l<=r:
                m = (l+r)//2
                if lst[m]==q:
                    idx = m
                    break
                elif lst[m] > q:
                    r = m-1
                else:
                    l = m+1
            a = lst[(idx+1)%len(lst)]
            b = lst[(idx-1)%len(lst)]
            c = lst[idx]
            localres = min(abs(b-c), abs(c-a), abs(n - abs(a-c)), abs(n-abs(b-c)))
            if localres!=0:
                res.append(localres)
            else:
                res.append(-1)
        return res
        