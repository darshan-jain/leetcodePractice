class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowflag = colflag = False
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    if row ==0:
                        rowflag = True
                    if col ==0:
                        colflag = True
                    elif row!=0 and col!=0:
                        matrix[row][0] = 0
                        matrix[0][col] = 0 
        
        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[row][0] ==0 or matrix[0][col] ==0:
                    matrix[row][col] = 0 
        if rowflag:
            matrix[0] = [0]*cols
        if colflag:
            for row in range(rows):
                matrix[row][0] = 0
        