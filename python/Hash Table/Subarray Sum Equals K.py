from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        sum_dict = defaultdict(int)
        
        # Initialize with 0 to handle the case where the subarray starts from the beginning
        sum_dict[0] = 1
        
        for num in nums:
            current_sum += num
            
            # If (current_sum - k) exists in sum_dict, then there exists a subarray
            # ending at the current index with sum k
            if current_sum - k in sum_dict:
                count += sum_dict[current_sum - k]
            
            # Add/update the current_sum in the dictionary
            sum_dict[current_sum] += 1
        
        return count

sol = Solution()
nums = [1, 1, 1]
k = 2
print(sol.subarraySum(nums, k))  # Output should be 2

nums = [1,2,3]
k = 3
print(sol.subarraySum(nums, k))  # Output should be 1