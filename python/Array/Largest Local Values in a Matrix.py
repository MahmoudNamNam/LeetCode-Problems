class Solution:
    def find_max(self, grid, x, y):
        max_element = float('-inf')  
        
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if i < len(grid) and j < len(grid[0]):
                    max_element = max(max_element, grid[i][j])
        
        return max_element

    def largestLocal(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        if rows < 3 or cols < 3:
            return None 
        
        max_local = [[0] * (cols - 2) for _ in range(rows - 2)]
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                max_local[i][j] = self.find_max(grid, i, j)
        
        return max_local



sol = Solution()

print(sol.largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))