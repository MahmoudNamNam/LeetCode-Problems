from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Find the minimum elements in each row
        min_row_elements = [min(row) for row in matrix]
        
        # Step 2: Find the maximum elements in each column
        max_col_elements = [max(col) for col in zip(*matrix)]
        
        # Step 3: Find the intersection of min_row_elements and max_col_elements
        lucky_numbers = [num for num in min_row_elements if num in max_col_elements]
        
        return lucky_numbers

sol = Solution()
matrix1 = [[3,7,8],[9,11,13],[15,16,17]]
matrix2 = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
matrix3 = [[7,8],[1,2]]


print(sol.luckyNumbers(matrix1))  #* Output: [15]
print(sol.luckyNumbers(matrix2))  #* Output: [12]
print(sol.luckyNumbers(matrix3))  # Output: [7]