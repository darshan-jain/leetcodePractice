# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # arr = []
        # for i in range(n):
        #     arr.append(i+1)
        l = 1
        r = n
        while l<=r:
            m = (l+r)//2
            val = guess(m)
            if val==0:
                return m
            elif val ==-1:
                r = m-1
            else:
                l = m+1
        return 0
        