# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: if the list has only one node or no need to reverse
        if head.next == None or left == right:
            return head
        
        # Step 2: Initialize dummy node and pointers
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        
        # Step 3: Traverse to the node just before 'left'
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
        
        # Now, 'cur' is at 'left' and 'leftPrev' is just before 'left'
        
        # Step 4: Reverse the sublist from 'left' to 'right'
        prev = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        
        # Step 5: Reconnect the reversed sublist with the original list
        leftPrev.next.next = cur
        leftPrev.next = prev
        
        # Step 6: Return the new head of the list
        return dummy.next
