class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>=0 else -1
        if x<0:
            x = x*sign
        s = str(x)
        s= s[::-1]
        x = int(s)
        x = x*sign
        return x if x >-2**31 and x<=2**31 -1 else 0
        