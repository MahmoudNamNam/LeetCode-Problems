# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head is not None and head.val in nums:
            head = head.next # Move head forward if its value is in nums

        prv = None
        current = head

        while current :
            if current.val in nums:
                if prv :
                    prv.next = current.next
                else:
                    head = current.next
                current = current.next
            else:
                prv = current
                current = current.next

        return head