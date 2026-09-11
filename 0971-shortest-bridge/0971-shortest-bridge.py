from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island1 = set()
        island2 = set()
        foundisland1 = False 
        foundisland2 = False
        rows = len(grid)
        cols = len(grid[0])

        def bfs1(r,c):
            island1.add((r,c))
            lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for row,col in lst:
                if 0<=row<rows and 0<=col<cols and grid[row][col] == 1 and (row,col) not in island1:
                    bfs1(row,col)
        def bfs2(r,c):
            island2.add((r,c))
            lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for row,col in lst:
                if 0<=row<rows and 0<=col<cols and grid[row][col] == 1 and (row,col) not in island2:
                    bfs2(row,col)
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    if not foundisland1 and not foundisland2:
                        bfs1(i,j)
                        foundisland1 = True
                    elif (i,j) not in island1:
                        bfs2(i,j)
                        foundisland2 = True
                    else:
                        continue
        q = deque([])
        for (r,c) in island1:
            q.append((r,c,0))
        visit = set()
        while q:
            r,c,dist = q.popleft()
            print(r,c,dist)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if (r,c) in island2:
                print(r,c)
                return dist-1 
            lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for row,col in lst:
                if 0<=row<rows and 0<=col<cols and (row,col) not in visit:
                    if (row,col) in island2:
                        return dist
                    q.append((row,col, dist+1))
        return 99
        