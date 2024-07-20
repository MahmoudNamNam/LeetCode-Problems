from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Get the dimensions of the matrix
        m, n = len(rowSum), len(colSum)
        
        # Initialize the matrix with zeros
        matrix = [[0] * n for _ in range(m)]
        
        # Iterate through the matrix to fill it with appropriate values
        i, j = 0, 0
        while i < m and j < n:
            # Find the minimum value that can be placed in matrix[i][j]
            val = min(rowSum[i], colSum[j])
            
            # Place the value in the matrix
            matrix[i][j] = val
            
            # Subtract the placed value from the respective row sum and column sum
            rowSum[i] -= val
            colSum[j] -= val
            
            # Move to the next row or column if the current row or column sum is satisfied
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        
        return matrix