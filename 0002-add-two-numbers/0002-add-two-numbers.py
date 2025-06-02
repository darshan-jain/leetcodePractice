# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        dummy = ListNode(0)
        tail = dummy 
        val = 0 
        while l1 or l2 or carry:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val+=l2.val
                l2 = l2.next
            carry = val//10
            val = val%10
            tail.next = ListNode(val)
            tail = tail.next
            val = carry
        
        return dummy.next

        