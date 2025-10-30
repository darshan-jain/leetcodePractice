class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append([position[i], speed[i]])
        
        arr.sort(reverse = True)
        print(arr)

        time = [0]*len(position)
        for i in range(len(position)):
            time[i] = (target - arr[i][0])/arr[i][1]
        
        stack = []
        for i in range(len(time)):
            if i==0:
                stack.append(time[i])
            else:
                if time[i]> stack[-1]:
                    stack.append(time[i])
        return len(stack)
        