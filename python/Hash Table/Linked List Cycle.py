from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Check if the list is empty or has only one node
        # A list with 0 or 1 nodes cannot have a cycle
        if not head or not head.next:
            return False
        
        seen = set()
        
        # Traverse the linked list
        while head:
            # If the current node is already in the set, we have a cycle
            if head in seen:
                return True
            
            # Otherwise, add the current node to the set
            seen.add(head)
            
            # Move to the next node
            head = head.next
        
        # If we reach the end of the list, there is no cycle
        return False
