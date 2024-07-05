# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """
        Finds the minimum and maximum distances between critical points in a linked list.
        
        Parameters:
        head (Optional[ListNode]): The head node of the linked list.

        Returns:
        List[int]: A list containing two integers - the minimum and maximum distance
                   between any two distinct critical points. If there are fewer than
                   two critical points, return [-1, -1].
        """
        
        # Convert the linked list to a list of node values for easier manipulation
        def nodes_to_list(head):
            lst = []
            while head:
                lst.append(head.val)
                head = head.next
            return lst
        
        # If the list has fewer than 3 nodes, it can't have any critical points
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        # Convert the linked list to a list of node values
        nodes = nodes_to_list(head)
        critical_indices = []

        # Traverse the node values to find critical points
        for i in range(1, len(nodes) - 1):
            if (nodes[i] > nodes[i - 1] and nodes[i] > nodes[i + 1]) or (nodes[i] < nodes[i - 1] and nodes[i] < nodes[i + 1]):
                critical_indices.append(i)
        
        # If there are fewer than 2 critical points, return [-1, -1]
        if len(critical_indices) < 2:
            return [-1, -1]
        
        # Initialize the minimum distance as infinity
        min_distance = float('inf')
        # The maximum distance is between the first and the last critical points
        max_distance = critical_indices[-1] - critical_indices[0]

        # Calculate the minimum distance between consecutive critical points
        for i in range(1, len(critical_indices)):
            min_distance = min(min_distance, critical_indices[i] - critical_indices[i - 1])
        
        return [min_distance, max_distance]

# Example usage:
# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Test cases
solution = Solution()

head1 = create_linked_list([3, 1])
print(solution.nodesBetweenCriticalPoints(head1))  # Output: [-1, -1]

head2 = create_linked_list([5, 3, 1, 2, 5, 1, 2])
print(solution.nodesBetweenCriticalPoints(head2))  # Output: [1, 3]

head3 = create_linked_list([1, 3, 2, 2, 3, 2, 2, 2, 7])
print(solution.nodesBetweenCriticalPoints(head3))  # Output: [3, 3]
