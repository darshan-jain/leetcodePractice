class Solution:
    def __init__(self):
        self.cache={}
    def climbStairs(self, n: int) -> int:

        #base cases 
        # n= 0 -> 1 way 
        # n = 1 -> 1 way 
        # n = 2 - > 2 ways 1+1 or 2
        # recursive tree 
        # n=4 
        # you can come to 3 or 2 from 4
        # you can come to 1 or 2 from 2 and 1 or 0 from 2
        if n==0 or n==1:
            return 1
        if n==2:
            return 2
        if n in self.cache:
            return self.cache[n]
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = res
        return res

        
        