# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #edge cases 
        if head is None:
            return None
        #find mid point
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        mid = slow 
        l2 = mid.next
        mid.next = None



        #reverse the 2nd List 
        curr = l2 
        prev= None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l2 = prev

        #Merge
        l1 = head
        while l1 and l2:
            l1next = l1.next
            l2next = l2.next
            l1.next = l2
            l2.next = l1next
            l1 = l1next
            l2 = l2next
        return head
        