from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        
        while i < j:
            current_sum = numbers[i] + numbers[j]
            
            if current_sum == target:
                return [i + 1, j + 1]  # Return 1-based indices as required by the problem
            elif current_sum < target:
                i += 1  # Move the left pointer to increase the sum
            else:
                j -= 1  # Move the right pointer to decrease the sum
        
        return []  # If no valid solution is found, return an empty list
