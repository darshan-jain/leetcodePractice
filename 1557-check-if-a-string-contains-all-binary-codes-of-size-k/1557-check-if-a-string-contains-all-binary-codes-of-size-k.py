class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        vals = set()
        for i in range(len(s)-k+1):
            word = s[i:i+k]
            if word not in vals:
                vals.add(word)
        

        for i in range(2**k-1,-1,-1):
            binval = str(bin(i)[2:])
            if len(binval)<k:
                binval = "0"*(k-len(binval)) + binval
            print(binval)
            if binval not in vals:
                return False 
        return True

        