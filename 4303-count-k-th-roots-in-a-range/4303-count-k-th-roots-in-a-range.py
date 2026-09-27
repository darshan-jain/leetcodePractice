class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k==1:
            return r-l+1
        num = 0
        cnt = 0 
        while True:
            if l<=num**k <= r:
                num+=1
                cnt+=1
            elif num**k <l:
                num+=1
            else:
                break
        return cnt

        