class MyHashMap:

    def __init__(self):
        self.seen = set()
        self.vals = []
        

    def put(self, key: int, value: int) -> None:
        if key in self.seen:
            for item in self.vals:
                if item[0]==key:
                    item[1]= value
        else:
            self.vals.append([key,value])
            self.seen.add(key)
        

    def get(self, key: int) -> int:
        if key in self.seen:
            for item in self.vals:
                if key==item[0]:
                    return item[1]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.seen:
            for i,item in enumerate(self.vals):
                if item[0]==key:
                    break
            self.vals.pop(i)
            self.seen.remove(key)

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)