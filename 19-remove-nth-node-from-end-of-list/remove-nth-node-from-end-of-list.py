# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)
        p1 = head
        p2 = dummy
        counts = 0
        while p1 != None:
            p1 = p1.next
            counts+=1
            if counts > n:
                p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
        
        