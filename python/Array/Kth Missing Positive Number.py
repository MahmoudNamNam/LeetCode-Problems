from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        current = 1
        arr_set = set(arr)
        
        while missing_count < k:
            if current not in arr_set:
                missing_count += 1
            if missing_count == k:
                return current
            current += 1
        
        return current
