class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        right = 0 
        curr_val = 0 
        minlen = 0

        #edge cases
        if sum(nums) < target:
            return 0 
        if len(nums)==0 or target==0:
            return 0 
        
        while right<len(nums):
            curr_val+=nums[right]
            right+=1
            if curr_val>=target:
                minlen = (right-left)
                break
        
        while right<=len(nums):
            while curr_val>=target:
                curr_val = curr_val-nums[left]
                left+=1
                if curr_val>=target:
                    minlen =min(minlen, right-left)
            if right<len(nums):
                curr_val+=nums[right]
            right+=1
        return minlen
            
        
        

        