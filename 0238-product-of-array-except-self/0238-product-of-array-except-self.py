class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rightProd = []
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                rightProd.append(1)
            else:
                rightProd.append(rightProd[-1]* nums[i+1])
        rightProd = rightProd[::-1]
        leftProd = []
        for i in range(0,len(nums)):
            if i==0:
                leftProd.append(1)
            else:
                leftProd.append(leftProd[-1]* nums[i-1])
        res = []
        for i in range(0,len(nums)):
            res.append(leftProd[i]* rightProd[i])
        return res
        