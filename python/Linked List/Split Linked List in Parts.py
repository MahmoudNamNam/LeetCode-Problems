# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.countNodes(head)
        parts, r = divmod(n, k)
        res = [None] * k
        curr = head
        for i in range(k):
            res[i] = curr
            for _ in range(parts + (r > 0) - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            r -= 1
        return res

    def countNodes(self, head: ListNode) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count

def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Create a linked list from the array [1,2,3,4,5,6,7,8,9,10]
head = create_linked_list([1,2,3,4,5,6,7,8,9,10])

# Split the linked list into k parts
sol = Solution()
result = sol.splitListToParts(head, 3)

# Print the result
for part in result:
    values = []
    while part:
        values.append(part.val)
        part = part.next
    print(values)
