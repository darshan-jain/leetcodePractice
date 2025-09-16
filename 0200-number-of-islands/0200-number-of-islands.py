class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            grid[row][col]='0'
            lst = [(row+1, col), (row-1,col), (row,col+1), (row,col-1)]
            for r,c in lst:
                if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]=='1':
                    dfs(r,c)
        rows, cols, = len(grid) , len(grid[0])
        island=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] =='1':
                    dfs(row, col)
                    island+=1
        return island
        