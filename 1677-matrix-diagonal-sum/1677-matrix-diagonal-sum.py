class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        pos = set()
        res = 0 
        for i in range(len(mat)):
            res+=mat[i][i]
            pos.add((i,i))
            if (i,(len(mat)-1)-i) not in pos:
                res+=mat[i][(len(mat)-1)-i]
        return res
        
        