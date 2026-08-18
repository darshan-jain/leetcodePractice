class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        val = 0 
        for i in range(0,len(nums), 2):
            val+=nums[i]
        return val