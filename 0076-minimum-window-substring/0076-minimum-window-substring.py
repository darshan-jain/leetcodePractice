class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        c = Counter(t)
        overall = len(c)
        l=r=0 
        while r < len(s):
            if s[r] in c:
                c[s[r]]-=1
                if c[s[r]]==0:
                    overall-=1
            while overall==0:
                if not res:
                    res = s[l:r+1]
                elif len(res)>(r-l+1):
                    res = s[l:r+1]
                if s[l] in c:
                    c[s[l]]+=1
                    if c[s[l]]>0:
                        overall+=1
                l+=1
            r+=1
        return res
            

        