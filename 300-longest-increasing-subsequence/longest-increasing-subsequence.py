class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # lst = [nums[0]]
        # max_len = 1
        # for num in nums[1:]:
        #     if num > lst[-1]:
        #         lst.append(num)
        #         max_len+=1
        #     else:
        #         ind = 0 
        #         while ind < len(nums) and lst[ind] < num:
        #             ind+=1
        #         lst[ind] = num
        # return max_len

        #Dynamic Programming Soln 

        LIS = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1+LIS[j])        
        return max(LIS)