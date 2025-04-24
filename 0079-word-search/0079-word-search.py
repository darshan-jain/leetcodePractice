class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row,col,index):
            if index>=len(word):
                return True
            if 0<=row<len(board) and 0<=col < len(board[0]) and board[row][col]==word[index]:
                letter = board[row][col]
                board[row][col]=""
                found = dfs(row+1,col,index+1) or dfs(row-1,col,index+1) or dfs(row,col+1,index+1) or dfs(row,col-1,index+1)
                board[row][col]=letter
                if found:
                    return True
            else:
                return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0] and dfs(row,col,0):
                    return True
        return False
        