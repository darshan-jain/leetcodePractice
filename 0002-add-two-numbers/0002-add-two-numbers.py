# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 if l1 else l2 
        dummy = ListNode(0)
        tail = dummy 
        carry = 0 
        while l1 or l2 or carry:
            val = 0 
            if l1:
                val+=l1.val
                l1 = l1.next
            if l2:
                val+=l2.val
                l2 = l2.next 
            val+=carry
            carry = val//10 
            val=val%10 
            node = ListNode(val)
            tail.next = node
            tail = tail.next
        return dummy.next