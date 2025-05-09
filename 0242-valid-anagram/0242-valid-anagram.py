class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms = {}
        hmt = {}
        if len(t) > len(s):
            s,t = t,s
        for char in s:
            hms[char] = 1 + hms.get(char,0)
        
        for char in t:
            hmt[char] = 1+hmt.get(char,0)
        
        for key,val in hms.items():
            if key not in hmt or val != hmt[key]:
                return False
        return True
        