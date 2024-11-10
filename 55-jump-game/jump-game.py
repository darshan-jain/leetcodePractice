class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Recursive Solution - O(max(nums)^n)
        # n = len(nums)
        # def can_reach(i):
        #     if i==n-1:
        #         return True
            
        #     for jump in range(1,nums[i]+1):
        #         if can_reach(i+jump):
        #             return True
                
        #     return False 

        # return can_reach(0)

        # Dynamic Programming Approach also exceeds time limit 

        #greedy appraoch 
        n = len(nums)
        target = n-1
        for i in range(n-1,-1,-1):
            maxjump = nums[i]
            if i + maxjump>= target:
                target = i
            
        return target ==0 