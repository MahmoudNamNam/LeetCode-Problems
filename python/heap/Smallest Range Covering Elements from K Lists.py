import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        
        # Initialize the heap with the first element from each list and track the max value
        max_value = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))  # (value, list_index, element_index)
            max_value = max(max_value, nums[i][0])
        
        best_range = [float('-inf'), float('inf')]
        
        while min_heap:
            min_value, row, idx = heapq.heappop(min_heap)
            
            # Update the range if it's smaller than the best range found so far
            if max_value - min_value < best_range[1] - best_range[0]:
                best_range = [min_value, max_value]
            
            # If we have more elements in the current list, push the next one into the heap
            if idx + 1 < len(nums[row]):
                next_value = nums[row][idx + 1]
                heapq.heappush(min_heap, (next_value, row, idx + 1))
                max_value = max(max_value, next_value)
            else:
                # If any of the lists is exhausted, stop the process
                break
        
        return best_range


sol = Solution()
print(sol.smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
print(sol.smallestRange([[1,2,3],[1,2,3],[1,2,3]]))