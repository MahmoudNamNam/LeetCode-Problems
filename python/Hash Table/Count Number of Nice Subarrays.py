from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        subarrays = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        
        for i in nums:
            curr_sum += i % 2
            if curr_sum - k in prefix_sum:
                subarrays += prefix_sum[curr_sum - k]
            
            # Add/update the current prefix sum in the dictionary
            prefix_sum[curr_sum] += 1
        
        return subarrays

sol = Solution()
nums = [1, 1, 2, 1, 1]
k = 3
print(sol.numberOfSubarrays(nums, k))  # Expected output: 2
