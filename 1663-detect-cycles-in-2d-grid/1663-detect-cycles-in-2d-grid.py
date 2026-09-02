class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(r,c,pr,pc, char):
            visit.add((r,c))
            lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for row,col in lst:
                if 0<=row<rows and 0<=col<cols and grid[row][col]==char:
                    if row==pr and col == pc:
                        continue
                    if (row,col) in visit:
                        return True
                    
                    if dfs(row,col, r,c,char):
                        return True
            return False

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit:
                    if dfs(i,j, -1,-1, grid[i][j]):
                        return True
        return False
        