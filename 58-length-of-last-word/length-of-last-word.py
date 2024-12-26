class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # words = s.split()

        # last = words[-1]

        # return len(last)
        
        length =0 
        i = len(s)-1
        while i>=0 and s[i] == " ":
            i-=1
        while i>=0 and s[i] != " ":
            i-=1
            length+=1
        return length