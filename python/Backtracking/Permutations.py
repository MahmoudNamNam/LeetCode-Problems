from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                permutations.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        permutations = []
        backtrack([])
        return permutations

# Test cases
solution = Solution()
print(solution.permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(solution.permute([0, 1]))      # Output: [[0, 1], [1, 0]]
print(solution.permute([1]))         # Output: [[1]]



# Another sol Using itertools

from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(perm) for perm in permutations(nums)]
    
solution = Solution()
print(solution.permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(solution.permute([0, 1]))      # Output: [[0, 1], [1, 0]]
print(solution.permute([1]))         # Output: [[1]]