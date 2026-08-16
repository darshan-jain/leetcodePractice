class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        def getval(a,b):
            if a == abs(b) or abs(a)== b:
                return 0
            if a<0:
                if abs(a)> b:
                    return a 
                else:
                    return b 
            else:
                if abs(b)>a:
                    return b 
                else:
                    return a 
            
        for val in asteroids:
            if not stack:
                stack.append(val)
            else:
                if (val>0 and stack[-1]>0 ) or (val<0 and stack[-1]<0):
                    stack.append(val)
                else:
                    #different direction 
                    stack.append(val)
                    while len(stack)>=2 and (val<0 and stack[-2]>0):
                        a = stack.pop()
                        b = stack.pop()
                        fval = getval(a,b)
                        print(a,b,val)
                        if fval==0:
                            break
                        stack.append(fval)
                        val = fval
                        
        return stack
                    
                    
        