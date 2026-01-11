class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = [0]*26
        dic2 = [0]*26 
        s1Len = len(s1)
        s2Len = len(s2)
        r = 0 
        l = 0 
        if s1Len > s2Len:
            return False 
        while r < s1Len:
            dic1[ord(s1[r]) - ord('a')]+=1
            dic2[ord(s2[r]) - ord('a')]+=1
            r+=1
        r-=1
        while r < s2Len:
            if dic1==dic2:
                return True
            r+=1
            if r < s2Len:
                dic2[ord(s2[r]) - ord('a')]+=1
            dic2[ord(s2[l]) - ord('a')]-=1
            l+=1
        return False

        