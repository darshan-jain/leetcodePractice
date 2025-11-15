class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sq = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                row[i].add(val)
                col[j].add(val)
                boxid = (i//3) *3 + (j//3)
                sq[boxid].add(val)
        
        def backtrack(r,c):
            if r==9:
                return True
            if c==9:
                return backtrack(r+1,0)
            if board[r][c]!='.':
                return backtrack(r,c+1)
            boxid = (r//3)*3 + (c//3)
            for num in "123456789":
                if num not in row[r] and num not in col[c] and num not in sq[boxid]:
                    board[r][c] = num
                    row[r].add(num)
                    col[c].add(num)
                    sq[boxid].add(num)
                    if backtrack(r,c+1):
                        return True
                    board[r][c] = '.'
                    row[r].remove(num)
                    col[c].remove(num)
                    sq[boxid].remove(num)
            return False


        backtrack(0,0)
        