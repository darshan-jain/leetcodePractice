class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0 
        last = len(nums)-1

        for i in range(len(nums)):
            if i > right: 
                return False 
            if i + nums[i] > right:
                right = i + nums[i]
            if right >=last:
                return True
        