class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0 
        j = -1
        lastseen = {}
        for i,c in enumerate(s):
            j = max(j , lastseen.get(c,-1))
            ans = max(ans, i - j)
            lastseen[c] = i
        return ans


        