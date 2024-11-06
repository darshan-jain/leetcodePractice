class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = 0
        for num in nums:
            seen[num] += 1
            if seen[num] >= 2:
                return True
            

        return False