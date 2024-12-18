class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            if i==1:
                nums[i] = max(nums[i],nums[i-1])
            else:
                nums[i]=max(nums[i-2]+nums[i], nums[i-1])
        return nums[-1]
        