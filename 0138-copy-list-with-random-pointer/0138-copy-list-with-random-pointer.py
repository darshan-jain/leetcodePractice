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
        if head is None:
            return None
        oldtonew = {}
        cur = head 
        while cur:
            oldtonew[cur] = Node(cur.val)
            cur = cur.next 
        cur = head 
        while cur:
            newnode = oldtonew[cur]
            newnode.next = oldtonew[cur.next] if cur.next in oldtonew else None 
            newnode.random = oldtonew[cur.random] if cur.random in oldtonew else None
            cur = cur.next
        return oldtonew[head]
        