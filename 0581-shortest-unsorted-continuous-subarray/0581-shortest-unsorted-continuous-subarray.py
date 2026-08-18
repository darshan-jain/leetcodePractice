class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        idx1=-1
        new = [num for num in nums]
        new.sort()
        for i in range(len(nums)):
            if nums[i]!=new[i]:
                idx1=i
                break
        
        idx2=len(nums)
        for i in range(len(nums)-1,-1,-1):
           
            if nums[i]!=new[i]:
              
                idx2=i
                break
      
        res = idx2-idx1+1
        if res > len(nums):
            return 0 
        return res
        