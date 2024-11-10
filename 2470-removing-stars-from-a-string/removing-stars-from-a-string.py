class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = list(s)
        res = []
        for letter in word:
            if letter == "*":
                res.pop()
            else:
                res.append(letter)
        return "".join(res)
        