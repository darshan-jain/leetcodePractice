class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0 
        rotten  = []
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    rotten.append((r,c))
        
        while rotten and fresh>0:
            time+=1
            curr = []
            for r,c in rotten:
                lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for row,col in lst:
                    if 0<=row<ROWS and 0<=col<COLS and grid[row][col]==1:
                        grid[row][col]=2
                        curr.append((row,col))
                        fresh-=1
                        if fresh==0:
                            return time
                rotten = curr
        
        if fresh==0:
            return time
        return -1


        