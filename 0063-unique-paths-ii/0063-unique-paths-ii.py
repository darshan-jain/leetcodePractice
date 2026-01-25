class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #edge case
        if obstacleGrid[0][0]==1:
            return 0 
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        grid = [[1]*cols for _ in range(rows)]
        

        #mark other obstacle
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j]==1:
                    grid[i][j]=0
        
        for i in range(rows):
            for j in range(cols):
                if i==0 and j>0 and grid[i][j-1]==0:
                    grid[i][j]=0
                if j==0 and i>0 and grid[i-1][j]==0:
                    grid[i][j]=0

        print(grid)
        
        
        for i in range(1,rows):
            for j in range(1,cols):
                if grid[i][j]==0:
                    continue
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        print(grid)
        return grid[-1][-1]

        

        