class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        # box number - allowed directions

        hm = {
            1: [(0,-1), (0,1)],
            2: [(-1,0),(1,0)], 
            3: [(1,0), (0,-1)],
            4: [(0,1), (1,0)],
            5: [(-1,0), (0,-1)], 
            6: [(-1,0), (0,1)]
        }

        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def isAllowed(r,c,pr,pc):
            if pr==-1 and pc==-1:
                return True
            vals = hm[grid[r][c]]
            lst = set()
            for dr,dc in vals:
                lst.add((r+dr, c+dc))
            return (pr,pc) in lst

        def dfs(r,c,pr,pc):
            #base condition
            print(r,c)
            if r == rows-1 and c == cols-1 and isAllowed(r,c,pr,pc): # add allowed check
                return True
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit or not isAllowed(r,c,pr,pc):
                return 
            visit.add((r,c))
            dirr = hm[grid[r][c]]
            dr1, dc1 = dirr[0]
            dr2, dc2 = dirr[1]
            return dfs(r+dr1, c+dc1, r,c) or dfs(r+dr2, c+dc2, r,c)


        if dfs(0,0,-1,-1):
            return True
        else:
            return False

        