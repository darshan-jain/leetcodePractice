class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowFlag = False
        colFlag = False
        rows, cols = len(matrix) , len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0 :
                    if row==0:
                        rowFlag = True
                    if col==0:
                        colFlag = True
                    else:
                        if row!=0 and col!=0:
                            matrix[row][0] =0  
                            matrix[0][col] = 0 
        
        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[0][col]==0 or matrix[row][0]==0:
                    matrix[row][col]=0
        
        if rowFlag:
            matrix[0] = [0]*cols
        
        if colFlag:
            for i in range(rows):
                matrix[i][0] = 0
        