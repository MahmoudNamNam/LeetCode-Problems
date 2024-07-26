from heapq import heappush, heappop
from typing import List, Optional

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         # Min-heap to store (node value, index in lists, node)
#         min_heap = []
        
#         # Initialize the heap with the head of each linked list
#         for i, lst in enumerate(lists):
#             if lst:
#                 heappush(min_heap, (lst.val, i, lst))
        
#         # Dummy node to serve as the head of the merged linked list
#         dummy = ListNode()
#         current = dummy
        
#         while min_heap:
#             # Pop the smallest node from the heap
#             _, i, node = heappop(min_heap)
#             # Add this node to the merged linked list
#             current.next = node
#             current = current.next
#             # If the popped node has a next node, push it into the heap
#             if node.next:
#                 heappush(min_heap, (node.next.val, i, node.next))
        
#         return dummy.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_nodes(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def nodes_to_list(node):
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop
        
        min_heap = []
        
        for i, lst in enumerate(lists):
            if lst:
                heappush(min_heap, (lst.val, i, lst))
        
        dummy = ListNode()
        current = dummy
        
        while min_heap:
            val, i, node = heappop(min_heap)
            print(f"Popped node with value {val} from list {i}")  # Debugging statement
            current.next = node
            current = current.next
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
                print(f"Pushed node with value {node.next.val} from list {i}")  # Debugging statement
        
        return dummy.next

# Specific test case
test_case = ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])

# Convert input lists to linked lists
input_lists = [list_to_nodes(lst) for lst in test_case[0]]

# Merge the linked lists
solution = Solution()
merged_head = solution.mergeKLists(input_lists)

# Convert the merged linked list back to a regular list
result = nodes_to_list(merged_head)

# Print result for debugging
print("Result:", result)
print("Expected:", test_case[1])

# Verify the result
assert result == test_case[1], f"Test case failed: {test_case[0]}, expected {test_case[1]}, got {result}"

print("Test case passed!")
