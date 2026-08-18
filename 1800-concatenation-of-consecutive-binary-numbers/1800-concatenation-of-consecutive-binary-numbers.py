class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        for i in range(1, n+1):
            binval =str(bin(i)[2:])
            res+=binval
        dec = int(res, 2)
        return dec % (10**9 + 7)
        