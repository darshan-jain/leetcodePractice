class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorsum = 0 
        for num in nums:
            xorsum^=num
        xorstr = str(bin(xorsum)[2:])
        print(xorstr, len(xorstr))
        idx = len(xorstr)
        for i in range(len(xorstr)-1,-1,-1):
            if xorstr[i]=="1":
                idx = i 
                break
        idx = len(xorstr) - idx -1 
        print(idx)
        res1 = 0 #idx bit is 0 
        res2 = 0 #idx bit is 1 
        comp = 1 
        while idx>0:
            comp = comp << 1
            idx-=1
        for num in nums:
            if num&comp==0:
                res1^=num
            else:
                res2^=num
        return [res2,res1]

        