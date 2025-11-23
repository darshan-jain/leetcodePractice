class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = []
        stackt = []
        for c in s:
            if c=='#':
                if len(stacks)>0:
                    stacks.pop()
            else:
                stacks.append(c)
        for c in t:
            if c=='#':
                if len(stackt)>0:
                    stackt.pop()
            else:
                stackt.append(c)
        return stacks==stackt
        