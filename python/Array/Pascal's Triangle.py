from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==1:
            return [[1]]
        triangle = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        return triangle
        

sol = Solution()
print(sol.generate(5))


"""
Initial triangle with 1s only:
[[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]

Processing row 2:
  triangle[2][1] = 1 + 1 = 2
Completed row 2: [1, 2, 1]

Processing row 3:
  triangle[3][1] = 1 + 2 = 3
  triangle[3][2] = 2 + 1 = 3
Completed row 3: [1, 3, 3, 1]

Processing row 4:
  triangle[4][1] = 1 + 3 = 4
  triangle[4][2] = 3 + 3 = 6
  triangle[4][3] = 3 + 1 = 4
Completed row 4: [1, 4, 6, 4, 1]

Final triangle:
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
"""