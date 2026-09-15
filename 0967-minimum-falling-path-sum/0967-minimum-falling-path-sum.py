class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = {}

        def dfs(r,c):
            if r == n:
                return 0 
            if c<0 or c>=n:
                return float("inf")
            if (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)] = matrix[r][c] + min(dfs(r+1,c), dfs(r+1,c+1),dfs(r+1,c-1))
            return dp[(r,c)]

        res = float("inf")
        for c in range(n):
            res = min(res, dfs(0,c))
        return res
        