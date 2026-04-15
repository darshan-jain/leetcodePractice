class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        res = []
        col = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            if r==n:
                ans = []
                for row in board:
                    val = "".join(row)
                    ans.append(val)
                res.append(ans)
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                board[r][c] = 'Q'
                col.add(c)
                posDiag.add((r+c))
                negDiag.add((r-c))
                backtrack(r+1)
                board[r][c]='.'
                col.remove(c)
                posDiag.remove((r+c))
                negDiag.remove((r-c))

        backtrack(0)
        return res
        