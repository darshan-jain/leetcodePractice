class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        majority = 0 
        l = 0 
        r = 0 
        ans = 0 
        while r < len(s):
            hm[s[r]] = 1 + hm.get(s[r],0)
            majority = max(majority, hm[s[r]])
            while r-l+1 > majority+k:
                hm[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
            r+=1
        return ans
        
        