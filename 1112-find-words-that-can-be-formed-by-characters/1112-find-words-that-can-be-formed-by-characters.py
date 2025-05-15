class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def satisfied(countword,count):
            for k,v in countword.items():
                if k not in count:
                    return False
                if count[k] <v:
                    return False
            return True

        count= Counter(chars)
        res = 0 
        for word in words:
            countword = Counter(word)
            if satisfied(countword,count):
                res+=len(word)
        return res
        