class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        arr = []
        for i in range(len(position)):
            arr.append([position[i], speed[i]])
        
        arr.sort(reverse=True)

        times = []

        for pos,speed in arr:
            time = (target-pos)/speed
            times.append(time)
        
        stack = []

        for item in times:
            if stack:
                if item > stack[-1]:
                    stack.append(item)
            
            else:
                stack.append(item)
        return len(stack)


        