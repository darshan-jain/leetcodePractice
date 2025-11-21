# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        dummy  = ListNode(0,head)
        prev = dummy
        while curr:
            if curr.val==val:
                prev.next = prev.next.next if prev.next else None
                curr = prev.next
            else:
                curr = curr.next 
                prev = prev.next 
        return dummy.next
        