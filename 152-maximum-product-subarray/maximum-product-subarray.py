class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minp = maxp=  nums[0]
        maxproduct = maxp
        for num in nums[1:]:
            temp = minp
            minp = min(num,num*minp,num*maxp)
            maxp = max(num,num*temp,num*maxp)
            maxproduct = max(maxproduct, maxp)
        return maxproduct