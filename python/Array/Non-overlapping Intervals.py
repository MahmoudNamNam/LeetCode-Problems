from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on the end time
        intervals.sort(key=lambda x: x[1])
        
        # Initialize the end time of the previous interval
        prev_end = float('-inf')
        cnt = 0  # Count of intervals to remove
        
        for interval in intervals:
            start, end = interval
            # If the current interval starts before the previous interval ends
            if start < prev_end:
                cnt += 1  # We need to remove this interval
            else:
                # Update the end time of the previous interval
                prev_end = end
        
        return cnt

# Test the solution
sol = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(sol.eraseOverlapIntervals(intervals))  # Output: 1

intervals = [[1,2],[1,2],[1,2]]
print(sol.eraseOverlapIntervals(intervals))  # Output: 2

intervals = [[1,2],[2,3]]
print(sol.eraseOverlapIntervals(intervals))  # Output: 0
