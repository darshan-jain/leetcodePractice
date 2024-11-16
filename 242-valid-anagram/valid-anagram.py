class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #return Counter(s) == Counter(t)

        s_counts = Counter(s)
        for char in t:
            if char not in s_counts:
                return False
            s_counts[char]-=1
            if s_counts[char] ==0:
                del s_counts[char]
        return len(s_counts)==0