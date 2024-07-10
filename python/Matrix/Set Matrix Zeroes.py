from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])  # Get the number of rows and columns
        
        # Determine if the first row needs to be zeroed out
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        
        # Determine if the first column needs to be zeroed out
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use the first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:  # If an element is zero
                    matrix[i][0] = 0  # Set the corresponding element in the first column to zero
                    matrix[0][j] = 0  # Set the corresponding element in the first row to zero
        
        # Zero out rows based on markers in the first column
        for i in range(1, m):
            if matrix[i][0] == 0:  # If the marker is zero
                for j in range(1, n):
                    matrix[i][j] = 0  # Set the entire row to zero
        
        # Zero out columns based on markers in the first row
        for j in range(1, n):
            if matrix[0][j] == 0:  # If the marker is zero
                for i in range(1, m):
                    matrix[i][j] = 0  # Set the entire column to zero
        
        # Zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0  # Set the first row to zero
        
        # Zero out the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0  # Set the first column to zero

# Test cases
solution = Solution()

# Test case 1
matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
solution.setZeroes(matrix1)
print(matrix1)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

# Test case 2
matrix2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
solution.setZeroes(matrix2)
print(matrix2)  # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

# Test case 3
matrix3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
solution.setZeroes(matrix3)
print(matrix3)  # Output: [[1, 2, 0], [4, 5, 0], [0, 0, 0]]

# Test case 4
matrix4 = [
    [0, 1],
    [1, 1]
]
solution.setZeroes(matrix4)
print(matrix4)  # Output: [[0, 0], [0, 1]]
