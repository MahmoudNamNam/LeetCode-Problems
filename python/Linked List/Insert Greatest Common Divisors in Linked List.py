# Definition for singly-linked list.
from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  
        
        current = head
        while current and current.next:
            # Calculate the GCD between current node and next node
            gcd_value = math.gcd(current.val, current.next.val)
            
            # Create a new node with the GCD value
            new_node = ListNode(gcd_value)
            
            # Insert the new node between current and current.next
            new_node.next = current.next
            current.next = new_node
            
            # Move the current pointer two steps forward
            current = new_node.next
        
        return current
