# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert_sorted(self, head, new_node):
        # Handle empty list or new node smaller than head
        if not head or new_node.val < head.val:
            new_node.next = head
            head = new_node
            return head  # Return new head if insertion is at the beginning

        # Traverse to find the insertion position
        prev = head
        current = head.next
        while current and current.val < new_node.val:
            prev = current
            current = current.next

        # Insert the new node between prev and current
        prev.next = new_node
        new_node.next = current
        return head  # Return head of the list

    def insertionSortList(self, head):
        if not head:
            return None

        sorted_list = None
        current = head
        while current:
            next_node = current.next
            sorted_list = self.insert_sorted(sorted_list, current)
            current = next_node

        return sorted_list
