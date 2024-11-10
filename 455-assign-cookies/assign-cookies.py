class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0 
        g.sort()
        s.sort()
        sptr = len(s)-1
        gptr = len(g)-1

        while sptr >=0 and gptr>=0:
            if s[sptr] >= g[gptr]:
                count +=1
                sptr-=1
                gptr-=1
            else:
                gptr-=1
        return count