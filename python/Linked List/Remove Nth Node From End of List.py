class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        # Calculate the length of the linked list
        length = self.length(head)
        
        # Find the index of the node to be removed
        idx = length - n
        
        # Special case: remove the head node
        if idx == 0:
            return head.next
        
        current = head
        # Move to the node just before the one to be removed
        for _ in range(idx - 1):
            current = current.next
        
        # Skip the next node (the one to be removed)
        current.next = current.next.next
        
        return head

    def length(self, head) -> int:
        count = 0
        current = head
        # Calculate the total number of nodes in the list
        while current:
            count += 1
            current = current.next
        return count



class Solution:
    def removeNthFromEnd(self, head, n: int):
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move first pointer n steps ahead
        for _ in range(n+1):
            first = first.next
        
        # Move both pointers until first reaches the end (len - n)
        # second will then point to the node just before the one to be removed
        while first:
            first = first.next
            second = second.next
        
        # Skip the next node (the one to be removed)
        second.next = second.next.next
        
        # Return the head of the modified list, which is dummy.next
        return dummy.next

solution =Solution()

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
values = [1,2,3,4,6,5]
n = 2
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

solution = Solution()
result = solution.removeNthFromEnd(head,2)

print("Linked List after removing duplicates:")
print_linked_list(result)
