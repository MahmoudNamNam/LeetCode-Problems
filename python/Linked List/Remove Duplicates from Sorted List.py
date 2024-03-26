class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None  # If the list is empty, return None
        
        current = head  # Start from the head of the list

        while current.next:  # Traverse until the end of the list
            if current.val == current.next.val:  # If current node's value is equal to next node's value
                current.next = current.next.next  # Skip the next node by pointing current's next to the one after next
            else:
                current = current.next  # Move to the next node
        
        return head  # Return the modified head of the list

