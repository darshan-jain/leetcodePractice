class Solution:
    def signFunc(self,val):
        if val >0:
            return 1
        elif val<0:
            return -1 
        else:
            return 0 
    def arraySign(self, nums: List[int]) -> int:
        val = 1
        for num in nums:
            val*=num
        return self.signFunc(val)
        