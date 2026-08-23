class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        peri = 0 

        def bfs(r,c):
            lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            land = 0 
            for row,col in lst:
                if 0<=row<rows and 0<=col<cols and grid[row][col]==1:
                    land+=1
            nonlocal peri
            peri+=(4-land)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    bfs(i,j)
        return peri
        