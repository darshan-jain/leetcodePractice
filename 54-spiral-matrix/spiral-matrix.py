class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_row =0 
        min_col =0 
        max_row = len(matrix)
        max_col = len(matrix[0])
        output = []
        row = 0 
        while min_row<max_row and min_col < max_col:
            for col in range(min_col,max_col):
                output.append(matrix[row][col])
            min_row+=1

            for row  in range(min_row,max_row):
                output.append(matrix[row][col])
            max_col-=1

            if min_row<max_row and min_col < max_col:
                for col in range(max_col-1,min_col-1,-1):
                    output.append(matrix[row][col])
                max_row-=1

                for row in range(max_row-1,min_row-1,-1):
                    output.append(matrix[row][col])
                min_col+=1
        return output
        