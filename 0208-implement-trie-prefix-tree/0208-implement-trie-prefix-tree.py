class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        d = self.root 
        for c in word:
            if c not in d.children:
                d.children[c] = TrieNode()
            d = d.children[c]
        d.isWord = True
        

    def search(self, word: str) -> bool:
        d = self.root 
        for c in word:
            if c not in d.children:
                return False 
            d = d.children[c]
        return d.isWord
        

    def startsWith(self, prefix: str) -> bool:
        d = self.root 
        for c in prefix:
            if c not in d.children:
                return False 
            d = d.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)