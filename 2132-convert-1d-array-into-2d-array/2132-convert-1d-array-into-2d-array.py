class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        k = 0 
        grid = [[0]*n for _ in range(m)]
        if m*n != len(original):
            return []
        for i in range(m):
            for j in range(n):
                grid[i][j] = original[k]
                k+=1
        return grid
        