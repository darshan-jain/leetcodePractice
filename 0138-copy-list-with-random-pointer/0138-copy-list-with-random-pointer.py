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
            return head
        oldtonew = {}
        curr = head
        while curr:
            node = Node(x = curr.val)
            oldtonew[curr] = node 
            curr = curr.next 
        curr = head 
        while curr:
            new_node = oldtonew[curr]
            new_node.next = oldtonew[curr.next] if curr.next else None
            new_node.random = oldtonew[curr.random] if curr.random else None
            curr = curr.next 
        return oldtonew[head]
        