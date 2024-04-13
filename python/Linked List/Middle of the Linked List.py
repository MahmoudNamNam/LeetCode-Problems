# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self,head):
        """Return the length of the linked list."""
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
    def middleNode(self, head) :
        count = 0
        position = self.length(head)//2
        current = head
        while current:
            if count == position:
                return current
            count += 1
            current = current.next