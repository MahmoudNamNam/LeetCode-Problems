# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one node, there can't be a cycle
        if not head or not head.next:
            return None
        
        # Initialize two pointers: slow and fast
        slow = head
        fast = head
        
        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next         # Move slow pointer by one step
            fast = fast.next.next    # Move fast pointer by two steps
            
            if slow == fast:         # Cycle detected
                # Step 2: Find the start of the cycle
                slow2 = head
                while slow2 != slow:
                    slow = slow.next
                    slow2 = slow2.next
                
                # Both pointers meet at the start of the cycle
                return slow
        
        # If no cycle exists, return None
        return None
