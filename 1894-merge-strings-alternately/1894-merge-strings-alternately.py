class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        word3=""
        while i<len(word1) or j<len(word2):
            if i<len(word1):
                word3+=word1[i]
                i+=1
            if j<len(word2):
                word3+=word2[j]
                j+=1
        
        return word3
        