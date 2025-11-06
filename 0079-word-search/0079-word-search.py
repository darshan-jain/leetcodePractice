class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r,c,i):
            if i>=len(word):
                return True
            if r<0 or r>=rows or c<0 or c>=cols or word[i]!=board[r][c]:
                return False
            letter = board[r][c]
            board[r][c]=""
            found = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            board[r][c] = letter
            if found:
                return True
                

        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0] and dfs(r,c,0):
                    return True
        return False
        