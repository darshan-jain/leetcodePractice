class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n = numerator
        d = denominator

        if (n%d)==0:
            return str(n//d)
        
        res = []
        if (n<0 and d>0) or (n>0 and d<0):
            res.append('-')
        n = abs(n)
        d = abs(d)
        res.append(str(n//d))
        res.append('.')

        rem = n%d
        seen = {}

        while rem!=0:
            if rem in seen:
                res.insert(seen[rem],'(')
                res.append(')')
                break
            seen[rem] = len(res)
            rem*=10
            res.append(str(rem//d))
            rem = rem%d

        return "".join(res)
        
        