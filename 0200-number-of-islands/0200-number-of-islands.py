class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0 
        def bfs(r,c):
            grid[r][c] = "0"
            lst = [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]
            for row,col in lst:
                if row>=0 and row<len(grid) and col >=0 and col<len(grid[0]) and grid[row][col]=="1":
                    bfs(row,col)
            



        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    bfs(i,j)
                    island+=1
        return island
        