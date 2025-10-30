class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item =='+':
                val1 = stack.pop()
                val2=stack.pop()
                res = val2 + val1
                stack.append(res)
            elif item =='-':
                val1 = stack.pop()
                val2=stack.pop()
                res = val2 - val1
                stack.append(res)
            elif item =='*':
                val1 = stack.pop()
                val2=stack.pop()
                res = val2 * val1
                stack.append(res)
            elif item =='/':
                val1 = stack.pop()
                val2=stack.pop()
                res = val2 / val1
                stack.append(int(res))
            else:
                stack.append(int(item))

        return stack[-1]

        