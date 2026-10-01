class RandomizedSet:

    def __init__(self):
        self.hm = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False 
        self.arr.append(val)
        self.hm[val] = len(self.arr)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False
        idx = self.hm[val]
        newval = self.arr[len(self.arr)-1]
        self.arr[idx] = newval
        self.hm[newval] = idx
        del self.hm[val]
        
        self.arr.pop()
        return True
        

    def getRandom(self) -> int:
        ridx = random.randint(0,len(self.arr)-1)
        return self.arr[ridx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()