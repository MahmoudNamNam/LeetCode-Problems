from typing import List

class Solution:
    def binarySearch(self, nums, target, findFirst):
        low = 0
        high = len(nums) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                result = mid
                if findFirst:
                    high = mid - 1  # Look on the left side for the first occurrence
                else:
                    low = mid + 1  # Look on the right side for the last occurrence
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Check if the list is empty or target is out of the range of nums
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        start = self.binarySearch(nums, target, True)
        end = self.binarySearch(nums, target, False)
        
        return [start, end]
