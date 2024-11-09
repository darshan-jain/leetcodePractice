class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        leftSum = 0
        res = [leftSum]
        for i in range(len(gain)):
            leftSum += gain[i]
            res.append(leftSum)
        
        return max(res)


        