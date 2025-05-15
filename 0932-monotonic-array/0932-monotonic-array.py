class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = False 
        isDecreasing = False 
        if len(nums)==1:
            return True

        if nums[0]<=nums[-1]:
            for i in range(len(nums)-1):
                if nums[i]<=nums[i+1]:
                    isIncreasing =True
                    continue
                else:
                    isIncreasing = False
                    break
            return isIncreasing
        
        if nums[0]>=nums[-1]:
            for i in range(len(nums)-1):
                if nums[i]>=nums[i+1]:
                    isDecreasing = True
                    continue
                else:
                    isDecreasing = False
                    break
            return isDecreasing


        #check increasing
        
        
        