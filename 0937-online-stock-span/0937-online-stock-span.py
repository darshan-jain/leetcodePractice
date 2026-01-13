class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price,1))
        else:
            if price < self.stack[-1][0]:
                self.stack.append((price,1))
            else:
                newfreq = 1
                while self.stack and price >= self.stack[-1][0]:
                    val,freq = self.stack.pop()
                    newfreq+=freq
                self.stack.append((price,newfreq))
        return self.stack[-1][1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)