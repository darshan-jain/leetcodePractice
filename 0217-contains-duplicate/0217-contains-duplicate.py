class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        for num in nums:
            if num not in vals:
                vals.add(num)
            else:
                return True
        return False
