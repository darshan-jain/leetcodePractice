class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        
        i=0
        d=1
        rows = [[] for _ in range(numRows)]
        for c in s:
            rows[i].append(c)
            if i==0:
                d=1
            elif i==numRows-1:
                d = -1
            i+=d
        
        result = ""
        for i in range(numRows):
            result+=''.join(rows[i])
        return result
        
        