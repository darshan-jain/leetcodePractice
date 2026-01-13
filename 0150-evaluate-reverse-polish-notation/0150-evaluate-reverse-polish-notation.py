class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t=='+':
                val2 = stack.pop()
                val1 = stack.pop()
                val3 = val1 + val2
                stack.append(val3)
            elif t=='*':
                val2 = stack.pop()
                val1 = stack.pop()
                val3 = val1 * val2
                stack.append(val3)
            elif t =='/':
                val2 = stack.pop()
                val1 = stack.pop()
                val3 = val1 / val2
                stack.append(int(val3) )
            elif t =='-':
                val2 = stack.pop()
                val1 = stack.pop()
                val3 = val1 - val2
                stack.append(val3) 
            else:
                stack.append(int(t))
        return stack[-1]
        