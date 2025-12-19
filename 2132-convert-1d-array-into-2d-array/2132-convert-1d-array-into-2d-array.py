class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n !=len(original):
            return []
        ptr = 0 
        res = []
        for i in range(m):
            newrow = []
            for j in range(n):
                newrow.append(original[ptr])
                ptr+=1
            res.append(newrow)
        return res


        