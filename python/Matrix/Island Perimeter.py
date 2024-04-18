from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4  # Start with the maximum perimeter for each land cell
                    if i > 0 and grid[i - 1][j] == 1:  # Check above
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:  # Check left
                        perimeter -= 2

        return perimeter




s =Solution()
s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])