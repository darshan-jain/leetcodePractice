class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            grid[r][c]='0'
            lst = [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]
            for row,col in lst:
                if 0<=row<rows and 0<=col<cols and grid[row][col]=='1':
                    dfs(row,col)

        rows = len(grid)
        cols = len(grid[0])
        island = 0 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1':
                    dfs(row,col)
                    island+=1
        return island
        