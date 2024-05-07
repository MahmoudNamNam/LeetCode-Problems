from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, node: ListNode) -> ListNode:
        previous, current = None, node
        while current:
            next_node = current.next
            current.next = previous
            previous, current = current, next_node
        return previous

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        rev = self.reverse(head)
        carry = 0
        current, previous = rev, None
        
        while current:
            new_value = current.val * 2 + carry
            current.val = new_value % 10
            carry = new_value // 10  
            previous, current = current, current.next

        # If there's any remaining carry, create a new node
        if carry:
            previous.next = ListNode(carry)

        # Reverse the list again to restore the original order
        result = self.reverse(rev)

        return result
