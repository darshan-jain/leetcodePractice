class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        s = list(s)
        for ele in s:
            if ele == '(':
                stack.append(')')
            elif ele == '{':
                stack.append('}')
            elif ele == '[':
                stack.append(']')
            elif not stack or stack.pop()!=ele:
                return False
        
        return not stack