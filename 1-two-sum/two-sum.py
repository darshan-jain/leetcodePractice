class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for ind in range(len(nums)):
            num = nums[ind]
            if target-num  in seen:
                return [ind, seen[target-num]]
            seen[num] = ind