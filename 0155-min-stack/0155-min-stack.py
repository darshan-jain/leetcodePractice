class MinStack:

    def __init__(self):
        self.stack = []
        self.track = []
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.track[-1] if self.track else val)
        self.track.append(val)

        

    def pop(self) -> None:
        self.track.pop()
        self.stack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.track[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()