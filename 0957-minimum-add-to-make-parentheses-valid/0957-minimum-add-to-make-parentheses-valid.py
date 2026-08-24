class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        s = list(s)
        cnt = 0 
        for c in s:
            if c=='(':
                stack.append(')')
            else:
                if stack and stack[-1]==c:
                    stack.pop()
                else:
                    cnt+=1
        return cnt+len(stack)
        