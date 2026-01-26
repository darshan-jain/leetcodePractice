class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Trie()
        for word in dictionary:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.end = True
        
        visited = {}

        def dp(index):
            if index ==len(s):
                return 0 
            if index in visited:
                return visited[index]
            res = 1 + dp(index+1)
            node = root 
            for i in range(index,len(s)):
                if s[i] not in node.children:
                    break
                node = node.children[s[i]]
                if node.end:
                    res = min(res, dp(i+1))
                if res==0:
                    break
            visited[index] = res
            return res
        return dp(0)
        