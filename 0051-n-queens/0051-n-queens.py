class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posDiag = set()
        negDiag = set()
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r>=n:
                part = []
                temp = ""
                for row in board:
                    temp = "".join(row)
                    part.append(temp)
                res.append(part)
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
        