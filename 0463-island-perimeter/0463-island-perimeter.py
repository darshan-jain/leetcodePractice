class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0 
        m = len(grid)
        n = len(grid[0])

        def bfs(r,c):
            lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            cnt = 0 
            for row,col in lst:
                if row>=0 and row<len(grid) and col>=0 and col<len(grid[0]):
                    if grid[row][col]==1:
                        cnt+=1
            print(cnt)
            nonlocal peri
            peri+=(4-cnt)
            return 
            


        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    bfs(r,c)
        return peri
        