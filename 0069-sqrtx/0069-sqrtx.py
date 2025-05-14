class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==1 or x==0:
            return x
        l = 1
        r = x//2
        while l <= r:
            m = (l+r)//2
            if m*m==x:
                return m
            elif m*m < x:
                l=m+1
            else:
                r=m-1
        return r
        