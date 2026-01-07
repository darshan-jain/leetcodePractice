class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #full prefix matrix
        self.prefix = []
        
        #construct each row
        for i in range(len(matrix)):
            row = []
            val = 0 
            for j in range(len(matrix[0])):
                val+=matrix[i][j]
                row.append(val)
            self.prefix.append(row)
        print(self.prefix)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        val = 0 
        for i in range(row1,row2+1):
            rowval = self.prefix[i][col2] - self.prefix[i][col1-1] if col1-1>=0 else self.prefix[i][col2]
            val+=rowval
        return val
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)