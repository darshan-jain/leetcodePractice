# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while slow and fast:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next
        return slow
        