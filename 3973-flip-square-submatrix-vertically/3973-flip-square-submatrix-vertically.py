class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        newmat = [[0]*k for _ in range(k)]
        for i in range(x,x+k):
            for j in range(y,y+k):
                newmat[i-x][j-y] = grid[i][j]
        
        for i in range(len(newmat)//2):
            newmat[i],newmat[k-i-1] = newmat[k-i-1], newmat[i]
        
        for i in range(x,x+k):
            for j in range(y,y+k):
                grid[i][j] = newmat[i-x][j-y]
        return grid
        