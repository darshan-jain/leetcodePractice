class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]
        for i in range(len(nums)-1,0,-1):
            output.append(output[-1]* nums[i])
        output = output[::-1]
        left = 1
        for i in range(len(nums)):
            output[i] = output[i]*left
            left = left* nums[i]
        return output