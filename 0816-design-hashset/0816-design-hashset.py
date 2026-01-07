class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.table = [None]* self.size

    def calc_hash_val(self,key):
        return key%self.size
        
    def add(self, key: int) -> None:
        hv = self.calc_hash_val(key)

        if self.table[hv]==None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)

    def remove(self, key: int) -> None:
        hv = self.calc_hash_val(key)

        if self.table[hv]!=None:
            while key in self.table[hv]:  #To remove all occurrence - but don't save all occurence
                self.table[hv].remove(key)
        

    def contains(self, key: int) -> bool:
        hv = self.calc_hash_val(key)
        if self.table[hv]!=None:
            return key in self.table[hv]
        return False  #Case where self.table[hv] is None
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)