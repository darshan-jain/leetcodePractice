class Solution:
    def decodeString(self, s: str) -> str:

        # 3[a2[c]]
        # stack = ['3','[','a',]
        # curr = 'c'
        # num = 2 


        stack = []

        for c in s:
            if c!=']':
                stack.append(c)
            else:
                curr=""
                while stack and stack[-1]!='[':
                    curr = stack.pop() + curr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(curr * int(num))
        return "".join(stack)

                

        