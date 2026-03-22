# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        minheap = []
        dummy = ListNode(0)
        tail = dummy 
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(minheap, (node.val,i,node) )#node.val for the actual comparision
        #print(minheap)
        while minheap:
            val,row, node = heapq.heappop(minheap)
            tail.next = node 
            tail = tail.next 
            if node.next:
                heapq.heappush(minheap, (node.next.val,row, node.next))
        return dummy.next



        