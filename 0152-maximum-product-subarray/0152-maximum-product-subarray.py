class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        leftProd = 1 
        rightProd = 1
        ans = nums[0]
        for i in range(len(nums)):
            leftProd = leftProd if leftProd!=0 else 1 
            rightProd = rightProd if rightProd!=0 else 1 
            leftProd *= nums[i]
            rightProd*=nums[n-i-1]
            ans = max(ans, leftProd, rightProd)
        return ans
        