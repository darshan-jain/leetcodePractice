class Solution:
    def countunique(self, s, pos, uniqelem, maxcount):
        if pos == len(s):
            maxcount[0] = max(maxcount[0], len(uniqelem))
            return 
        substr = ""
        for i in range(pos, len(s)):
            substr +=s[i]

            if substr not in uniqelem:
                uniqelem.add(substr)
                self.countunique(s,i+1,uniqelem, maxcount)
                uniqelem.remove(substr)
        

    def maxUniqueSplit(self, s: str) -> int:
        maxcount = [0]
        uniqelem = set()
        self.countunique(s,0,uniqelem, maxcount)
        return maxcount[0]