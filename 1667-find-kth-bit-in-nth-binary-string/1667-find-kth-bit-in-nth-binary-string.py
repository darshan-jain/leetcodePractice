class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ic = 0 

        while n>1:
            length = (1<<n) -1
            mid = length//2 + 1

            if k ==mid:
                return "0" if ic%2==1 else "1"
            
            if k > mid:
                k = length-k+1
                ic+=1
            n-=1
        return "1" if ic%2==1 else "0"
            
        