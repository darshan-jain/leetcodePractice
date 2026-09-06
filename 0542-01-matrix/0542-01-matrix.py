from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #multi source bfs 
        rows = len(mat)
        cols = len(mat[0])
        q = deque()
        dist = [[-1]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    dist[i][j]=0
                    q.append((i,j,0))
        
        while q:
            r,c,val = q.popleft()
            lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in lst:
                if 0<=nr<rows and 0<=nc<cols and dist[nr][nc]==-1:
                    dist[nr][nc] = 1 + dist[r][c]
                    q.append((nr,nc, dist[nr][nc]))
        return dist



        

        