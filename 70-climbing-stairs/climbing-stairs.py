class Solution:
    def helper(self,n,memo={}):
        if n in memo:
            return memo[n]
        if n == 0 :
            return 1
        if n < 0 :
            return 0 
        left = self.helper(n-1)
        right = self.helper(n-2)
        memo[n] = val = left+right
        return val
    def climbStairs(self, n: int) -> int:
        return self.helper(n)
        