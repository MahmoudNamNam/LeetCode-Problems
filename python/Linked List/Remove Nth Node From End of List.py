class Solution:
    def removeNthFromEnd(self, head, n: int):
        length = self.length(head)
        idx = length - n - 1
        
        if idx == -1:
            return head.next
        
        if idx < 0 or idx >= length:
            return head
        
        current = head
        for _ in range(idx):
            current = current.next
        
        current.next = current.next.next
        return head

    def length(self, head) -> int:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count