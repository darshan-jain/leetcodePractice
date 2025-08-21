class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0 
        i=0
        j=0
        while j < len(s) and i < len(g):
            if s[j]>=g[i]:
                j+=1
                i+=1
                ans+=1
            else:
                j+=1
        return ans
        