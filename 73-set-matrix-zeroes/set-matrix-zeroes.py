class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        isRowZero = False
        isColZero = False

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

                    if i==0:
                        isRowZero = True
                    if j==0:
                        isColZero = True
        
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[i])-1,-1,-1):
                if matrix[i][0] ==0 :
                    if i!=0 or isRowZero:
                        matrix[i][j] = 0
                if matrix[0][j] ==0:
                    if j!=0 or isColZero:
                        matrix[i][j] = 0 

        