class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        leftprod = 1 
        rightprod = 1 
        ans = nums[0]
        for i in range(len(nums)):
            leftprod = leftprod if leftprod != 0 else 1 
            rightprod = rightprod if rightprod!=0 else 1 
            leftprod *= nums[i]
            rightprod *= nums[n-i-1]
            ans = max(ans, leftprod, rightprod)
        return ans
        