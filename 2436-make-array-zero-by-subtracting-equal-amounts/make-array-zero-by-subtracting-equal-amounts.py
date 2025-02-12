class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # if len(nums)==1 and nums[0] ==0:
        #     return 0
        # time =0
        # while sum(nums)!= 0:
        #     copy = [ele for ele in nums if ele!=0]
        #     x = min(copy)            
        #     for i in range(len(nums)):
        #         if nums[i]!=0:
        #             nums[i]-=x
        #     time+=1
        #     print(nums)
        # return time

        unique_set = {number for number in nums if number!=0}
        return len(unique_set)