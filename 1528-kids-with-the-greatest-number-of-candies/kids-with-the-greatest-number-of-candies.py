class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandies = max(candies)
        ans = []
        
        for i in range(len(candies)):
            candyCount = candies[i] + extraCandies
            if candyCount >= maxCandies:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
        