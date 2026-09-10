class Solution:
    def rotatedDigits(self, n: int) -> int:
        bag = {
            "0":"0",
            "1":"1",
            "8":"8",
            "2":"5",
            "5":"2",
            "6":"9",
            "9":"6"
        }
        res = []
        def isGood(val):
            val = str(val)
            new = []
            for c in val:
                if c not in bag:
                    return False
                new.append(bag[c])
            new = "".join(new)
            print(new,val)
            return int(new)!=int(val)

        for i in range(1,n+1):
            if isGood(i):
                res.append(i)
        return len(res)

        