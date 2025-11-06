class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1
        output = []
        for i in range(n):
            product*=nums[i]
            output.append(product)
        
        product = 1
        for i in range(n-1,0,-1):
            output[i] = output[i-1]*product
            product*=nums[i]
        output[0] = product
        return output
        