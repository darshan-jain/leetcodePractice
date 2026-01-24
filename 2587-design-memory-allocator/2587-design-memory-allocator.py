class Allocator:

    def __init__(self, n: int):
        self.arr = [-1]*n
        self.n = n
        
    def allocate(self, size: int, mID: int) -> int:
        available = 0 
        for i in range(self.n):
            if self.arr[i]==-1:
                available+=1
            else:
                available = 0 
            if available ==size:
                for j in range(i-size+1, i+1):
                    self.arr[j] = mID
                return i-size+1
        return -1
        

    def freeMemory(self, mID: int) -> int:
        count=0
        for i in range(self.n):
            if self.arr[i]==mID:
                self.arr[i]=-1
                count+=1
        return count
        
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)