class TrieNode():
    def __init__(self):
        self.children = {}
        self.endofword = False 
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True
    
    def search(self,word):
        cur = self.root 
        for c in word:
            if c not in cur.children:
                return False 
            cur = cur.children[c]
            if not cur.endofword:
                return False 
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        for w in words:
            t.insert(w)
        res = []
        for w in words:
            if t.search(w):
                res.append(w)
        if res:
            res.sort(key = lambda x : (-len(x),x))
        else:
            return ''
        return res[0]
        