class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = minp = nums[0]
        max_product = maxp 
        for num in nums[1:]:
            temp = num*maxp
            maxp = max(num , num*maxp, num*minp)
            minp = min(num, temp , num*minp)
            max_product = max(max_product, maxp)
        return max_product
        