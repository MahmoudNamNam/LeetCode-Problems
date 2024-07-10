from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse both lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
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
        
        # Reverse the result list to get the final answer
        return self.reverseList(dummy.next)