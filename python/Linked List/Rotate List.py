class Solution:
    def rotateRight(self, head, k: int) -> ListNode: # type: ignore
        """
        Rotate a linked list to the right by a given number of positions.

        Args:
            head: The head node of the linked list to be rotated.
            k: The number of positions to rotate the linked list to the right.

        Returns:
            The head node of the rotated linked list.

        """
        if not head or k <= 0:
            return head

        # Find the length of the linked list and the last node
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # Adjust k to be within the range of the list
        k %= length

        if k == 0:
            return head

        # Find the (k+1)th node from the end
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Rotate the list
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
