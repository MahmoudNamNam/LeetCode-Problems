from typing import List
from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        idx_q = deque()
        min_len = float('inf') 

        # Iterate over the prefix sum array
        for i in range(n + 1):
            # Check if we have a valid subarray
            while idx_q and prefix_sum[i] - prefix_sum[idx_q[0]] >= k:
                min_len = min(min_len, i - idx_q.popleft())

            # Maintain the increasing order of the queue
            while idx_q and prefix_sum[i] <= prefix_sum[idx_q[-1]]:
                idx_q.pop()

            # Add the current index to the queue
            idx_q.append(i)

        return min_len if min_len != float('inf') else -1


sol = Solution()
print(sol.shortestSubarray(nums = [2,-1,2,3], k = 3))
# print(sol.shortestSubarray())