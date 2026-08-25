class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        nums.sort()
        for i,num in enumerate(nums):
            hm[num]=i 
        
        res = 0 
        for i,num in enumerate(nums):
            lastidx = hm[num+1] if num+1 in hm else -1 
            if lastidx!=-1:
                res = max(res, lastidx-i+1)
        return res
        