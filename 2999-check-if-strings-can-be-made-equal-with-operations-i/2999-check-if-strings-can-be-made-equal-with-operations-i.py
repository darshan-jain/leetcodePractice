class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        i = 0 
        j = 0 
        s1 = list(s1)
        s2 = list(s2)
        while i<len(s1):
            if s1[i]==s2[j]:
                i+=1
                j+=1
            elif j+2<len(s2) and  s1[i]==s2[j+2]:
                s2[j],s2[j+2]=s2[j+2],s2[j]
                i+=1
                j+=1
            else:
                return False
        if i==len(s1) and j==len(s2):
            return True
        return False
        