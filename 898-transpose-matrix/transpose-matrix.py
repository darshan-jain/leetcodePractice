class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        op = [[0]*rows for i in range(cols)]
        for row in range(rows):
            for col in range(cols):
                op[col][row] = matrix[row][col]
        return op