class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)-1
        for i in range(1, n+1):
            if nums[i-1]!=i:
                print(i)
                return False
        
        if nums[-1]!=n:
            return False
        return True
        