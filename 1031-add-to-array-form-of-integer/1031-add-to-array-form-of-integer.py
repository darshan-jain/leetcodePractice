class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        val = 0 
        for i in num:
            val = (val*10) + i 
        val = val+k
        res = []
        while val >0:
            res.append(val%10)
            val=val//10
        return res[::-1]
        