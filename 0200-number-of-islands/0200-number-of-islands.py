class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row,col):
            grid[row][col]='0'
            lst = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for r,c in lst:
                if 0<=r<len(grid) and 0 <=c<len(grid[0]) and grid[r][c]=='1':
                    dfs(r,c)
                    
        island=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1':
                    dfs(r,c)
                    island+=1
        return island
        