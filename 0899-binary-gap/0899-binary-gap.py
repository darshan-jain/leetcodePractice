class Solution:
    def binaryGap(self, n: int) -> int:
        binval = str(bin(n)[2:]) 
        stack = []
        right = []
        for i in range(len(binval)-1,-1,-1):
            
            while stack and binval[stack[-1]]=="0":
                stack.pop()

            if stack:
                right.append(stack[-1])
            else:
                right.append(-1)
            stack.append(i)
        right = right[::-1]
        print(right)
        res = [0]*len(right)
        for i in range(len(right)):
            if binval[i]=="1" and right[i]>0:
                res[i]=right[i]-i
        return max(res)

        
        