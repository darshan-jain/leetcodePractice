class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c=='(':
                stack.append(')')
            elif c =='[':
                stack.append(']')
            elif c=='{':
                stack.append('}')
            else:
                if not stack or c!=stack[-1]:
                    return False
                else:
                    stack.pop()
        return True if len(stack)==0 else False
        