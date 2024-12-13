import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(n, i) for i, n in enumerate(nums)]
        marked = set()
        heapq.heapify(heap)
        res = 0
        while heap:
            n, i = heapq.heappop(heap)
            if i in marked:
                continue
            
            marked.add(i - 1)
            marked.add(i + 1)
            res += n
        
        return res