class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0 
        for i in range(len(s)-1):
            a = s[i]
            b = s[i+1]
            res+=abs(ord(a)-ord(b))
        return res
        