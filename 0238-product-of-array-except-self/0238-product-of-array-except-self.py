class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        for i in range(len(nums)):
            if i==0:
                left.append(1)
            else:
                val = nums[i-1]*left[-1]
                left.append(val)
        right = []
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                right.append(1)
            else:
                val = nums[i+1]*right[-1]
                right.append(val)
        right = right[::-1]
        ans = []
        for i in range(len(nums)):
            ans.append(left[i]*right[i])
        return ans
        