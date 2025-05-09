class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s ==" ":
            return True
        s = list(s)
        t = []
        for char in s:
            if char.isalnum():
                t.append(char.lower())
        l = 0
        r = len(t)-1
        while l<=r:
            if t[l]!=t[r]:
                return False
            l +=1
            r-=1
        return True


        