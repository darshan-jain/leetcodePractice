class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_row = 0 
        min_col = 0 
        max_row = len(matrix)
        max_col = len(matrix[0])
        res = []
        row = 0 
        while min_row<max_row and min_col < max_col:
            for col in range(min_col, max_col):
                res.append(matrix[row][col])
            min_row+=1

            for row in range(min_row,max_row):
                res.append(matrix[row][col])
            max_col-=1

            if min_row<max_row and min_col < max_col:
                for col in range(max_col-1,min_col-1,-1):
                    res.append(matrix[row][col])
                max_row-=1

                for row in range(max_row-1,min_row-1,-1):
                    res.append(matrix[row][col])
                min_col+=1
        
        return res
        