from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            # If the target is found, return its index
            if nums[mid] == target:
                return mid
            
            # Determine which portion is sorted
            if nums[left] <= nums[mid]:
                # Left portion is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right portion is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # Target not found
        return -1

# Example usage:
solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1
print(solution.search([1], 0))                    # Output: -1
