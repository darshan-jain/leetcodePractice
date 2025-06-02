class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0 
        sign = 1
        result = 0 

        while idx<len(s) and s[idx]==" ":
            idx+=1
        if idx <len(s) and s[idx] in ("-","+"):
            if s[idx]=='-':
                sign = -1
            idx+=1
        while idx<len(s) and s[idx].isnumeric():
            result = result*10+int(s[idx])
            idx+=1
        result*=sign

        if result<-2**31:
            return -2**31
        elif result>2**31 -1:
            return 2**31 -1
        return result