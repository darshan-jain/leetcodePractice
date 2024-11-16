class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count = 0
        # while n:
        #     count +=n&1
        #     n = n>>1
        # return count
        
        count = 0
        while n:
            n = n& (n-1)
            count+=1
        return count