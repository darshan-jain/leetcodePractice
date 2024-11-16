class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        words = s.split()
        revwords = words[::-1]
        return " ".join(revwords)