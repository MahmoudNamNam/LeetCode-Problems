from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        for W in range(int(area**.5), 0, -1):
            if area % W == 0:
                L = area // W
                return [L, W]
        return []



sol = Solution()

print(sol.constructRectangle(4))       # Output: [2, 2]
print(sol.constructRectangle(37))      # Output: [37, 1]
print(sol.constructRectangle(122122))  # Output: [427, 286]