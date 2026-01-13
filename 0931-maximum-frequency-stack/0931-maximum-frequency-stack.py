class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxV = 0 
        self.stacks = {}
        

    def push(self, val: int) -> None:
        valcnt = 1 + self.count.get(val,0)
        self.count[val] = valcnt 
        if valcnt > self.maxV:
            self.maxV = valcnt 
            self.stacks[valcnt] = []
        self.stacks[valcnt].append(val)
        

    def pop(self) -> int:
        res = self.stacks[self.maxV].pop()
        self.count[res]-=1
        if not self.stacks[self.maxV]:
            self.maxV-=1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()