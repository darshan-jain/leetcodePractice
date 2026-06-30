class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0 
        r = 0 
        c = Counter(t)
        overall = len(c)
        res = ""
        while r<len(s):
            if s[r] in c:
                c[s[r]]-=1
                if c[s[r]]==0:
                    overall-=1
                while overall==0:
                    if not res or len(res) > (r-l+1):
                        res = s[l:r+1]
                    if s[l] in c:
                        c[s[l]]+=1
                        if c[s[l]]>0:
                            overall+=1
                    l+=1
            r+=1
        return res
        