class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = []
        right = []
        for i in range(len(nums)):
            if i==0:
                left.append(1)
            else:
                val = left[-1]*nums[i-1]
                left.append(val)
        
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                right.append(1)
            else:
                val= right[-1]* nums[i+1]
                right.append(val)
        right.reverse()

        for i in range(len(left)):
            res.append(left[i]*right[i])
        return res
        