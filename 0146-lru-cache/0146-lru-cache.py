class Node:
    def __init__(self,key,val):
        self.key = key 
        self.val = val 
        self.prev = None 
        self.next = None 
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity 
        self.leftNode = Node(0,0)
        self.rightNode = Node(0,0)
        self.leftNode.next = self.rightNode 
        self.rightNode.prev = self.leftNode
    
    def insert(self,node):
        last, prev = self.rightNode, self.rightNode.prev
        prev.next = node 
        node.prev = prev
        last.prev = node 
        node.next = last
    
    def remove(self,node):
        prev,nxt = node.prev, node.next
        prev.next = nxt 
        nxt.prev = prev
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            oldnode = self.cache[key]
            self.remove(oldnode)
        newnode = Node(key,value)
        self.cache[key] = newnode
        self.insert(newnode)

        if len(self.cache) > self.capacity:
            lru = self.leftNode.next 
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)