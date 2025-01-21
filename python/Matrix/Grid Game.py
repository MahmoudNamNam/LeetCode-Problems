from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        min_result = float('inf')
        row1_sum = sum(grid[0])
        row2_sum = 0
        
        for i in range(len(grid[0])):
            row1_sum -= grid[0][i]
            min_result = min(min_result, max(row1_sum, row2_sum))
            row2_sum += grid[1][i]
        
        return min_result
    
sol = Solution()
grid = [[2,5,4],[1,5,1]]
print(sol.gridGame(grid))  # 4

grid = [[3,3,1],[8,5,2]]
print(sol.gridGame(grid))  # 4