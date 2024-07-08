from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_length = 0
        i = 0
        while i < len(nums):
            # Find the start of the new valid subarray
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                start = i
                current_length = 1
                i += 1
                # Expand the subarray while conditions are met
                while i < len(nums) and nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                    current_length += 1
                    i += 1
                # Update the maximum length found
                max_length = max(max_length, current_length)
            else:
                i += 1
        
        return max_length

# Example Usage
sol = Solution()
print(sol.longestAlternatingSubarray([3, 2, 5, 4], 5))  # Output: 3
print(sol.longestAlternatingSubarray([1, 2], 2))        # Output: 1
print(sol.longestAlternatingSubarray([2, 3, 4, 5], 4))  # Output: 3
