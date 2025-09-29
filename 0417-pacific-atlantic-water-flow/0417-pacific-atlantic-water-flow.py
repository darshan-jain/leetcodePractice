class Solution:
    def check(self,heights, row, col , ocean):
        ocean[row][col]=True
        lst = [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]
        for r,c in lst:
            if 0<=r<len(heights) and 0<=c<len(heights[0]) and ocean[r][c]==False and heights[r][c]>=heights[row][col]:
                self.check(heights, r,c,ocean)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights), len(heights[0])
        pac = [[False for _ in range(cols)] for _ in range(rows)]
        atl = [[False for _ in range(cols)] for _ in range(rows)]
        res = []

        for i in range(rows):
            self.check(heights, i,0,pac)
            self.check(heights, i,cols-1,atl)
        
        for j in range(cols):
            self.check(heights, 0,j,pac)
            self.check(heights, rows-1, j ,atl)
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res

        