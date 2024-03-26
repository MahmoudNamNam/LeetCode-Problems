from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    



# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list values
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)

# Test case
values = [1, 1, 2, 3, 3]
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

solution = Solution()
result = solution.deleteDuplicates(head)

print("Linked List after removing duplicates:")
print_linked_list(result)
