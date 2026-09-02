class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c, pr, pc, char):
            visit.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # Check boundary and matching character
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                    # Skip the cell we just came from
                    if (nr, nc) == (pr, pc):
                        continue
                    
                    # If neighbor is already visited, we found a cycle!
                    if (nr, nc) in visit:
                        return True
                    
                    if dfs(nr, nc, r, c, char):
                        return True

            return False

        for r in range(rows):
            for c in range(cols):
                # Only start DFS from unvisited cells
                if (r, c) not in visit:
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True

        return False