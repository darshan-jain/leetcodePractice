class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])
        r = N-1 
        c =0 
        while r>=0 and c<M:
            m = matrix[r][c]
            if m == target:
                return True
            elif m < target:
                c+=1
            else:
                r-=1
        return False

        