class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binxstr = str(bin(x)[2:])
        binystr = str(bin(y)[2:])
        binxstr = "0" * (32 - len(binxstr)) + binxstr
        binystr = "0" * (32 - len(binystr)) + binystr
        cnt = 0 
        for i in range(32):
            if binxstr[i]!=binystr[i]:
                cnt+=1
        return cnt
        