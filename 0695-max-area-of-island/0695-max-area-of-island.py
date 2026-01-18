class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0 

        def bfs(r,c,area):
            area+=1
            grid[r][c]=0
            lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for row,col in lst:
                if row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and grid[row][col]==1:
                    area = bfs(row,col,area)
            print(area)
            return area

        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area = bfs(i,j,0)
                    maxarea = max(area,maxarea)
        return maxarea
        