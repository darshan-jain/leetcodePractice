class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)
        # return s==t
        
        #2nd Solution
        return Counter(s) == Counter(t)