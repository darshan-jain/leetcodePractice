class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a= list(s)
        b = list(t)

        if len(s)!=len(t):
            return false
        
        d = {}
        seen = set()

        for i, char in enumerate(a):
            if char not in d:
                if b[i] in seen:
                    return False
                d[char] = b[i]
                seen.add(b[i])
            else:
                if d[a[i]] != b[i]:
                    return False
        return True
        