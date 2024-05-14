from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxGold = 0
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in visited:
                return 0
            visited.add((i, j))
            currentGold = grid[i][j]
            maxPathGold = max(dfs(i+1, j), dfs(i-1, j), dfs(i, j+1), dfs(i, j-1))
            visited.remove((i, j))  
            return currentGold + maxPathGold

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, dfs(i, j))

        return maxGold

grid1 = [[0,6,0],[5,8,7],[0,9,0]]
grid2 = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]

sol = Solution()
print(sol.getMaximumGold(grid1))  # Output: 24
print(sol.getMaximumGold(grid2))  # Output: 28
