# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(-2000, head)
        prev = dummy 
        curr = head 
        while curr:
            #delete
            if curr.val==prev.val:
                while curr and curr.val==prev.val:
                    curr=curr.next
                prev.next = curr

            #not deleted
            else:
                curr = curr.next 
                prev = prev.next 
        return dummy.next
        