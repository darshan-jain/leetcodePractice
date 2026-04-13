class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r 

        def canSplit(val):
            subarray = 1 
            w = 0 
            for i in nums:
                w+=i
                if w > val:
                    subarray+=1
                    w=i
                
            return subarray<=k

        while l<=r:
            m = (l+r)//2
            if canSplit(m):
                res = min(res, m)
                r = m-1
            else:
                l=m+1
        return res
        