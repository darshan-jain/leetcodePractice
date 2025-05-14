class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hms = Counter(s)
        hmt = Counter(t)
        res=""
        for k,v in hmt.items():
            if k in hms:
                if hms[k]!=v:
                    res+=k
            else:
                res+=k
        return res
        