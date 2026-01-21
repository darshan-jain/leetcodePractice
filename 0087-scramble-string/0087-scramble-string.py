class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        hm = {}
        def solve(s1,s2):
            if len(s1)==1:
                return s1==s2
            if s1==s2:
                return True
            key = s1+s2
            if key in hm:
                return hm[key]
            if Counter(s1)!=Counter(s2):
                hm[key] = False
                return hm[key]
            n = len(s1)
            
            for i in range(1,len(s1)):
                if (solve(s1[:i],s2[:i]) and solve(s1[i:],s2[i:])) or (solve(s1[:i], s2[n-i:]) and solve(s1[i:],s2[:n-i])):
                    hm[key] = True
                    return hm[key]
            hm[key] = False
            return hm[key]
        n = len(s1)
        return solve(s1,s2)
        