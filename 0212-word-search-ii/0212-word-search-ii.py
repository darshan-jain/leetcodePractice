class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False 
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        res = set()
        visit = set()
        root = Trie()
        for word in words:
            root.addWord(word)
        
        def dfs(r,c,node,word):
            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or (r,c) in visit or board[r][c] not in node.children:
                return 
            visit.add((r,c))
            word+=board[r][c]
            node = node.children[board[r][c]]
            if node.isWord:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        
        for i in range(m):
            for j in range(n):
                dfs(i,j,root,"")
        return list(res)

        