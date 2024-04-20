class Solution:
    def length(self, head):
        """Return the length of the linked list."""
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count

    def deleteMiddle(self, head) :
        if not head or not head.next:  # If the list is empty or has only one node
            return None
        
        # Find the length of the list
        length = self.length(head)
        if length == 1:  # If the list has only one node
            return None
        
        # Find the position of the middle node
        position = length // 2
        
        # Traverse to the middle node
        prev = None
        current = head
        for _ in range(position):
            prev = current
            current = current.next
        
        # Delete the middle node
        prev.next = current.next
        
        return head