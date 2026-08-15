class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <=1:
            return False
        tot = 1
        i = 2
        while i*i <=num:
            if num%i==0:
                tot+=i
                if i*i!=num:
                    tot+=(num//i)
            i+=1
        return tot==num

        