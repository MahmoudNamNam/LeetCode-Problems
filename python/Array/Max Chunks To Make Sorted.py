from typing import List


class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        max_seen = 0
        chunks = 0
        
        for i, value in enumerate(arr):
            max_seen = max(max_seen, value)
            if max_seen == i:
                chunks += 1
                
        return chunks