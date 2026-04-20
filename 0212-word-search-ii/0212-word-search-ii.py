class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False 
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addword(self,word):
        d = self.root 
        for c in word:
            if c not in d.children:
                d.children[c] = TrieNode()
            d = d.children[c]
        d.isWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        root = Trie()
        res = set()
        for word in words:
            root.addword(word)
        visit = set()
        def dfs(r,c,node, word):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit or board[r][c] not in node.children:
                return 
            word+=board[r][c]
            node = node.children[board[r][c]] 
            visit.add((r,c))
            if node.isWord:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.root.children:
                    dfs(i,j,root.root,"")
        return list(res)
                
        