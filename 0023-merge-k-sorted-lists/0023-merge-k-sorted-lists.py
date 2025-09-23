import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy  = ListNode(0)
        tail = dummy 
        minheap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(minheap, (node.val, i,node))
        
        while minheap:
            val, corelist, node = heapq.heappop(minheap)
            tail.next = ListNode(val = val)
            tail = tail.next
            if node.next:
                heapq.heappush(minheap, (node.next.val, corelist, node.next))
        return dummy.next


        