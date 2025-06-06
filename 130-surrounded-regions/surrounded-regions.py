class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board) , len(board[0])

        def capture(r,c):
            if (r<0 or r==rows or c<0 or c==cols or board[r][c]!="O"):
                return 
            board[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c-1)
            capture(r,c+1)

        
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=='O' and (row==0 or row==rows-1 or col==0 or col==cols-1):
                    capture(row,col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=='O':
                    board[row][col]='X'
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=='T':
                    board[row][col]='O'
        

        