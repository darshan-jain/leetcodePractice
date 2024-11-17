from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for word in strs:
            dic["".join(sorted(word))].append(word)
        return dic.values()
        
        