class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = [0] * 26      
        dic2 = [0]*26
        s1Len = len(s1)
        s2Len = len(s2)
        if s1Len > s2Len:
            return False 
        left = 0
        right = 0 
        while right<s1Len:
            dic1[ord(s1[right]) - ord('a')]+=1
            dic2[ord(s2[right]) - ord('a')]+=1
            right+=1
        
        right-=1
        while right<s2Len:
            if dic1==dic2:
                return True
            right+=1
            if right!=s2Len:
                dic2[ord(s2[right]) - ord('a')]+=1
            dic2[ord(s2[left]) - ord('a')]-=1
            left+=1
        return False
            



       