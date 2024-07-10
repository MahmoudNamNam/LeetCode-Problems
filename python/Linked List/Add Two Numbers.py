from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to form the resultant linked list.
        dummy = ListNode(0)
        current = dummy
        carryOver = 0
        
        # Loop until both l1 and l2 are exhausted and there's no carry over left.
        while l1 or l2 or carryOver > 0:
            # Get the value of the current nodes, or 0 if the node is None.
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate the sum of the values and the carry over.
            sm = v1 + v2 + carryOver
            # Update carryOver for the next iteration.
            carryOver = sm // 10
            # Get the last digit of the sum to store in the new node.
            sm %= 10
            
            # Add the sum value as a new node to the result linked list.
            current.next = ListNode(sm)
            current = current.next
            
            # Move to the next nodes in l1 and l2.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the next node of dummy which is the head of the resultant linked list.
        return dummy.next

# Helper function to create a linked list from a list of values.
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list back to a list of values.
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [7, 0, 8]

l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [0]

l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
