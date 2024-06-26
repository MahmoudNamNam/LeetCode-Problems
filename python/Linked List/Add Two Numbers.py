# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carryOver = 0
        
        while l1 or l2 or carryOver > 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            sm = v1 + v2 + carryOver
            carryOver = sm // 10
            sm %= 10
            
            current.next = ListNode(sm)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
