class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                totalSum = nums[i]+ nums[l]+nums[r]
                if totalSum > 0:
                    r=r-1
                elif totalSum < 0 : 
                    l = l+1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l]==nums[l-1]:
                        l+=1
        return res
        