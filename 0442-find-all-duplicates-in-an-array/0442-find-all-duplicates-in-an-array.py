class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            pos = abs(nums[i])-1
            if nums[pos]<0:
                res.append(abs(nums[i]))
            nums[pos]*=-1
        return res
        