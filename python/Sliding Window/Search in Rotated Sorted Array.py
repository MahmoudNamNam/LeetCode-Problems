from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize the deque and the result list
        deq = deque()
        result = []
        
        for i in range(len(nums)):
            # Remove elements not in the sliding window
            if deq and deq[0] == i - k:
                deq.popleft()
            
            # Remove elements smaller than the current element
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            # Add the current element at the end of the deque
            deq.append(i)
            
            # The front of the deque is the largest element of the current window
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result

# Example usage:
sol = Solution()
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k = 3))  # Output: [3, 3, 5, 5, 6, 7]
