# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast= fast.next.next 
        
        mid = slow 
        nxt = mid.next
        mid.next = None 
        prev= None 
        while nxt:
            temp= nxt.next 
            nxt.next = prev 
            prev = nxt 
            nxt = temp 
        
        head2 = prev 
        head1 = head 
        while head1 and head2:
            l1next = head1.next 
            l2next = head2.next 
            head1.next = head2
            head2.next = l1next 
            head1 = l1next
            head2 = l2next 
        

        