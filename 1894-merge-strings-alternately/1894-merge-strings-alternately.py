class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0 
        q = 0 
        ans = ""
        while p<len(word1) and q < len(word2):
            ans+=word1[p]
            ans+=word2[q]
            p+=1
            q+=1
        
        while p<len(word1):
            ans+=word1[p]
            p+=1
        
        while q<len(word2):
            ans+=word2[q]
            q+=1
        return ans

        