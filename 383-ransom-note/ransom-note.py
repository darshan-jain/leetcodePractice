from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # dr = defaultdict(list)
        # dm = defaultdict(list)
        # letters = list(ransomNote)
        # for char in letters:
        #     dr[char] = 0 
        # for char in letters:
        #     dr[char] +=1
        
        # lettersmaga = list(magazine)
        # for char in lettersmaga:
        #     dm[char] =0
        # for char in lettersmaga:
        #     dm[char] +=1
        
        # for key,value in dr.items():
        #     if key not in dm or value>dm[key]:
        #         return False
        # return True

        d = defaultdict(list)
        for char in magazine:
            d[char] =0
        for char in magazine:
            d[char] += 1
        for char in ransomNote:
            if char not in d or d[char] <= 0 :
                return False
            d[char] -=1
        return True
        