class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #base case
        if sum(nums)%2:  #sum is odd , cannot be partitioned
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for t in dp:
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp = nextDP
        
        return True if target in dp else False
        