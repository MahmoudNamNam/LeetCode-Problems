# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to hold the merged list
        dummy = ListNode(-1)
        current = dummy
        
        # Traverse both lists and compare values
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in list1 or list2, append them
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2
        
        # Return the merged list starting from the next of the dummy node
        return dummy.next
