class Solution:
    def firstUniqChar(self, s: str) -> int:
        adjlst = defaultdict(list)
        for i,c in enumerate(s):
            adjlst[c].append(i)
        ans = float("inf")
        for k,v in adjlst.items():
            if len(v)>1:
                continue
            else:
                ans = min(ans, v[0])
        return ans if ans!= float("inf") else -1
        