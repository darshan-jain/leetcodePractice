class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm =collections.defaultdict(list)

        for val in strs:
            key = ''.join(sorted(val))
            hm[key].append(val)
        
        return hm.values()

        