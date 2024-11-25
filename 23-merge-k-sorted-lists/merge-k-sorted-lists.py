import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap,(node.val,i,node))
        dummy = ListNode(0)
        curr = dummy
        while min_heap:
            val,i,node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_heap,(node.next.val,i,node.next))
        return dummy.next

        