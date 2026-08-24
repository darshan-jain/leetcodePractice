class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows = len(mat)
        cols = len(mat[0])
        k%=cols 

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]!=mat[i][(j+k)%cols]:
                    return False 
        return True
        