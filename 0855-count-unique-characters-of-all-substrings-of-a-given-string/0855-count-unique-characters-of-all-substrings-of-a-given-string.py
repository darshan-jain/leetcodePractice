class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # ans = 0 
        # uniqchar = 0 
        # for i in range(len(s)):
        #     hm = set()
        #     repeat_elem = set()
        #     for j in range(i,len(s)):
        #         if s[j] not in hm and s[j] not in repeat_elem:
        #             hm[s[j]] = 1
        #         else:
        #             repeat_elem.add(s[j])
        #             if s[j] in hm:
        #                 del hm[s[j]] 
        #         #print(s[i:j+1], uniqchar)
        #         uniqchar = len(hm)
        #         ans+=uniqchar

        # return ans

        res = 0 
        curr = 0 
        d = collections.defaultdict(lambda: [-1,-1])
        for i, c in enumerate(s):
            curr += (i-d[c][0]) - (d[c][0] - d[c][1])
            d[c][1] = d[c][0]
            d[c][0] = i 
            res+=curr
        return res
        