from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
    
    def merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left_half = self.merge_sort(nums[:mid])
        right_half = self.merge_sort(nums[mid:])
        
        return self.merge(left_half, right_half)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_array = []
        i = j = 0
        
        # Merge the two halves together
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        
        # If there are remaining elements in the left half, add them
        while i < len(left):
            sorted_array.append(left[i])
            i += 1
        
        # If there are remaining elements in the right half, add them
        while j < len(right):
            sorted_array.append(right[j])
            j += 1
        
        return sorted_array

