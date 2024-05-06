from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        next_greater = self.removeNodes(current.next)
        current.next = next_greater
        if not next_greater or current.val >= next_greater.val:
            return current
        return next_greater