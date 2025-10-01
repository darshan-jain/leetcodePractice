class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0 
        for item in nums:
            num^=item
        return num
        