# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        
        p,slow,fast = None, head, head 
        while fast and fast.next:
            p = slow 
            slow = slow.next 
            fast = fast.next.next 
        p.next = None 

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, l1,l2):
        dummy = ListNode(0)
        tail = dummy 
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next 
            else:
                tail.next = l2 
                l2 = l2.next 
            tail = tail.next
        
        if l1:
            tail.next = l1 
        
        if l2:
            tail.next = l2 
        return dummy.next
        