from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        def backtrack(idx, val):
            # Base case: when all elements have been considered
            if idx == n:
                # Check if the current value equals the target
                return 1 if val == target else 0
            
            # Recursively try adding and subtracting the current number
            return backtrack(idx + 1, val + nums[idx]) + backtrack(idx + 1, val - nums[idx])
        
        return backtrack(0, 0)

sol = Solution()
print(sol.findTargetSumWays(nums = [1,1,1,1,1], target = 3))  # Output should be 5
print(sol.findTargetSumWays(nums = [1], target = 1))          # Output should be 1
"""

Time Limit Exceeded

"""

#  Use Memo 

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        
        def backtrack(idx, current_sum):
            # Base case: when all elements have been considered
            if idx == n:
                return 1 if current_sum == target else 0
            
            # Check if result is already computed for the current state
            if (idx, current_sum) in memo:
                return memo[(idx, current_sum)]
            
            # Recursively try adding and subtracting the current number
            add = backtrack(idx + 1, current_sum + nums[idx])
            subtract = backtrack(idx + 1, current_sum - nums[idx])
            
            # Store the result in memo
            memo[(idx, current_sum)] = add + subtract
            
            return memo[(idx, current_sum)]
        
        return backtrack(0, 0)

sol = Solution()
print(sol.findTargetSumWays(nums = [1,1,1,1,1], target = 3))  # 5
print(sol.findTargetSumWays(nums = [1], target = 1))          #  1
