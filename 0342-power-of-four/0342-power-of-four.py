class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        x = math.log(n,4)
        return int(x)==x

        