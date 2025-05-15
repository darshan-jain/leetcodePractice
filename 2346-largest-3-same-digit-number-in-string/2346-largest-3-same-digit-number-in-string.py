class Solution:
    def largestGoodInteger(self, num: str) -> str:

        #get all substring of len 3 with 1 unique element
        options = []
        #num = str(num)
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                options.append(int(num[i:i+3]))
        options.sort()
        print(options)
        if options:
            if options[-1]==0:
                return "000"
            else:
                return str(options[-1]) 
        else:
            return ""
