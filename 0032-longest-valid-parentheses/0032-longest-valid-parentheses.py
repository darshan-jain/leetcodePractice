class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = 0 
        r = 0 
        m = 0 
        for c in s:
            if c =='(':
                l+=1
            else:
                r+=1
            if l==r:
                m = max(m, l*2)
            elif r>l:
                r=0
                l=0
        l =0 
        r =0 
        for c in s[::-1]:
            if c =='(':
                l+=1
            else:
                r+=1
            if l==r:
                m = max(m, l*2)
            elif l>r:
                r=0
                l=0
        return m

        