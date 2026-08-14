# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1,head)
        groupPrev = dummy 
        def getkthnode(node,k):
            curr = node 
            while curr and k>0:
                curr = curr.next
                k-=1
            return curr


        while True:
            kth = getkthnode(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next 
            prev, curr = groupNext, groupPrev.next
            while curr!=groupNext:
                temp = curr.next
                curr.next = prev 
                prev = curr 
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = prev 
            groupPrev = temp
        return dummy.next 


        