class Solution:
    def isPalindrome(self, s: str) -> bool:
        newlist = []
        for c in s:
            if c.isalnum():
                newlist.append(c.lower())
        l = 0 
        r = len(newlist)-1
        while l<=r:
            if newlist[l]!=newlist[r]:
                return False
            l+=1
            r-=1
        return True
        