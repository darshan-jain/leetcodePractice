class Solution:
    def isSubstringPresent(self, s: str) -> bool:

        # def reverse(s):
        #     l = 0 
        #     r = len(s)-1
        #     while l<=r:
        #         s[l],s[r] = s[r],s[l]
        #         l+=1
        #         r-=1
        #     return s
        
        rev = s[::-1]

        for i in range(0,len(s)-1):
            w = s[i:i+2]
            if w in rev:
                return True
        return False

        