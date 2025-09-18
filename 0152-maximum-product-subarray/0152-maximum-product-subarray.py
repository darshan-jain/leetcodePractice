class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = minp = nums[0]
        max_product = maxp
        for num in nums[1:]:
            temp = maxp*num
            print(temp)
            maxp = max(num, num*maxp,num*minp)
            print(maxp)
            minp = min(num, temp, num*minp)
            print(minp)
            max_product = max(max_product, maxp)
        return max_product

        