class Solution:
    def binaryGap(self, n: int) -> int:
        binval = str(bin(n)[2:])
        res = 0 
        for i in range(len(binval)):
            if binval[i]=="1":
                j = i+1
                while j<len(binval) and binval[j]=="0":
                    j+=1
                if j< len(binval) and binval[j]=="1":
                    idxval = j-i
                    res = max(res, idxval)
        return res
        