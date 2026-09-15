class Node:
    def __init__(self, val, nxt, prev):
        self.val = val
        self.next = nxt
        self.prev = prev
class MyLinkedList:

    def __init__(self):
        self.size = 0 
        self.leftNode = Node(0,None,None)
        self.rightNode = Node(0,None,None)
        self.leftNode.next = self.rightNode
        self.rightNode.prev = self.leftNode
        

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        i = -1
        curr = self.leftNode
        while i<index:
            i+=1
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        self.size+=1
        prev,nxt = self.leftNode, self.leftNode.next
        newnode = Node(val, None, None)
        prev.next = newnode
        newnode.prev = prev 
        newnode.next = nxt
        nxt.prev = newnode
        

    def addAtTail(self, val: int) -> None:
        self.size+=1
        last, prev = self.rightNode, self.rightNode.prev 
        newnode = Node(val, None, None)
        prev.next = newnode 
        newnode.prev = prev 
        newnode.next = last 
        last.prev = newnode
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index == self.size:
            self.addAtTail(val)
        else:
            self.size+=1
            i = -1 
            curr = self.leftNode
            while i<index:
                i+=1
                curr = curr.next
            prev, last = curr.prev, curr
            newnode = Node(val,None,None)
            prev.next = newnode 
            newnode.prev = prev 
            newnode.next = last
            last.prev = newnode
        
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 
        else:
            self.size-=1
            i = -1 
            curr = self.leftNode 
            while i<index:
                curr = curr.next
                i+=1
            prev = curr.prev
            nxt = curr.next
            prev.next = nxt
            nxt.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)