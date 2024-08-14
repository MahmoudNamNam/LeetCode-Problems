from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        fast = head
        slow = head

        # Move the 'fast' pointer to the k-th node from the beginning
        for i in range(k - 1):
            if fast is None:
                return head  # If k is out of bounds, return the list as is
            fast = fast.next

        # Save the reference to the k-th node from the beginning
        first = fast
        fast = fast.next  # Move the 'fast' pointer one step ahead

        # Move both 'fast' and 'slow' pointers until 'fast' reaches the end of the list
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # 'slow' now points to the k-th node from the end
        # Swap the values of the first and slow nodes
        first.val, slow.val = slow.val, first.val 
        
        return head
