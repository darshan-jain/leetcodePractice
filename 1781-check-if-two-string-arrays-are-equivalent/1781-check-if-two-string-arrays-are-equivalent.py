class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res1 = ""
        for word in word1:
            res1+=word
        res2=""
        for word in word2:
            res2+=word
        return res1==res2
        