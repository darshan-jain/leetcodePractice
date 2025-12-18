class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # res = []
        # def backtrack(p,currSum, target):
        #     if currSum==target:
        #         res.append(p[:])
        #         return 
        #     for i in range(n):
        #         if currSum + nums[i]>target:
        #             continue
        #         backtrack(p+[nums[i]], currSum + nums[i], target)
        
        # backtrack([],0,target)
        # return len(res)
        
        res = [0]*(target+1)
        res[0] = 1
        for i in range(target+1):
            for num in nums:
                if i>=num:
                    res[i]+=res[i-num]
        return res[-1]