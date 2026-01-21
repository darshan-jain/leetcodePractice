class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0 
        minn = min (n,limit)

        for i in range(minn+1):
            for j in range(minn+1):
                t=n-i-j
                if t>=0 and t<=limit:
                    res+=1
        return res
