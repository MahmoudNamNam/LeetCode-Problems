from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = 0
        right = 0
        current_sum = 0
        max_fruits = 0
        n = len(fruits)

        def step(left: int, right: int) -> int:
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            else:
                return (fruits[right][0] - fruits[left][0] +
                        min(abs(startPos - fruits[left][0]), abs(startPos - fruits[right][0])))

        while right < n:
            current_sum += fruits[right][1]
            while left <= right and step(left, right) > k:
                current_sum -= fruits[left][1]
                left += 1
            max_fruits = max(max_fruits, current_sum)
            right += 1

        return max_fruits


# Test
sol = Solution()
print(sol.maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4))  # Output: 9
