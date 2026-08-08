class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        val = [0]*26
        val2 = [0]*26
        for c in magazine:
            idx = ord(c) - ord('a')
            val[idx]+=1
        for c in ransomNote:
            idx = ord(c) - ord('a')
            val2[idx]+=1
        
        for i,v in enumerate(val2):
            if v > val[i]:
                return False
        return True

        