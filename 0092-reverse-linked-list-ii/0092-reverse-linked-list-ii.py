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
            curr = curr.next
            leftPre = leftPre.next
        subListhead = curr 
        preNode = None
        for _ in range(right-left+1):
            temp = curr.next
            curr.next = preNode
            preNode =curr
            curr = temp
        subListhead.next = curr 
        leftPre.next = preNode
        return dummy.next


        