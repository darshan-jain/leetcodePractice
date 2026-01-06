class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        bag = set()
        for num in nums:
            if num in bag:
                return True 
            bag.add(num)
        return False
        