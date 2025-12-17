class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ways = [0]*(n+1)
        ways[0] = 1
        for i in range(len(s)):
            print(s[i],ways)
            if s[i]=='0':
                ways[i+1]+=0
            if 1<= int(s[i]) <=9:
                ways[i+1]+=ways[i]
            if i>=1 and 10<= int(s[i-1])*10 + int(s[i]) <=26:
                ways[i+1]+=ways[i-1]
        
        return ways[-1]
        