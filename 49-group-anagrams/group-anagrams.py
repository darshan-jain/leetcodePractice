class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = collections.defaultdict(list)

        for val in strs:
            key = ''.join(sorted(val))
            dict[key].append(val)
        
        return dict.values()
        