class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        vals = set()
        for i in range(len(s)-k+1):
            word = s[i:i+k]
            if word not in vals:
                vals.add(word)
        

        if len(vals)==2**k:
            return True
        return False

        