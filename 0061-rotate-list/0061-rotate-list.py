# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rotateOnce(head):
            prev = head 
            last = head.next 
            while last and last.next:
                last = last.next 
                prev = prev.next 
            
            prev.next = None 
            last.next = head 
            head = last 
            return head
        if not head or not head.next:
            return head 
        if k==0:
            return head 
        
        size = 0 
        curr = head 
        while curr:
            curr = curr.next
            size+=1
        
        k = k%size 

        while k>0:
            head = rotateOnce(head)
            k-=1
        return head


        