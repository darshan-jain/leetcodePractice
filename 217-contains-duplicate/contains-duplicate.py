class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Hashmap Approach
        # seen = {}
        # for i in range(len(nums)):
        #     seen[nums[i]] = 0
        # for num in nums:
        #     seen[num] += 1
        #     if seen[num] >= 2:
        #         return True
            

        # return False

        # set data structure approach 
        setnums = set()
        for num in nums:
            if num in setnums:
                return True
            setnums.add(num)
        return False