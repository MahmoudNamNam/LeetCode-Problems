from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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



class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Initialize two dummy nodes for partitions
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head
        
        # Traverse the original linked list
        current = head
        while current:
            # If the value is less than x, append it to before partition
            if current.val < x:
                before.next = current
                before = before.next
            # If the value is greater than or equal to x, append it to after partition
            else:
                after.next = current
                after = after.next
            current = current.next
        
        # Connect the end of before partition to the start of after partition
        after.next = None  # Set the end of after partition to None to avoid cycles
        before.next = after_head.next
        
        return before_head.next


# Test case
values = [1, 4, 3, 2, 5, 2]
x = 3
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

solution = Solution()
result = solution.partition(head, x)

print("Linked List after partitioning around", x, ":")
print_linked_list(result)