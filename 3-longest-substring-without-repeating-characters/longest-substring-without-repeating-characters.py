class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = -1
        ans = 0 
        lastseen = {}
        for i,c in enumerate(s):
            j = max(j, lastseen.get(c,-1))
            ans = max(ans,i-j)
            lastseen[c] = i
        return ans
        