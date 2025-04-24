class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        part = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n]+=1
        
        def backtrack():
            if len(part)==len(nums):
                res.append(part.copy())
                return 
            for n in count:
                if count[n]>0:
                    part.append(n)
                    count[n]-=1
                    backtrack()
                    part.pop()
                    count[n]+=1
            
        
        backtrack()
        return res
        