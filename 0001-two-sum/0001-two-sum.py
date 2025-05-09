class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        res = []
        for i in range(0,len(nums)):
            num = nums[i]
            if target - num in hm:
                return [i,hm[target-num]]
            hm[num] = i 
        return [-1,-1]
        