class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res1 = []
        for char in s:
            if char == "#":
                if len(res1)==0:
                    continue
                res1.pop()
            else:
                res1.append(char)
        res2 = []
        for char in t:
            if char == "#":
                if len(res2)==0:
                    continue
                res2.pop()
            else:
                res2.append(char)
        
        return (res1==res2)
