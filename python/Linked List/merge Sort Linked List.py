# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:# type: ignore
        if not head or not head.next:
            return head
        
        middle = self.find_middle(head)
        left_half = head
        right_half = middle.next
        middle.next = None
        
        left_sorted = self.sortList(left_half)
        right_sorted = self.sortList(right_half)
        
        return self.merge(left_sorted, right_sorted)
    
    def find_middle(self, head: ListNode) -> ListNode:# type: ignore
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode: # type: ignore
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        
        return dummy.next
