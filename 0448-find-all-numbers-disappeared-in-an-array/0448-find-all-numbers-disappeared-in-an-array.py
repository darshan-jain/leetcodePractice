class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i,num in enumerate(nums):
            pos = abs(num)-1
            if nums[pos]>0:
                nums[pos]*=-1
        
        for i in range(n):
            if nums[i]>0:
                res.append(i+1)
        
        if res:
            return res
        return []
        