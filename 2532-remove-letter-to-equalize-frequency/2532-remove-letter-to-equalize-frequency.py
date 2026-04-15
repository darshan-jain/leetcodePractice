class Solution:
    def equalFrequency(self, word: str) -> bool:
        hm = [0]*26
        for c in word:
            index = ord(c) - ord('a')
            hm[index]+=1
        for i in range(26):
            hm[i]-=1
            test_val = max(hm)
            res = True
            for j in range(26):
                if hm[j]==0:
                    continue
                if hm[j]!=test_val:
                    res = False
                    break
            if res == True:
                return True
            hm[i]+=1
        return False
            
                