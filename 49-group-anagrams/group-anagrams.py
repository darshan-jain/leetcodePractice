class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # hm =collections.defaultdict(list)

        # for val in strs:
        #     key = ''.join(sorted(val))
        #     hm[key].append(val)
        
        # return hm.values()

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(s)
        return res.values()

        