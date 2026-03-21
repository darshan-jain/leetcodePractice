class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1]
        for i in range(1,len(nums)):
            left.append(left[-1]*nums[i-1])
        #print(left)
        right = [1]
        for i in range(len(nums)-2,-1,-1):
            right.append(right[-1]*nums[i+1])
        right = right[::-1]
        res = []
        for i in range(len(left)):
            res.append(left[i]*right[i])
        return res

        