class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       val = set()
       for num in nums:
        if num in val:
            return num
        val.add(num)