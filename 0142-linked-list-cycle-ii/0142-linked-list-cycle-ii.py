# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None 
        slow =head 
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                new = head 
                while new and slow:
                    if new ==slow:
                        return new
                    new = new.next 
                    slow = slow.next 
                    
        return None
        
        

        