from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0 
        rotten = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    rotten.append([i,j])
        
        time = -1 
        visit = set()
        if fresh==0:
            return 0
        while rotten:
            time+=1
            print(rotten)
            for _ in range(len(rotten)):
                r,c  = rotten.popleft()
                lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for row,col in lst:
                    if row>=0 and row<len(grid) and col>=0  and col < len(grid[0]) and grid[row][col]==1 and (row,col) not in visit:
                        fresh-=1
                        grid[row][col]=2
                        visit.add((row,col))
                        rotten.append([row,col])
        
        return time if fresh==0 else -1
            
        