class Solution:
    def removeElements(self, head: Optional[ListNode], key: int) -> Optional[ListNode]: #type: ignore
        # Handle cases where the head node(s) need to be removed
        while head is not None and head.val == key:
            head = head.next

        prv = None
        current = head

        # Traverse the list and remove nodes with the specified key
        while current :
            if current.val == key:
                # Skip the node with the specified key
                if prv :
                    prv.next = current.next
                else:
                    # If prv is None, it means we are at the head node
                    head = current.next
                current = current.next
            else:
                prv = current
                current = current.next

        return head
