# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k ==0:
            return head
        n = 0 
        curr = head 
        while curr:
            n+=1
            curr = curr.next 
        if n<=1:
            return head
        k = k%n
        if k ==0:
            return head
        dummy = ListNode(0,head)
        slow = dummy 
        fast = head 
        for _ in range(k):
            fast = fast.next 
        while fast:
            fast = fast.next 
            slow = slow.next 
        end = slow 
        newhead = end.next 
        end.next = None 
        cur = newhead 
        while cur.next:
            cur = cur.next 
        cur.next = head 
        return newhead
        