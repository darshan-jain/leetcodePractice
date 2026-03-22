# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        dummy = ListNode(0)
        tail = dummy 
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(minheap, (node.val, i, node))
        
        while minheap:
            val, row, node = heapq.heappop(minheap) 
            tail.next= node 
            tail = tail.next 
            if node.next:
                heapq.heappush(minheap, (node.next.val, row, node.next))
        return dummy.next

        