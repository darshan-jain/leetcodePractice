class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_p = min_p = nums[0]
        max_product = max_p
        for num in nums[1:]:
            temp = min_p
            min_p = min(num,num*min_p,num*max_p)
            max_p = max(num,num*temp,num*max_p)
            max_product = max(max_p,max_product)
        return max_product
        