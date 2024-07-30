from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        second = float('-inf')  # This will store the potential "2" in the 132 pattern
        
        for num in reversed(nums):
            if num < second:
                return True
            while stack and num > stack[-1]:
                second = stack.pop()
            stack.append(num)
        
        return False
    

sol=Solution()

print(sol.find132pattern([1, 2, 3, 4]))  # Output: False
print(sol.find132pattern([3, 1, 4, 2]))  # Output: True
print(sol.find132pattern([-1, 3, 2, 0])) # Output: True