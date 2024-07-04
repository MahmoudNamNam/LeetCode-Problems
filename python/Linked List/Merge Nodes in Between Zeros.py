# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to help with constructing the new list
        dummy = ListNode()
        # This will store the sum of values between zeroes
        sum_val = 0
        # Move the head to the first node after the initial zero
        head = head.next
        # Current pointer for constructing the new list
        cur = dummy
        
        # Iterate through the linked list
        while head:
            if head.val == 0:
                # When encountering a zero, create a new node with the sum and add it to the new list
                cur.next = ListNode(sum_val)
                cur = cur.next  # Move the current pointer
                sum_val = 0  # Reset sum_val for the next segment
            else:
                # Add the current node's value to sum_val
                sum_val += head.val
            # Move to the next node
            head = head.next
        
        # Return the new list starting from the node after the dummy
        return dummy.next

# Example usage:
# Create a linked list [0, 3, 1, 0, 4, 5, 2, 0]
head = ListNode(0)
head.next = ListNode(3)
head.next.next = ListNode(1)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next = ListNode(0)

# Call the function
sol = Solution()
new_head = sol.mergeNodes(head)

# Print the new linked list
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
# Output should be: 4 -> 11
