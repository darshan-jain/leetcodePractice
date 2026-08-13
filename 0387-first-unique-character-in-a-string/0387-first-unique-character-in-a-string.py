class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = defaultdict(list)
        for i,c in enumerate(s):
            hm[c].append(i)
        ans= float("inf")
        for k,v in hm.items():
            if len(v)>1:
                continue
            ans = min(ans, v[0])
        return ans if ans!=float("inf") else -1
        