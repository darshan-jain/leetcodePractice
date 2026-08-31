class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addword(self, word):
        d = self.root 
        for c in word:
            if c not in d.children:
                d.children[c] = TrieNode()
            d = d.children[c]
        d.isWord = True
    
    def search(self, word, root, diff, idx):
        if diff < 0:
            return False
        
        if idx == len(word):
            return root.isWord

        letter = word[idx]

        # 1. Option A: Exact match (0 edits)
        if letter in root.children:
            if self.search(word, root.children[letter], diff, idx + 1):
                return True

        # 2. Option B: Substitution edit (1 edit) - try all other branches
        if diff > 0:
            for c, child in root.children.items():
                if c != letter:  # Skip the exact match we already tried above
                    if self.search(word, child, diff - 1, idx + 1):
                        return True

        return False



class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        root = Trie()

        for word in dictionary:
            root.addword(word)
        
        ans = []
        for word in queries:
            if root.search(word, root.root,2,0):
                ans.append(word)
        return ans

        