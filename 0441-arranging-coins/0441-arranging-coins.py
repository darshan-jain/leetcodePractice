class Solution:
    def arrangeCoins(self, n: int) -> int:
        # if n==1 or n==2:
        #     return 1
        # remCoins = n
        # for i in range(1,n):
        #     remCoins = remCoins - i
        #     if remCoins==0:
        #         return i
        #     if remCoins <0:
        #         return i-1

        l,r = 1, n 
        res = 0 
        while l <=r:
            mid = (l+r)//2
            coins = (mid/2) * (mid+1)
            if coins > n:
                r = mid-1
            else:
                l = mid+1
                res = max(res,mid)
        return res
        

            
        