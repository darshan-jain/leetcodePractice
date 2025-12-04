# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        leftPre = dummy 
        curr = head 
        for i in range(left-1):
            leftPre = leftPre.next 
            curr = curr.next 
        
        subListHead = curr 

        preNode = None
        for i in range(right-left+1):
            nextNode = curr.next 
            curr.next = preNode
            preNode = curr 
            curr = nextNode 
        
        leftPre.next = preNode 
        subListHead.next = curr
        return dummy.next
        