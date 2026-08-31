class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        ans = []
        def getdist(w1,w2):
            res = 0 
            for a,b in zip(w1,w2):
                if a!=b:
                    res+=1
            return res
        
        for word in queries:
            for ww in dictionary:
                val = getdist(word, ww)
                if val<=2:
                    ans.append(word)
                    break
        return ans
        