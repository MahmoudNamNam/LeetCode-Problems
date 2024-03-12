from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Sort the array in descending order
        nums.sort(reverse=True)
        
        # Initialize the number of operations
        operations = 0
        
        # Iterate through the sorted array
        for i in range(1, len(nums)):
            # If the current element is not equal to the next element
            if nums[i] != nums[i-1]:
                # Increase the number of operations by the current index
                operations += i
        
        return operations



solution = Solution()
print(solution.reductionOperations([5,1,3]))  # Output: 3
print(solution.reductionOperations([1,1,1]))  # Output: 0
print(solution.reductionOperations([1,1,2,2,3]))  # Output: 4
