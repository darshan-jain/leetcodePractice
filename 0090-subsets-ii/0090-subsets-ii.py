class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, part):
            res.append(part[:])
            if idx==len(nums):
                return 
            for i in range(idx,len(nums)):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                dfs(i+1, part+[nums[i]])


        dfs(0,[])
        return res
        