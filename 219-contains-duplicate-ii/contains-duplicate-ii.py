class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in seen : 
                if abs(i-seen[num])<=k:
                    return True
            seen[num] = i
        return False
        