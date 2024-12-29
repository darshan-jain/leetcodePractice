class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = (n*(n+1))/2
        sum = int(sum)
        arrsum = 0 
        for num in nums:
            arrsum+=num
        return sum-arrsum
        