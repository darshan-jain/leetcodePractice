class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        count = 1
        pairs.sort(key=lambda x:x[1])
        
        freetime = pairs[0][1]
        for pair in pairs[1:]:
            if pair[0] > freetime:
                count+=1
                freetime = pair[1]
            
        return count
            
        