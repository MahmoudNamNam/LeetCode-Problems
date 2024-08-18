from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = float('inf')
        max_val = float('-inf')
        max_distance = 0
        
        for array in arrays:
            if min_val != float('inf'):
                max_distance = max(max_distance, abs(array[-1] - min_val))
            if max_val != float('-inf'):
                max_distance = max(max_distance, abs(max_val - array[0]))
            
            min_val = min(min_val, array[0])
            max_val = max(max_val, array[-1])
        
        return max_distance
