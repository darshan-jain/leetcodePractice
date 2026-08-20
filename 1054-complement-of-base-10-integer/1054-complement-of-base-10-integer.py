class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binvalstr = str(bin(n)[2:])
        res = ""
        for c in binvalstr:
            if c =="1":
                res+="0"
            else:
                res+="1"
        return int(res,2)
        