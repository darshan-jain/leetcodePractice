# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        sublistprev = dummy 
        curr = head 
        for _ in range(left-1):
            sublistprev = sublistprev.next
            curr = curr.next
        sublisthead = curr 
        preNode = None 
        for _ in range(right-left+1):
            temp = curr.next
            curr.next = preNode
            preNode = curr 
            curr = temp
        sublisthead.next= curr
        sublistprev.next = preNode
        return dummy.next
        