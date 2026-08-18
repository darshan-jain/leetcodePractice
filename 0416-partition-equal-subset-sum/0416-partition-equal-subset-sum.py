class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        total = sum(nums)
        target = total//2
        if total%2!=0:
            return False 
        for num in nums:
            next_level = set()
            for items in dp:
                next_level.add(items)
                next_level.add(items+num)
            dp = next_level
            if target in dp:
                return True
        return False
        