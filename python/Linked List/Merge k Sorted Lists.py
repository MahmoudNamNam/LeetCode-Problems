from heapq import heappush, heappop
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to store (node value, index in lists, node)
        min_heap = []
        
        # Initialize the heap with the head of each linked list
        for i, lst in enumerate(lists):
            if lst:
                heappush(min_heap, (lst.val, i, lst))
        
        # Dummy node to serve as the head of the merged linked list
        dummy = ListNode()
        current = dummy
        
        while min_heap:
            # Pop the smallest node from the heap
            _, i, node = heappop(min_heap)
            # Add this node to the merged linked list
            current.next = node
            current = current.next
            # If the popped node has a next node, push it into the heap
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next