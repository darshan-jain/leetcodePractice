class Solution:
    def dfs(self,board, word, row, col,ind):
        if ind >= len(word):
            return True

        if 0<=row<len(board) and 0<=col<len(board[0]) and word[ind]==board[row][col]:
            letter = board[row][col]
            board[row][col] = ''
            found = self.dfs(board,word,row+1,col,ind+1) or self.dfs(board,word,row-1,col,ind+1) or self.dfs(board,word,row,col+1,ind+1) or self.dfs(board,word,row,col-1,ind+1)
            board[row][col] = letter
            if found:
                return True
        else:
            return False

        
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board) , len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col]==word[0] and self.dfs(board,word,row,col,0):
                    return True
        
        return False
        