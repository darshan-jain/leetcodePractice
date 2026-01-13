class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        def check(a,b):
            if a > abs(b):
                return a
            elif a==abs(b):
                return None
            else:
                return b
        
        for el in asteroids:
            if not stack:
                stack.append(el)
            else:
                #if in same direction just append 
                if (el > 0 and stack[-1]>0 ) or (el<0 and stack[-1]<0):
                    stack.append(el)

                #else in opp direction
                #check until it reaches the same direction 
                else:
                    stack.append(el)
                    while len(stack)>=2 and ( (stack[-2] > 0 and stack[-1]<0 )):
                        a = stack.pop()
                        b = stack.pop()
                        newval = check(b,a)
                        if newval==None:
                            continue
                        else:
                            stack.append(newval)
                            
        return stack
        