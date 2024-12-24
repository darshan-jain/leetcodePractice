class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        words = s.split()
        if len(pattern)!= len(words):
            return False

        d = {}
        seen = set()
      

        for i, char in enumerate(pattern):
            if char not in d:
                if words[i] in seen:
                    return False
                d[char] = words[i]
                seen.add(words[i])
            else:
                if d[char] != words[i]:
                    return False

        return True





