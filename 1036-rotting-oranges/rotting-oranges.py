class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh =0 
        rotten = []
        time = 0 
        rows,cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    fresh+=1
                if grid[row][col]==2:
                    rotten.append((row,col))

        while rotten and fresh > 0 :
            time+=1
            curr = []
            for r,c in rotten:
                lst = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
                for row,col in lst:
                    if 0<=row<rows and 0<=col<cols and grid[row][col]==1:
                        grid[row][col]=2
                        fresh-=1
                        curr.append((row,col))
                        if fresh==0:
                            return time
            rotten = curr
        
        if fresh==0:
            return time
        else:
            return -1
        