from typing import List

class Solution:
    def isMagicSquare(self, grid: List[List[int]], row: int, col: int) -> bool:
        # Check if the subgrid contains distinct numbers from 1 to 9
        num_set = set()
        for i in range(3):
            for j in range(3):
                num = grid[row + i][col + j]
                if num < 1 or num > 9 or num in num_set:
                    return False
                num_set.add(num)
        
        # Check row sums
        if (grid[row][col] + grid[row][col + 1] + grid[row][col + 2] != 15 or
            grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2] != 15 or
            grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2] != 15):
            return False
        
        # Check column sums
        if (grid[row][col] + grid[row + 1][col] + grid[row + 2][col] != 15 or
            grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1] != 15 or
            grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2] != 15):
            return False
        
        # Check diagonal sums
        if (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] != 15 or
            grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] != 15):
            return False
        
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        # Iterate through each possible 3x3 subgrid
        for i in range(rows - 2):
            for j in range(cols - 2):
                if self.isMagicSquare(grid, i, j):
                    count += 1
        
        return count

# Example usage:
grid1 = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
grid2 = [[8]]
solution = Solution()

print(solution.numMagicSquaresInside(grid1))  # Output: 1
print(solution.numMagicSquaresInside(grid2))  # Output: 0
