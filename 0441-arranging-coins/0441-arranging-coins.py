class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        remCoins = n
        for i in range(1,n):
            remCoins = remCoins - i
            if remCoins==0:
                return i
            if remCoins <0:
                return i-1
        
        

            
        