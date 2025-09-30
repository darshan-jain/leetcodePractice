class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minH = maxH = grid[0][0]
        visit = [[False]*n for _ in range(n)]
        for r in range(n):
            minH = min(minH, min(grid[r]))
            maxH = max(maxH, max(grid[r]))
        
        def dfs(node,t):
            r,c = node
            if min(r,c)<0 or max(r,c)>=n or visit[r][c] or grid[r][c] > t:
                return False 
            if r==n-1 and c==n-1:
                return True
            visit[r][c] = True
            return dfs((r+1,c),t) or dfs((r-1,c),t) or dfs((r,c+1),t) or dfs((r,c-1),t)
        
        l, r = minH, maxH
        while l < r:
            m = (l + r) >> 1
            if dfs((0, 0), m):
                r = m
            else:
                l = m + 1
            for row in range(n):
                for col in range(n):
                    visit[row][col] = False

        return r
        