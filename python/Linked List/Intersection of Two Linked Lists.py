from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        def get_length(head: Optional[ListNode]) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        lenA = get_length(headA)
        lenB = get_length(headB)
        
        # Align both lists by advancing the longer list by the difference in lengths
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        
        # Traverse both lists simultaneously to find the intersection
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None

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

# Helper function to find a node by value.
def find_node_by_value(head, value):
    while head:
        if head.val == value:
            return head
        head = head.next
    return None

# Test cases
# Example 1
listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]
skipA = 2
skipB = 3

headA = create_linked_list(listA)
headB = create_linked_list(listB)

# Creating the intersection
intersect_node = find_node_by_value(headA, 8)
headB_ptr = headB
for _ in range(skipB):
    headB_ptr = headB_ptr.next
headB_ptr.next = intersect_node

solution = Solution()
result = solution.getIntersectionNode(headA, headB)
print(result.val if result else "No intersection")  # Output: 8

# Example 2
listA = [1, 9, 1, 2, 4]
listB = [3, 2, 4]
skipA = 3
skipB = 1

headA = create_linked_list(listA)
headB = create_linked_list(listB)

# Creating the intersection
intersect_node = find_node_by_value(headA, 2)
headB_ptr = headB
for _ in range(skipB):
    headB_ptr = headB_ptr.next
headB_ptr.next = intersect_node

result = solution.getIntersectionNode(headA, headB)
print(result.val if result else "No intersection")  # Output: 2

# Example 3
listA = [2, 6, 4]
listB = [1, 5]

headA = create_linked_list(listA)
headB = create_linked_list(listB)

result = solution.getIntersectionNode(headA, headB)
print(result.val if result else "No intersection")  # Output: No intersection
