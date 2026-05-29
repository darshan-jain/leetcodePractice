class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0 
        def dfs(r,c):
            grid[r][c]='0'
            lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for row, col in lst:
                if 0<=row<rows and 0<=col<cols and grid[row][col]=='1':
                    dfs(row,col)
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    dfs(i,j)
                    island+=1
        return island
        