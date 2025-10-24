class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms = {}
        hmt = {}

        for c in s:
            hms[c] = 1 + hms.get(c,0)
        
        for c in t:
            hmt[c] = 1+hmt.get(c,0)
        
        if len(hmt)!=len(hms):
            return False

        for c in s:
            k,v = c,hms[c]
            if k not in hmt or hmt[c]!=hms[c]:
                return False
        
        return True
        