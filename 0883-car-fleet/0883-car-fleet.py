class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = []
        for a,b in zip(position, speed):
            t.append((a,b))
        t.sort(reverse = True)
        nt = []
        for val,s in t:
            nt.append((target-val)/s)
        print(nt)
        stack = []
        for val in nt:
            if not stack:
                stack.append(val)
            else:
                if val > stack[-1]:
                    stack.append(val)
        print(stack)
        return len(stack)

        