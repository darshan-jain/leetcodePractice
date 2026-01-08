class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = ""
        for c in s:
            if c.isalnum():
                letters += c.lower()
        
        l = 0 
        r = len(letters)-1
        while l<=r:
            if letters[l]!=letters[r]:
                return False 
            l+=1
            r-=1
        return True
        