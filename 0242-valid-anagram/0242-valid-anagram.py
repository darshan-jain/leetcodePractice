class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms = {}
        hmt = {}

        for c in s:
            hms[c] = 1 + hms.get(c,0)
        
        for c in t:
            hmt[c] = 1 + hmt.get(c,0)
        
        for k,v in hms.items():
            if k not in hmt or hmt[k]!=v:
                return False 
        return True if len(hms)==len(hmt) else False
        