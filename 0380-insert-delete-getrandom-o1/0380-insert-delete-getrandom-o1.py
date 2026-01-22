import random
class RandomizedSet:

    def __init__(self):
        self.hm = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.hm:
            self.arr.append(val)
            self.hm[val] = len(self.arr)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hm:
            idx = self.hm[val]
            self.arr[idx] = self.arr[len(self.arr)-1]
            self.hm[self.arr[idx]] = idx
            self.arr.pop()
            del self.hm[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return self.arr[randint(0,len(self.arr)-1)]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()