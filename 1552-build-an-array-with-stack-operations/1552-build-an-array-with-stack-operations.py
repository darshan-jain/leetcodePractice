class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        vals = set(target)
        op = []
        stack = []
        for i in range(1,n+1):
            if stack==target:
                break
            op.append("Push")
            stack.append(i)
            if i in vals:
                continue
            else:
                op.append("Pop")
                stack.pop()
        return op

        