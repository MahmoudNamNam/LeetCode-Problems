from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result list with the first interval
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # Get the last interval in the result list
            last_interval = res[-1]
            current_interval = intervals[i]
            
            # Check if there is an overlap
            if last_interval[1] >= current_interval[0]:
                # Merge the intervals by updating the end time
                last_interval[1] = max(last_interval[1], current_interval[1])
            else:
                # No overlap, so add the current interval to the result list
                res.append(current_interval)
        
        return res

# Test the solution
sol = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(sol.merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]
