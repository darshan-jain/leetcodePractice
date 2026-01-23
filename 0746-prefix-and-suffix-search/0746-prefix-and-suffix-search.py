class WordFilter:

    def __init__(self, words: List[str]):
        self.hm= defaultdict(list)
        for i,w in enumerate(words):
            self.hm[(w[0],w[-1])].append((i,w))
        
        

    def f(self, pref: str, suff: str) -> int:
        if (pref[0],suff[-1]) not in self.hm:
            return -1
        lst = self.hm[(pref[0],suff[-1])]
        for i in range(len(lst)-1,-1,-1):
            prefLen = len(pref)
            suffLen = len(suff)
            idx,word = lst[i]
            if word[0:prefLen]==pref and word[len(word)-suffLen:]==suff:
                return idx
        
        return -1
       
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)