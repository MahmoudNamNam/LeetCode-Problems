from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k:
                combinations.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        combinations = []
        backtrack(1, [])
        return combinations

# Test cases
solution = Solution()
print(solution.combine(4, 2))  # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(solution.combine(1, 1))  # Output: [[1]]



# Another sol Using itertools

from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(range(1, n+1), k)
    
solution = Solution()
print(*solution.combine(4, 2))  # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(*solution.combine(1, 1))  # Output: [[1]]

