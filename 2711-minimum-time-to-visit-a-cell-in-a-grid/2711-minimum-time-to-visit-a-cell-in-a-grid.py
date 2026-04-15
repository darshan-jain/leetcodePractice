import heapq
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0])>1:
            return -1
        
        minheap = [(0,0,0)] #time, r,c
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        while minheap:
            t,r,c = heapq.heappop(minheap)
            if r == ROWS-1 and c==COLS-1:
                return t 
            nei = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in nei:
                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or (nr,nc) in visit:
                    continue
                wait = 0 
                if abs(grid[nr][nc]-t)%2==0:
                    wait = 1 
                n_time = max(t+1, grid[nr][nc]+wait)
                heapq.heappush(minheap,(n_time, nr,nc))
                visit.add((nr,nc))
        

        