class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for word in strs:
            sword = sorted(word)
            sword = ''.join(sword)
            if sword not in hm:
                hm[sword] = []
            hm[sword].append(word)
        ans = []
        for k,v in hm.items():
            ans.append(v)

        return ans