class Node:
    def __init__(self,key,value):
        self.key = key 
        self.val = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next =self.right
        self.right.prev = self.left
    
    def insert(self,node):
        last,prev = self.right, self.right.prev 
        prev.next = node
        node.prev = prev 
        node.next = last 
        last.prev = node
    
    def remove(self,node):
        prev,nxt = node.prev, node.next
        prev.next = nxt 
        nxt.prev= prev
        

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

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)