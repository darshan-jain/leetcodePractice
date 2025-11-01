class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowFlag = 0 
        colFlag = 0 
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    if row==0:
                        rowFlag = 1
                    if col==0:
                        colFlag = 1
                    else:
                        
                        matrix[row][0]=0
                        matrix[0][col]=0
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if rowFlag:
            for i in range(cols):
                matrix[0][i]=0
        
        if colFlag:
            for i in range(rows):
                matrix[i][0]=0


                    
        