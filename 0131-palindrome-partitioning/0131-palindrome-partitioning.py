class Solution:
    def isPali(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r = l+1,r-1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(i):
            if i>=len(s):
                res.append(part.copy())
                return 
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        
        backtrack(0)
        return res
        