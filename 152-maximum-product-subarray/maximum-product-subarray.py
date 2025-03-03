class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = minp = nums[0]
        max_product = maxp 
        for num in nums[1:]:
            temp = maxp*num
            maxp = max(num, num*minp, num*maxp)        
            minp = min(num, num*minp, temp)
            max_product = max(max_product, maxp)
        return max_product