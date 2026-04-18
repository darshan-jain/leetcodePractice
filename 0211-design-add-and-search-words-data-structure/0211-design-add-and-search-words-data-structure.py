class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        d = self.root 
        for c in word:
            if c not in d.children:
                d.children[c] = TrieNode()
            d = d.children[c]
        d.isWord = True
        

    def search(self, word: str) -> bool:
        d = self.root
        def dfs(root, word):
            curr = root 
            for i,c in enumerate(word):
                if c=='.':
                    for child in curr.children.values():
                        if dfs(child, word[i+1:]):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False 
                    curr = curr.children[c]
            return curr.isWord
        return dfs(d, word)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)