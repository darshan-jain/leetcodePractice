"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtonew = {}
        curr = head 
        if curr is None:
            return None 
        while curr:
            oldtonew[curr] = Node(curr.val)
            curr = curr.next
        
        for oldnode, newnode in oldtonew.items():
            newnode.next = oldtonew[oldnode.next] if oldnode.next else None
            newnode.random = oldtonew[oldnode.random] if oldnode.random else None 
        return oldtonew[head]
        