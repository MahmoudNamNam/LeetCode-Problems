import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            rem = math.floor(math.sqrt(largest))
            heapq.heappush(max_heap, -rem)
        
        return -sum(max_heap)

# Example usage
sol = Solution()
print(sol.pickGifts(gifts=[25, 64, 9, 4, 100], k=4))  # Output: 29
