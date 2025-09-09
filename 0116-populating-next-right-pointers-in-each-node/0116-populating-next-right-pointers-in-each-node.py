"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        def con2nodes(p,q):
            if q is None:
                return 
            p.next = q
            con2nodes(p.left,p.right)
            con2nodes(q.left,q.right)
            con2nodes(p.right, q.left)
        con2nodes(root.left, root.right)
        return root
        