# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        tail = None

        while cur:
            next_node = cur.next

            # Break the cycle
            cur.next = tail

            # Move pointers
            tail = cur
            cur = next_node

        return tail

class Solution(object):
    def reverseList(self, head):
        """
        Reverse a singly-linked list in-place.

        :param head: The head of the linked list.
        :type head: ListNode
        :return: The new head of the reversed linked list.
        :rtype: ListNode
        """

        # Initialize 'next' pointer to None (as it will become the new tail)
        reversed_head = None

        # Traverse the original list
        while head:
            # Save the next node before changing 'head.next'
            next_node = head.next

            # Reverse the link by pointing 'head.next' to the reversed part
            head.next = reversed_head

            # Move the pointers forward
            reversed_head = head
            head = next_node

        # Return the new head of the reversed list
        return reversed_head
