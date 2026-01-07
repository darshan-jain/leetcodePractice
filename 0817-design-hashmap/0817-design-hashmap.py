class MyHashMap:

    def __init__(self):
        self.size = 1000000
        self.table = [-1]*self.size
        
    def calc_hashval(self,key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hv = self.calc_hashval(key)
        self.table[hv]=value

    def get(self, key: int) -> int:
        hv = self.calc_hashval(key)
        return self.table[hv]
        

    def remove(self, key: int) -> None:
        hv = self.calc_hashval(key)
        self.table[hv] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)