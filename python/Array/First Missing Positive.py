from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Rearrange the elements in the array such that each element nums[i] is placed at index nums[i] - 1
        for i in range(n):
            # Continue swapping until the current element is in its correct position
            # or the element is out of the range [1, n]
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1  # Find the correct index for the current element
                # Swap the current element with the element at its correct index
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # After rearranging, find the first index where the element is not in the correct position
        for i in range(n):
            # If an element is not at its correct position, return the expected number at this position
            if nums[i] != i + 1:
                return i + 1

        # If all positions have the correct elements, the missing number is n + 1
        return n + 1

# Example usage:
solution = Solution()
print(solution.firstMissingPositive([1, 2, 0]))      # Output: 3
print(solution.firstMissingPositive([3, 4, -1, 1]))  # Output: 2
print(solution.firstMissingPositive([7, 8, 9, 11, 12]))  # Output: 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        missing = 1

        while(missing in nums):
            missing += 1
        
        return missing
solution = Solution()
print(solution.firstMissingPositive([7, 8, 9, 11, 12]))  # Output: 1